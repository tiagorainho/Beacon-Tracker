import numpy as np, math, subprocess
from beacontools import BeaconScanner, EddystoneTLMFrame, BluetoothAddressType, EddystoneUIDFrame
from time import time
from beepy import beep

import requests

base_url = 'http://192.168.42.203:5001/'
user_id = 0

def CalcularPosicao3(signals,old_pos): 
    # Recebe     # Recebe  dist[0]dos com forma : [Localization,PowerSent,PowerReceived] e localization = (lat,lon,height) ta sem altura
    earthR = 6371

    Pos=[static_info[s][1] for s in signals]
    PowerSent=[static_info[s][0] for s in signals]
    PowerReceived=[np.mean(signals[s][0]) for s in signals]

    dist=[(PowerSent[i]/(4*np.pi * PowerReceived[i]))**(1/2) * Area for i in range(3)]

    xA = (earthR) *(math.cos(math.radians(Pos[0][0])) * math.cos(math.radians(Pos[0][1])))
    yA = (earthR) *(math.cos(math.radians(Pos[0][0])) * math.sin(math.radians(Pos[0][1])))
    zA = (earthR) *(math.sin(math.radians(Pos[0][0])))

    xB = (earthR) *(math.cos(math.radians(Pos[1][0])) * math.cos(math.radians(Pos[1][1])))
    yB = (earthR) *(math.cos(math.radians(Pos[1][0])) * math.sin(math.radians(Pos[1][1])))
    zB = (earthR) *(math.sin(math.radians(Pos[1][0])))

    xC = (earthR) *(math.cos(math.radians(Pos[2][0])) * math.cos(math.radians(Pos[2][1])))
    yC = (earthR) *(math.cos(math.radians(Pos[2][0])) * math.sin(math.radians(Pos[2][1])))
    zC = (earthR) *(math.sin(math.radians(Pos[2][0])))

    P1 = np.array([xA, yA, zA])
    P2 = np.array([xB, yB, zB])
    P3 = np.array([xC, yC, zC])

    ex = (P2 - P1)/(np.linalg.norm(P2 - P1))
    i = np.dot(ex, P3 - P1)
    ey = (P3 - P1 - i*ex)/(np.linalg.norm(P3 - P1 - i*ex))
    ez = np.cross(ex,ey)
    d = np.linalg.norm(P2 - P1)
    j = np.dot(ey, P3 - P1)


    x = (pow(dist[0],2) - pow(dist[1],2) + pow(d,2))/(2*d)
    y = ((pow(dist[0],2) - pow(dist[2],2) + pow(i,2) + pow(j,2))/(2*j)) - ((i/j)*x)
    z = np.sqrt(pow(dist[0],2) - pow(x,2) - pow(y,2))
    print(z)

    tmp=pow(dist[0],2) - pow(x,2) - pow(y,2)
    if pow(dist[0],2) - pow(x,2) - pow(y,2)>0:
        z=np.sqrt(tmp)
    else:
        print("Ligma balls")


    triPt = P1 + x*ex + y*ey + z*ez
    lat = math.degrees(math.asin(triPt[2] / earthR))
    lon = math.degrees(math.atan2(triPt[1],triPt[0]))

    new_pos=lat, lon, int(np.average([Pos[0][2],Pos[1][2],Pos[2][2]]))
    if new_pos!=old_pos:
        #print(signals.keys())
        #print([signals[s][0] for s in signals])
        
        idx=0
        for s in signals:
            print("{}: {}".format(s[0],dist[idx]*1000))
            idx+=1

    
    return new_pos

def CalcularPosicao2(signals,old_pos):
    earthR = 6371

    Pos=[static_info[s][1] for s in signals]
    PowerSent=[static_info[s][0] for s in signals]
    PowerReceived=[np.mean(signals[s][0]) for s in signals]

    dist=[(PowerSent[i]/(4*np.pi * PowerReceived[i]))**(1/2) * Area for i in range(2)]

    xA = (earthR) *(math.cos(math.radians(Pos[0][0])) * math.cos(math.radians(Pos[0][1])))
    yA = (earthR) *(math.cos(math.radians(Pos[0][0])) * math.sin(math.radians(Pos[0][1])))
    zA = (earthR) *(math.sin(math.radians(Pos[0][0])))

    xB = (earthR) *(math.cos(math.radians(Pos[1][0])) * math.cos(math.radians(Pos[1][1])))
    yB = (earthR) *(math.cos(math.radians(Pos[1][0])) * math.sin(math.radians(Pos[1][1])))
    zB = (earthR) *(math.sin(math.radians(Pos[1][0])))

    x = (dist[1]*xA + dist[0]*xB)/(dist[0]+dist[1])
    y = (dist[1]*yA + dist[0]*yB)/(dist[0]+dist[1])
    z = (dist[1]*zA + dist[0]*zB)/(dist[0]+dist[1])

    lat = math.degrees(math.asin(z / earthR))
    lon = math.degrees(math.atan2(y,x))

    new_pos=lat,lon, int(np.average([Pos[0][2],Pos[1][2]]))
    if new_pos!=old_pos:
        #print(signals.keys())
        #print([signals[s][0] for s in signals])
        
        idx=0
        for s in signals:
            print("{}: {}".format(s[0],dist[idx]*1000))
            idx+=1

    return lat,lon, int(np.average([Pos[0][2],Pos[1][2]]))

def verification(signals):
    delete=[]
    for s in signals.keys():
        if time()-signals[s][1]>0.6:
            delete.append(s)
    for d in delete:
        del signals[d]
    if len(signals)>3:
        min_pow=0
        min_s=0
        for s in signals:
            if signals[s][0]<min_pow:
                min_pow=signals[s][0]
                min_s=s
        del signals[min_s]

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s  @ %s" % (bt_addr, rssi, packet, additional_info))
    global last_verification, old_pos, max_dB
    
    watt=pow(10,rssi/10)/1000
    signalID=packet.namespace
    if signalID not in static_info:
        return
    if rssi>max_dB:
        max_dB=rssi
        print(max_dB)
    #print("<%s, %d> %s  @ %s" % (bt_addr, rssi, packet, additional_info))
    if signalID in signals:
        signals[signalID][0].append(watt)
        if len(signals[signalID][0])>10:
            signals[signalID][0].pop(0)
        signals[signalID][1]=time()
    else:
        signals[signalID]=[[watt],time(),True]
    if len(signals)>3 or time()-last_verification>.4:
        verification(signals)
        last_verification=time()
    if len(signals)==3:
        new_pos=CalcularPosicao3(signals,old_pos)
    elif len(signals)==2:
        new_pos=CalcularPosicao2(signals,old_pos)
    else:
        new_pos=static_info[list(signals.keys())[0]][1]
        if signals[signalID][2] and np.mean(signals[signalID][0])>-53:
            beep(sound=1)
            signals[signalID][2]=False
    if new_pos!=old_pos:
        #print(signals.keys())
        #print([signals[s][0] for s in signals])
        old_pos=new_pos
    print(new_pos)

    if not np.isnan(new_pos[0]):
        response = requests.post(
                url = base_url + 'position',
                headers = {'content-type':'application/json'},
                json = 
                    {
                        "user_id": user_id,
                        "coordinates": [new_pos[0], new_pos[1]]
                    }
                ,
                timeout=4
            )

    return new_pos
    #print("<%s, %d> %s  @ %s" % (bt_addr, rssi, packet, additional_info))


signals={}
max_dB=-100
tran_pow=pow(10,-66/10)/1000
Area=.8*pow(10,-2)
#static_info={"a"*20:[tran_pow,(40.623835,-8.657254,0)],"b"*20:[tran_pow,(40.623920,-8.657278,0)],"c"*20:[tran_pow,(40.623858,-8.657328,0)]}
static_info={"a"*20:[tran_pow,(40.623851,-8.656939,0)],"b"*20:[tran_pow,(40.623897,-8.656820,0)],"c"*20:[tran_pow,(40.624074,-8.656998,0)]}
# scan for all TLM frames of beacons in the namespace "12345678901234678901"
scanner = BeaconScanner(
    callback,
    packet_filter=[EddystoneTLMFrame, EddystoneUIDFrame],
    scan_parameters={"address_type": BluetoothAddressType.PUBLIC,"interval_ms":2.5}
)
last_verification=time()
old_pos=0
scanner.start()
input()
scanner.stop()



"""
dict_keys(['aaaaaaaaaaaaaaaaaaaa', 'cccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbb'])
[9.999999999999999e-11, 6.30957344480193e-11, 1.2589254117941662e-11]
(40.62419331974484, -8.656974261981887, 0)

dict_keys(['aaaaaaaaaaaaaaaaaaaa', 'cccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbb'])
[3.981071705534969e-11, 6.30957344480193e-11, 6.309573444801943e-12]
(40.624193319744826, -8.656974261981887, 0)

dict_keys(['aaaaaaaaaaaaaaaaaaaa', 'cccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbb'])
[3.981071705534969e-11, 3.981071705534969e-11, 1e-12]
(40.62419331974484, -8.656974261981887, 0)

dict_keys(['aaaaaaaaaaaaaaaaaaaa', 'cccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbb'])
[2.511886431509582e-11, 3.981071705534969e-11, 1e-12]
(40.624193319744826, -8.656974261981887, 0)

dict_keys(['aaaaaaaaaaaaaaaaaaaa', 'cccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbb'])
[2.511886431509582e-11, 1.0000000000000001e-11, 1.2589254117941663e-12]
(40.62419331974484, -8.656974261981887, 0)

dict_keys(['aaaaaaaaaaaaaaaaaaaa', 'cccccccccccccccccccc'])
[1.584893192461114e-10, 1.584893192461111e-12]
(40.624193319744826, -8.656974261981887, 0)

dict_keys(['aaaaaaaaaaaaaaaaaaaa', 'cccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbb'])
[1.2589254117941662e-10, 1.584893192461111e-12, 3.981071705534969e-12]
(40.62405899980835, -8.656900499811952, 0)
"""
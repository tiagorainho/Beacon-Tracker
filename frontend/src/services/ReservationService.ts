
import { current_reservation } from '../stores/current_reservation'
import { request } from "./ApiService";
import type { Reservation } from '../models/Reservation';
import { get } from 'svelte/store';


export async function perform_check_in(reservation_id:number, room_id:number, user_ids:number[]) {
    for(let i:number=0; i<user_ids.length; i++){
        if(user_ids[i] == null) {
            user_ids.splice(i,1)
        }
    }

    let completed_reservation: Reservation = await request(
        "/reservation",
        "PUT",
        {
            'reservation_id': reservation_id,
            'room_id': room_id,
            'user_ids': user_ids
        },
        {
            'Content-Type': 'application/json'
        }
    );
    current_reservation.set(completed_reservation['updated_reservation'])
    console.log(get(current_reservation))
  }
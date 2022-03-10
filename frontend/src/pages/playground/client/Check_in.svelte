
<script lang="ts">

    import { perform_check_in } from '../../../services/ReservationService';

    let available_rooms = [999999, 888888]
    let selected_room = available_rooms[0]
    let user_ids: number[] = [12, null]
    let reservation_id: number;

    function select_room(room) {
        selected_room = room;
    }

    function update_ids() {
        for(let i:number=0; i<user_ids.length; i++){
            if(user_ids[i] == null) {
                user_ids.splice(i,1)
            }
        }
        user_ids = [...user_ids, null]
    }

    function submit() {
        perform_check_in(reservation_id, selected_room, user_ids)
    }

</script>

<div>
    <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="reservation_id">
            Reservation ID
        </label>
        <input bind:value={reservation_id} class="shadow appearance-none border rounded w-1/2 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="reservation_id" type="number" placeholder="Reservation ID">
    </div>
    <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="room">
            Room
        </label>
        <div class="grid grid-cols-3 gap-2">
            {#each available_rooms as room}
                <div>
                    <img on:click={() => select_room(room)} src="https://cdn.pixabay.com/photo/2014/08/11/21/39/wall-416060__340.jpg" class="{selected_room == room? '': 'opacity-50'} rounded-sm cursor-pointer {selected_room == room? 'border-green-400 border-2': ''}"  alt="room"/>
                </div>
            {/each}
        </div>
    </div>
    <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="guests">
            Add Guest
        </label>
        {#each user_ids as id}
            <div class="py-1">
                <input on:change={update_ids} bind:value={id} class="shadow appearance-none border rounded w-1/2 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="number" placeholder="User ID">
            </div>
        {/each}
    </div>
    <button on:click={submit} class="bg-green-600 hover:bg-green-500 text-white font-bold py-2 px-4 rounded">
        Check in
    </button>
</div>
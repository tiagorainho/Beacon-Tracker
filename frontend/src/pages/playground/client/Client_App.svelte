

<script lang="ts">
    import CheckIn from './Check_in.svelte';
    import Notifications from './Notifications.svelte';
    import Activities from './Activities.svelte';
    import Location from './Location.svelte';
    import Requests from './Requests.svelte';

    import { current_reservation } from './../../../stores/current_reservation';

    let selected_tab = 'check_in';
    const selected_color = 'text-it-red bg-gray-300';

    function switch_tab(new_tab) {
        selected_tab = new_tab;
    }


</script>

<div>
    <div class="text-center mb-4 font-semibold">Client View</div>
    <div class="grid grid-cols-3 gap-x-3 gap-y-2 text-center mb-3">
        <div on:click={() => switch_tab('check_in')} class="bg-gray-200 hover:bg-gray-300 rounded-sm cursor-pointer {selected_tab == 'check_in' ? selected_color : ''}">Check in</div>
        {#if Object.keys($current_reservation).length != 0}
            <div on:click={() => switch_tab('activities')} class="bg-gray-200 hover:bg-gray-300 rounded-sm cursor-pointer {selected_tab == 'activities' ? selected_color : ''}">Activities</div>
            <div on:click={() => switch_tab('requests')} class="bg-gray-200 hover:bg-gray-300 rounded-sm cursor-pointer {selected_tab == 'requests' ? selected_color : ''}">Requests</div>
            <div on:click={() => switch_tab('location')} class="bg-gray-200 hover:bg-gray-300 rounded-sm cursor-pointer {selected_tab == 'location' ? selected_color : ''}">Family location</div>
            <div on:click={() => switch_tab('notifications')} class="bg-gray-200 hover:bg-gray-300 rounded-sm cursor-pointer {selected_tab == 'notifications' ? selected_color : ''}">Notifications</div>
        {/if}
    </div>
    <div class="w-full bg-white shadow-lg rounded px-8 pt-6 pb-8 mb-4">
        {#if selected_tab == 'check_in'}
            <CheckIn/>
        {:else if selected_tab == 'location'}
            <Location/>
        {:else if selected_tab == 'requests'}
            <Requests/>
        {:else if selected_tab == 'activities'}
            <Activities/>
        {:else if selected_tab == 'notifications'}
            <Notifications/>
        {/if}
    </div>

</div>
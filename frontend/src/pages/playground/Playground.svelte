
<script lang="ts">
    import ClientApp from "./client/Client_App.svelte";
    import HotelApp from "./hotel/Hotel_App.svelte";
</script>

<div class="flex gap-4">
    <div class="flex-1">
        <ClientApp/>
    </div>
    <div class="border border-gray-400"></div>
    <div class="flex-1">
        <HotelApp/>
    </div>
</div>

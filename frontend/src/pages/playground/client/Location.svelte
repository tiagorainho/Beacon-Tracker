<script lang="ts">
  import { onMount } from "svelte";
  import mapboxgl, { Map } from "mapbox-gl";
  import { update_positions } from './../../../services/LocationService'
  import type { Position } from "../../../models/Position";
  import { user_positions } from './../../../stores/user_positions';
  mapboxgl.accessToken = "pk.eyJ1IjoidGlhZ28xMjM0IiwiYSI6ImNsMGY2d2d2djBxNjEzY3BybW1zeGRzMWQifQ.PKKDDY8Su3BCttoWQ4B0uA"
  import {get} from 'svelte/store';
  import { poll } from "./../../../components/poll.ts";

  let map: Map | undefined;
  async function initMap() {
      map = new mapboxgl.Map({
          center: [-8.657796, 40.623716],
          zoom: 18,
          container: "map",
          style: "mapbox://styles/mapbox/light-v10?optimize=true",
      });
      map?.resize();
  }

  let markers = []

  onMount(() => {
      initMap();
      
      const marker1 = new mapboxgl.Marker()
      .setLngLat([-8.657796, 40.623716])
      .addTo(map);  
      markers = [marker1]

      poll(async function fetchData() {
        let positions: any = await update_positions([0])
        positions = JSON.parse(positions.user_positions)
        markers[0].setLngLat([positions.longitude, positions.latitude])
        .addTo(map);
      }, 1000);

  });

  
  $: {
    
  }


</script>

<div id="map" class="w-full h-96">


</div>
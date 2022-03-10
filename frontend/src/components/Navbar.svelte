<script lang="ts">
    import {location} from 'svelte-spa-router'
    const selected_color = 'text-it-red';
</script>


<nav class="flex flex-col flex-wrap justify-between font-mono bg-white h-12 px-4 md:px-32">

    <!-- left -->
    <ul class="my-auto">
        <li class="h-8 w-8">
            <img
                class="h-full w-full mx-auto"
                src="/logo.png"
                alt="logo" />
        </li>
    </ul>

    <!-- center -->

    <!-- FIX FIXED WIDTH WHEN IN SMALL SCREEN -->
    <ul class="flex items-center gap-10 flex-grow justify-end">
        <a href="/#" class="hover:no-underline {$location == '/' ? selected_color : ''}">Home</a>
        <a href="/#/playground" class="hover:no-underline {$location == '/playground' ? selected_color : ''}">Playground</a>
    </ul>

    <!-- right  -->
    {#if false}
    <ul class="flex items-center">
        <li class="pr-6">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-bell">
                <path
                    d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
        </li>
        <li class="h-10 w-10">
            <img
                class="h-full w-full rounded-full mx-auto"
                src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
                alt="profile woman" />
        </li>
    </ul>
    {/if}
</nav>
<div class="border-t border-gray-200"></div>

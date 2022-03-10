<script lang="ts">
	import Router from 'svelte-spa-router'
	import { routes } from './routes'
	import Navbar  from './components/Navbar.svelte'
	import Footer from './components/Footer.svelte'

</script>

<body class="flex flex-col min-h-screen font-body">
	<Navbar/>
	<div class="flex-grow min-w-full px-4 md:px-32 py-12 bg-light-gray text-gray-700 z-0">
    	<Router {routes}/>
	</div>	  
	<Footer/>
</body>
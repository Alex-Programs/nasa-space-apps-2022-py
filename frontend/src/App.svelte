<script>
    import Box from "./Box.svelte";

</script>
<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

#location {
    border: 2px solid rgba(255, 255, 255, 0.2);
    background-color: rgba(255, 255, 255, 0.2);
	width: 240px;
	transition: width 0.5s;
	transition-timing-function: cubic-bezier(.77,.31,.22,.66);
}
#location:focus {
	width: 100%;
}
</style>

<main class="bg-gradient-to-r from-teal-700 to-slate-900 p-8 h-screen">
	<Box>
		<div class="text-center">
			<input class="p-8 rounded-xl outline-none text-white text-xl opacity-80" type="text" name="location" id="location" placeholder="Location">
		</div>
	</Box>
</main>
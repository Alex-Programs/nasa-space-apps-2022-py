<script lang="ts">
	import Box from "./Box.svelte";
	let location = "";
	let results = [];

	async function autocomplete() {
		const res = await (await fetch(`/api/get_locations?query=${location}`)).json()
		if (!res.error) {
			results = res.data
		} else {
			results = []
		}
	}
</script>

<main class="bg-gradient-to-r from-teal-700 to-slate-900 h-screen p-16">
	<Box>
		<div class="text-center">
			<input
				class="glass p-8 rounded-xl outline-none text-white text-xl opacity-80"
				type="text"
				name="location"
				id="location"
				placeholder="Location"
				bind:value={location}
				on:input={autocomplete}
			/>
			{#each results as result}
				<button class="glass w-96 h-8 text-white">{result.name}</button>
				<br />
			{/each}
		</div>
	</Box>
</main>

<style>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

	.glass {
		border: 2px solid rgba(255, 255, 255, 0.2);
		border-top: none;
		border-bottom: none;
		background-color: rgba(255, 255, 255, 0.2);
	}

	#location {
		width: 240px;
		transition: width 0.5s;
		transition-timing-function: cubic-bezier(0.77, 0.31, 0.22, 0.66);
	}
	#location:focus, #location:not(:placeholder-shown) {
		width: 100%;
	}
</style>

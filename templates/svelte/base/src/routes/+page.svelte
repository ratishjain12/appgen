<script lang="ts">
	import { onMount } from 'svelte';

	let count = 0;

	onMount(() => {
		console.log('Svelte app mounted');
	});
</script>

<main>
	<div class="container">
		<h1>Svelte App</h1>
		<p>Ready to build!</p>
		<button on:click={() => count++}>
			Count: {count}
		</button>
	</div>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		margin: 0 auto;
	}

	.container {
		max-width: 800px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	button {
		font-size: 1.2em;
		padding: 0.5em 1em;
		background: #ff3e00;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	button:hover {
		background: #ff5722;
	}
</style> 
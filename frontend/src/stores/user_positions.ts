

import { writable } from 'svelte/store';

import type { Position } from '../models/Position';

function getLastPositions() {
	const { subscribe, update, set } = writable([] as Position[]);

	return {
		subscribe,
		update,
        set
	};
}

export const user_positions = getLastPositions();
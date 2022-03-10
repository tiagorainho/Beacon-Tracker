

import { writable } from 'svelte/store';

import type { User } from '../models/User';

function getUser() {
	const { subscribe, update, set } = writable({
		id:0,
		name:"Tiago"
	} as User);

	return {
		subscribe,
		update,
        set
	};
}

export const current_user = getUser();
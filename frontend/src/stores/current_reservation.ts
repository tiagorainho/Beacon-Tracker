

import { writable } from 'svelte/store';

import type { Reservation } from '../models/Reservation';


function getReservation() {
	const { subscribe, update, set } = writable({} as Reservation);

	return {
		subscribe,
		update,
        set
	};
}

export const current_reservation = getReservation();
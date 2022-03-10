
import type { Position } from '../models/Position';
import { user_positions } from '../stores/user_positions'
import { request } from "./ApiService";

export async function update_positions(user_ids: number[]) {

    let positions: Position[] = await request(
        "/user_positions?user_ids=0",
        "GET"
    );
    user_positions.set(positions)
    return positions
  }
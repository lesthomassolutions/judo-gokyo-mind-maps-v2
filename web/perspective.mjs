export const stanceKey='judo-mindmaps.stance.v1';
export const normalizeStance=value=>value==='left'?'left':'right';
export function readStance(storage){try{return normalizeStance(storage.getItem(stanceKey));}catch{return'right';}}
export function saveStance(storage,value){try{storage.setItem(stanceKey,normalizeStance(value));return true;}catch{return false;}}

import type { LimitOffsetResult } from "./shared.interface";

export interface Gallery extends LimitOffsetResult {
  results: Photo[];
}

export interface Photo {
  picture: string;
  thumbnail: string;
  content: string;
  id: number;
}

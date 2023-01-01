import type { LimitOffsetResult } from "./shared.interface";

export interface GuestBook extends LimitOffsetResult{
  results: GuestBookEntry[]; 
};

export interface GuestBookEntry {
  uuid: string;
  user_fullname: string;
  user: number;
  text: string;
  created_at: string;
};

export interface GuestBookError {
  text?: string[];
  non_field_errors?: string[];
}
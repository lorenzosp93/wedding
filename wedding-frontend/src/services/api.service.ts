import type { AxiosResponse } from "axios";
import type {
  Information,
  Message,
  Response,
  Subscription,
} from "@/models/listObjects.interface";
import type { Gallery } from "@/models/gallery.interface";
import type { User, Profile } from "@/models/auth.interface";
import type { GuestBook, GuestBookEntry } from "@/models/guestbook.interface";
import { HttpClient, HttpClientProtected } from "./http.client";
import { useAuthStore } from "@/stores";

const API_URL: string = import.meta.env.VITE_APP_BACKEND_URL;

class ApiClient extends HttpClient {
  constructor() {
    super(API_URL);
  }
}

class ApiClientProtected extends HttpClientProtected {
  constructor() {
    super(useAuthStore, API_URL);
  }
}

interface LimitOffsetOptions {
  overrideLink?: string;
  limit: number;
}

class ApiService extends ApiClient {
  async login(email: string): Promise<AxiosResponse> {
    return this.instance.post("/api/auth/email/", { email });
  }
  async registerUser(invitee: User): Promise<AxiosResponse> {
    return this.instance.post("/api/user/register-user/", invitee);
  }
  async getToken(email: string, token: string): Promise<AxiosResponse> {
    return this.instance.get(
      `/api/shared/magic-auth/?email=${email}&token=${token}&api=1`
    );
  }
}

class ApiServiceProtected extends ApiClientProtected {
  async setupPlusOne(invitee: User): Promise<AxiosResponse> {
    return this.instance.post("/api/user/setup-plus-one/", invitee);
  }

  async getUserSubscription(): Promise<AxiosResponse<Subscription[]>> {
    return this.instance.get("/api/user/subscription/");
  }

  async getUserProfile(): Promise<AxiosResponse<Profile[]>> {
    return this.instance.get("/api/user/profile/");
  }

  async getInboxContent(): Promise<AxiosResponse<Message[]>> {
    return this.instance.get("/api/inbox/message/");
  }

  async postInboxResponse(response: Response): Promise<AxiosResponse> {
    return this.instance.post("/api/inbox/response/", response);
  }

  async deleteInboxResponse(response_uuid: string): Promise<AxiosResponse> {
    return this.instance.delete(`/api/inbox/response/${response_uuid}/`);
  }

  async getInfoContent(): Promise<AxiosResponse<Information[]>> {
    return this.instance.get("/api/info/");
  }

  async getGalleryContent(
    options: LimitOffsetOptions
  ): Promise<AxiosResponse<Gallery>> {
    let overrideLink = options.overrideLink?.length
      ? options.overrideLink
      : null;
    return this.instance.get(
      overrideLink ?? `/api/photo/?limit=${options.limit}`
    );
  }

  async postUserSubscription(
    subscription: PushSubscriptionJSON | undefined
  ): Promise<AxiosResponse> {
    return this.instance.post("/api/user/subscription/", subscription);
  }

  async getGuestBookContent(
    options: LimitOffsetOptions
  ): Promise<AxiosResponse<GuestBook>> {
    let overrideLink = options.overrideLink?.length
      ? options.overrideLink
      : null;
    return this.instance.get(
      overrideLink ?? `/api/guestbook/entry/?limit=${options.limit}`
    );
  }

  async postGuestBookEntry(
    text: string
  ): Promise<AxiosResponse<GuestBookEntry>> {
    return this.instance.post("/api/guestbook/entry/", { text: text });
  }

  async deleteGuestBookContent(
    uuid: string
  ): Promise<AxiosResponse<GuestBookEntry[]>> {
    return this.instance.delete(`/api/guestbook/entry/${uuid}/`);
  }
}

export const apiService = new ApiServiceProtected();
export const apiServicePublic = new ApiService();

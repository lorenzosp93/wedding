import { describe, it, expect, vi, beforeEach } from "vitest";
import { createPinia, setActivePinia } from "pinia";
import { useNotificationStore } from "../notification.store";
import { apiService } from "@/services/api.service";
import type { Subscription } from "@/models/listObjects.interface";
import type { AxiosResponse } from "axios";

let testSubscription = {
  endpoint: "https://abc.com",
  keys: {
    p256dh: "abc123",
    auth: "abc",
  },
} as Subscription;

let axiosResponse = {
  data: [],
  status: 200,
  statusText: "fulfilled",
  headers: {},
  config: {},
} as AxiosResponse;

describe("Notification store test", () => {
  beforeEach(() => {
    const pinia = createPinia();
    setActivePinia(pinia);
  });

  it("Gets subscriptions", () => {
    let store = useNotificationStore();

    let res = vi.spyOn(apiService, "getUserSubscription").mockResolvedValue({
      ...axiosResponse,
      data: [testSubscription],
    });

    store.checkIsSubscribed().then(() => {
      expect(store.isSubscribed).toBe(true);
      expect(res).toBeCalled();
    });
  });
});

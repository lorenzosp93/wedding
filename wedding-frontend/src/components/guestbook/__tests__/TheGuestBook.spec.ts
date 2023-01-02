import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { VueWrapper, mount } from "@vue/test-utils";
import TheGuestBook from "../TheGuestBook.vue";
import { useGuestBookStore } from "@/stores";
import type { Store } from "pinia";
import { createTestingPinia } from "@pinia/testing";

describe("Guest book item tests", () => {
  let store: Store<"guestbook">;
  let wrapper: VueWrapper;

  beforeEach(() => {
    wrapper = mount(TheGuestBook, {
      global: {
        mocks: { $t: (t: string) => t },
        plugins: [
          createTestingPinia({
            initialState: {
              guestbook: {
                entries: [
                  {
                    uuid: "abc123",
                    user_fullname: "Some User",
                    user: 0,
                    text: "test text",
                    created_at: "2023-01-02T12:18:00Z",
                  },
                  {
                    uuid: "abc222",
                    user_fullname: "Some Other User",
                    user: 1,
                    text: "test other text",
                    created_at: "2023-01-01T12:19:00Z",
                  },
                ],
              },
            },
          }),
        ],
      },
    });
    store = useGuestBookStore();
  });
  it("Displays entry", async () => {
    let items = wrapper.findAllComponents({ name: "GuestBookItem" });
    expect(items).toHaveLength(2);
    expect(items[0].text()).toContain("test text");
    expect(items[1].text()).toContain("test other text");
  });
  it("Gets more content", async () => {
    let infinite = wrapper.findComponent({ name: "InfiniteScrolling" });
    infinite.vm.$emit("getMoreContent");
    expect((store as any).getEntries).toBeCalled();
  });
});

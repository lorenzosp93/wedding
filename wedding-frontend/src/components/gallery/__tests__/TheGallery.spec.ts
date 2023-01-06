import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { type VueWrapper, mount } from "@vue/test-utils";
import TheGallery from "../TheGallery.vue";
import { createTestingPinia } from "@pinia/testing";
import { useGalleryStore } from "@/stores";
import type { Store } from "pinia";

vi.useFakeTimers();

describe("Gallery tests", () => {
  let wrapper: VueWrapper;
  let store: Store;

  beforeEach(async () => {
    wrapper = mount(TheGallery, {
      attachTo: document.body,
      global: {
        plugins: [
          createTestingPinia({
            initialState: {
              gallery: {
                gallery: [
                  {
                    picture: "https://picture.url",
                    thumbnail: "https://thumb.url",
                    content: "testContent",
                    id: 0,
                  },
                  {
                    picture: "https://picture1.url",
                    thumbnail: "https://thumb1.url",
                    content: "testContent1",
                    id: 1,
                  },
                ],
              },
            },
          }),
        ],
        mocks: {
          $t: (t: string) => t,
        },
      },
    });
    store = useGalleryStore();
  });

  it("Creates columns", async () => {
    let cols = wrapper.findAll('[data-test="gallery-cols"]');

    expect(cols[0].element.childElementCount).toBe(1);
    expect(cols[1].element.childElementCount).toBe(1);
  });

  it("Activates photos", async () => {
    let item = wrapper.findComponent({ name: "ThumbnailItem" });
    await item.trigger("click");
    expect((wrapper.vm as any).activePhoto).toStrictEqual(item.vm.photo);
  });

  it("Gets more content", async () => {
    let infinite = wrapper.findComponent({ name: "InfiniteScrolling" });
    infinite.vm.$emit("getMoreContent");
    expect((store as any).getGalleryContent).toBeCalled();
  });
});

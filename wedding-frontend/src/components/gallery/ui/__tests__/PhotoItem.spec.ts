import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { mount } from "@vue/test-utils";
import PhotoItem from "../PhotoItem.vue";

describe("Photo item test", () => {
  it("Displays picture", async () => {
    let wrapper = mount(PhotoItem, {
      propsData: {
        activePhoto: {
          picture: "https://picture.link",
          thumbnail: "https://thumb.link",
          content: "testContent",
          id: 0,
        },
      },
    });

    let img = wrapper.find("img");
    expect(img.element.src).toBe("https://picture.link/");
    let outside = wrapper.find('[data-test="outside"]');
    await outside.trigger("click");
    expect(wrapper.emitted("closePhoto")).toBeTruthy();
  });
});

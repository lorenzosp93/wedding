import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { mount } from "@vue/test-utils";
import ThumbnailItem from "../ThumbnailItem.vue";

describe("Photo item test", () => {
  it("Displays picture", async () => {
    let wrapper = mount(ThumbnailItem, {
      propsData: {
        photo: {
          picture: "https://picture.link",
          thumbnail: "https://thumb.link",
          content: "testContent",
          id: 0,
        },
      },
    });

    let img = wrapper.find("img");
    expect(img.element.src).toBe("https://thumb.link/");
    let content = wrapper.find('[test-data="content"]');
    expect(content.text()).toContain("testContent");
  });
});

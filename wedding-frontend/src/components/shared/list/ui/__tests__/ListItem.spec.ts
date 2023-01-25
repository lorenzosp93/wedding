import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { VueWrapper, mount } from "@vue/test-utils";
import ListItem from "../ListItem.vue";
import type { IListObject } from "@/models/listObjects.interface";

describe("Test list items", () => {
  let wrapper: VueWrapper;
  beforeEach(() => {
    wrapper = mount(ListItem, {
      global: {
        mocks: { $t: (t: string) => t },
      },
      propsData: {
        obj: {
          subject: "testSubject",
          content: "testContent",
          thumbnail: "https://thumb.url",
        } as IListObject,
        active: false as boolean,
      },
    });
  });

  it("Displays list item", async () => {
    let thumb = wrapper.find("img");
    expect(thumb.element.src).toBe("https://thumb.url/");
    expect(wrapper.text()).toContain("testSubject");
    expect(wrapper.text()).toContain("testContent");
  });
});

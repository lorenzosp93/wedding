import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { type VueWrapper, mount } from "@vue/test-utils";
import DetailView from "../DetailView.vue";
import type { ComponentPublicInstance } from "vue";

describe("Detail view tests", () => {
  let wrapper: VueWrapper<ComponentPublicInstance<any>>;

  beforeEach(() => {
    wrapper = mount(DetailView, {
      global: {
        mocks: {
          $t: (t: string) => t,
        },
      },
      propsData: {
        activeObject: {
          uuid: "abc123",
          subject: "testSubject",
          content: "testContent",
          questions: [],
          picture: "https://picture.url",
        },
        active: 1,
        searchedListLength: 2,
      },
    });
  });

  it("Hides the detail view", async () => {
    await wrapper.get('[data-test="hide-icon"]').trigger("click");

    expect(wrapper.emitted().hideDetail).toHaveLength(1);
  });

  it("Changes the article", async () => {
    await wrapper.findAll("li")[0].trigger("click");
    await wrapper.findAll("li")[1].trigger("click");
    expect(wrapper.emitted().setActive[0]).toStrictEqual([0]);
    expect(wrapper.emitted().setActive[1]).toStrictEqual([2]);
  });

  it("Displays the article", () => {
    let img = wrapper.get("img");
    expect(img.element.src).toBe("https://picture.url/");
    expect(wrapper.text()).toContain("testSubject");
    expect(wrapper.text()).toContain("testContent");
  });
});

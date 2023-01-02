import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { VueWrapper, mount } from "@vue/test-utils";
import GuestBookItem from "../GuestBookItem.vue";
import type { ComponentPublicInstance } from "vue";

describe("Guest book item tests", () => {
  let wrapper: VueWrapper<ComponentPublicInstance<any>>;

  beforeEach(() => {
    wrapper = mount(GuestBookItem, {
      props: {
        entry: {
          uuid: "abc123",
          user_fullname: "Some User",
          user: 0,
          text: "test text",
          created_at: "2023-01-02T12:18:00Z",
        },
        own: true,
      },
    });
  });
  it("Displays entry", async () => {
    expect(wrapper.text()).toContain("Some User");
    expect(wrapper.text()).toContain("test text");
  });
  it("Doesn't show trash for other's", async () => {
    expect(wrapper.find("svg").exists()).toBeTruthy();
    await wrapper.setProps({ own: false });
    expect(wrapper.find("svg").exists()).toBeFalsy();
  });
  it("Deletes entry", async () => {
    let trash = wrapper.find("svg");
    trash.trigger("click");
    expect(wrapper.emitted().deleteEntry).toHaveLength(1);
  });
});

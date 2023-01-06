import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { VueWrapper, mount } from "@vue/test-utils";
import GuestBookForm from "../GuestBookForm.vue";
import type { ComponentPublicInstance } from "vue";

describe("Guest book item tests", () => {
  let wrapper: VueWrapper<ComponentPublicInstance<any>>;

  beforeEach(() => {
    wrapper = mount(GuestBookForm, {
      global: {
        mocks: { $t: (t: string) => t },
      },
      props: {
        submitError: undefined,
        submitLoading: false,
      },
    });
  });
  it("Submits text", async () => {
    let textArea = wrapper.get("textarea");
    let button = wrapper.get("button");
    await textArea.setValue("This is a test message.");
    await textArea.trigger("submit");
    await button.trigger("submit");
    expect(wrapper.emitted().submitEntry[0]).toStrictEqual([
      "This is a test message.",
    ]);
    expect(wrapper.emitted().submitEntry).toHaveLength(2);
    expect(wrapper.vm.text).toBe("");
  });
});

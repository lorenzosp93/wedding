// src/components/composables/useBreakpoint.spec.ts
import { mount } from "@vue/test-utils";
import { useBreakpoints } from "../breakpoints";
import { nextTick } from "vue";
import { describe, expect, it } from "vitest";

describe("useBreakpoint", () => {
  it("updates the breakpoint value when the window size changes", async () => {
    // Mock the window.outerWidth value
    Object.defineProperty(window, "outerWidth", {
      writable: true,
      configurable: true,
      value: 500,
    });

    const TestComponent = {
      template: `<div>{{ breakpoint }}</div>`,
      setup() {
        const breakpoint = useBreakpoints();
        return { breakpoint };
      },
    };

    const wrapper = mount(TestComponent);

    // Initially, the breakpoint should be 'xl' because the window width is less than 768
    expect(wrapper.text()).toBe("xl");

    // Change the window width to 800
    window.outerWidth = 800;
    window.dispatchEvent(new Event("resize"));

    // Wait for the next DOM update
    await nextTick();

    // Now, the breakpoint should be 'md' because the window width is between 768 and 1024
    expect(wrapper.text()).toBe("md");
  });
});

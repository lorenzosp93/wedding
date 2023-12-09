// src/components/composables/useTruncation.spec.ts
import { mount } from "@vue/test-utils";
import { truncate, removeHtml } from "../truncation";
import { describe, expect, it } from "vitest";

describe("truncate", () => {
  it("truncates a long string to the specified length", async () => {
    const TestComponent = {
      template: `<div>{{ truncatedText }}</div>`,
      setup() {
        const truncatedText = truncate("This is a very long string", 10);
        return { truncatedText };
      },
    };

    const wrapper = mount(TestComponent);

    // The truncated text should be 'This is a...'
    expect(wrapper.text()).toBe("This is a ...");
  });
});

describe("removeHtml", () => {
  it("removes HTML tags from a string", () => {
    const htmlString = "<p>Hello, <strong>world</strong>!</p>";
    const result = removeHtml(htmlString);
    expect(result).toBe("Hello, world!");
  });

  it("returns an empty string if the input is an empty string", () => {
    const result = removeHtml("");
    expect(result).toBe("");
  });

  it("returns the same string if there are no HTML tags", () => {
    const plainString = "Hello, world!";
    const result = removeHtml(plainString);
    expect(result).toBe(plainString);
  });
});

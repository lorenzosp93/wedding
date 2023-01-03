import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { VueWrapper, mount } from "@vue/test-utils";
import QuestionView from "../QuestionView.vue";
import type { ComponentPublicInstance } from "vue";

describe("Question view tests", () => {
  let wrapper: VueWrapper<ComponentPublicInstance<any>>;

  beforeEach(() => {
    wrapper = mount(QuestionView, {
      global: {
        mocks: {
          $t: (t: string) => t,
        },
      },
      propsData: {
        questions: [
          {
            uuid: "abc123",
            content: null,
            subject: "someQuestion?",
            options: [
              {
                uuid: "12345",
                content: "option1",
              },
              {
                uuid: "23456",
                content: "option2",
              },
              {
                uuid: "3456",
                content: "option3",
              },
            ],
            response: null,
            multi_select: true,
            free_text: true,
            mandatory: true,
          },
          {
            uuid: "abc234",
            content: null,
            subject: "someOtherQuestion?",
            options: [
              {
                uuid: "a5",
                content: "option4",
              },
              {
                uuid: "b6",
                content: "option5",
              },
            ],
            response: null,
            multi_select: false,
            free_text: true,
            mandatory: true,
          },
        ],
      },
    });
  });

  it("Submits responses", () => {});
});

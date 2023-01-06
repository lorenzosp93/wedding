import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { VueWrapper, mount } from "@vue/test-utils";
import QuestionView from "../QuestionView.vue";
import type { ComponentPublicInstance } from "vue";
import type { Response } from "@/models/listObjects.interface";

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
                uuid: "a12345",
                content: "option1",
              },
              {
                uuid: "a23456",
                content: "option2",
              },
              {
                uuid: "a3456",
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

  it("Submits responses", async () => {
    await wrapper.get("#a23456").trigger("input");
    await wrapper.get("#a3456").trigger("input");
    await wrapper.get("#b6").trigger("input");
    await wrapper.findAll("input[type=text]")[1].setValue("someText");
    await wrapper.get("button").trigger("click");

    let submit = wrapper.emitted().submitResponse[0] as Array<Response[]>;
    expect(submit[0]).toHaveLength(2);
    expect(submit[0][0].question).toBe("abc123");
    expect(submit[0][0].option).toStrictEqual(["a23456", "a3456"]);
    expect(submit[0][1].question).toBe("abc234");
    expect(submit[0][1].option).toStrictEqual(["b6"]);
    expect(submit[0][1].text).toBe("someText");
  });
});

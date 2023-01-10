import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { type VueWrapper, mount } from "@vue/test-utils";
import ListView from "../ListView.vue";
import type { ComponentPublicInstance } from "vue";

describe("Test list view", () => {
  let wrapper: VueWrapper<ComponentPublicInstance<any>>;

  beforeEach(() => {
    wrapper = mount(ListView, {
      global: {
        mocks: {
          $t: (t: string) => t,
          $router: {
            push: vi.fn(),
          },
          $route: {
            name: "testRoute",
            params: {
              active: 0,
            },
          },
        },
      },
      propsData: {
        objList: [
          {
            uuid: "abc123",
            subject: "testSubject",
            content: "testContent",
            questions: [],
            picture: "https://picture.url",
          },
          {
            uuid: "def456",
            subject: "testSubject1",
            content: "testContent1",
            questions: [],
            picture: "https://picture1.url",
          },
        ],
        loading: false,
      },
    });
  });

  it("Displays the list", async () => {
    expect(wrapper.vm.$router.push).toBeCalledWith({
      name: "testRoute",
      params: {
        active: "0",
      },
    });
    let li = wrapper.findAllComponents({ name: "ListItem" });
    expect(li).toHaveLength(2);
    await li[1].trigger("click");
    expect(wrapper.vm.$router.push).toBeCalledWith({
      name: "testRoute",
      params: {
        active: "1",
      },
    });
  });

  it("Searches the list", async () => {
    let search = wrapper.get("input");
    await search.setValue("1");
    expect(wrapper.findAllComponents({ name: "ListItem" })).toHaveLength(1);
  });
});

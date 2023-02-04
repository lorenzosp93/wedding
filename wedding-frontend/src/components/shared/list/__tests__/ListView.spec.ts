import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { type VueWrapper, mount } from "@vue/test-utils";
import ListView from "../ListView.vue";
import type { ComponentPublicInstance } from "vue";
import { createTestingPinia } from "@pinia/testing";

describe("Test list view", () => {
  let wrapper: VueWrapper<ComponentPublicInstance<any>>;

  beforeEach(() => {
    vi.mock("vue-router", async () => {
      const actual: typeof import("vue-router") = await vi.importActual(
        "vue-router"
      );
      return {
        ...actual,
        useRouter: vi.fn(() => ({
          push: vi.fn(),
        })),
        useRoute: vi.fn(() => ({
          name: "testRoute",
          params: {
            active: "test-slug",
          },
        })),
      };
    });
    wrapper = mount(ListView, {
      global: {
        mocks: {
          $t: (t: string) => t,
        },
        plugins: [createTestingPinia()],
      },
      propsData: {
        objList: [
          {
            uuid: "abc123",
            subject: "testSubject",
            content: "testContent",
            questions: [],
            picture: "https://picture.url",
            slug: "test-slug",
          },
          {
            uuid: "def456",
            subject: "testSubject1",
            content: "testContent1",
            questions: [],
            picture: "https://picture1.url",
            slug: "test-slug-1",
          },
        ],
        loading: false,
      },
    });
  });

  it("Displays the list", async () => {
    expect(wrapper.vm.router.push).toBeCalledWith({
      name: "testRoute",
      params: {
        active: "test-slug",
      },
    });
    let li = wrapper.findAllComponents({ name: "ListItem" });
    expect(li).toHaveLength(2);
    await li[1].trigger("click");
    expect(wrapper.vm.router.push).toBeCalledWith({
      name: "testRoute",
      params: {
        active: "test-slug-1",
      },
    });
  });

  it("Searches the list", async () => {
    let search = wrapper.get("input");
    await search.setValue("1");
    expect(wrapper.findAllComponents({ name: "ListItem" })).toHaveLength(1);
  });
});

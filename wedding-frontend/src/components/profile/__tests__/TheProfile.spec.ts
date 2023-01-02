import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { type VueWrapper, mount } from "@vue/test-utils";
import TheProfile from "../TheProfile.vue";
import type { ComponentPublicInstance } from "vue";
import { useAuthStore } from "@/stores";
import { createTestingPinia } from "@pinia/testing";
import type { Store } from "pinia";

describe("The Profile tests", () => {
  let wrapper: VueWrapper<ComponentPublicInstance<any>>;
  let store: Store<"auth">;

  beforeEach(() => {
    wrapper = mount(TheProfile, {
      global: {
        mocks: { $t: (t: string) => t },
        plugins: [
          createTestingPinia({
            initialState: {
              auth: {
                profile: {
                  id: 0,
                  user: {
                    first_name: "testName",
                    last_name: "testLastName",
                    email: "test@email.com",
                  },
                  type: "family",
                  parent: null,
                  childs: [],
                  language: "it",
                  plus: 1,
                },
              },
            },
          }),
        ],
      },
    });
    store = useAuthStore();
  });

  it("Tests profile data display", async () => {
    expect(wrapper.text()).toContain("testName");
    expect(wrapper.text()).toContain("testLastName");
    expect(wrapper.text()).toContain("test@email.com");
  });
  it("Tests profile logout", async () => {
    let logout = wrapper.find('[data-test="logout-button"]');
    logout.trigger("click");

    expect((store as any).logout).toBeCalled();
  });
  it("Tests plusOne button display", async () => {
    let plus = wrapper.find('[data-test="plusOne-button"]');
    expect(plus.exists()).toBeTruthy();
    store.$patch({ profile: { plus: 0 } });
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="plusOne-button"]').exists()).toBeFalsy();
  });
  it("Tests plusOne data display", async () => {
    store.$patch({
      profile: {
        childs: [
          {
            id: 1,
            user: {
              first_name: "testChildName",
              last_name: "testChildLastName",
              email: "test@childemail.com",
            },
            type: "family",
            parent: 0,
            childs: [],
            language: "it",
            plus: 0,
          },
          {
            id: 2,
            user: {
              first_name: "testChild2Name",
              last_name: "testChild2LastName",
              email: "test@child2email.com",
            },
            type: "family",
            parent: 0,
            childs: [],
            language: "it",
            plus: 0,
          },
        ],
      },
    });
    await wrapper.vm.$nextTick();
    let plusones = wrapper.find('[data-test="plusOne-table"]');
    expect(plusones.element.childElementCount).toBe(2);
    expect(plusones.text()).toContain("testChildName");
    expect(plusones.text()).toContain("testChild2LastName");
    expect(plusones.text()).toContain("test@childemail.com");
  });
});

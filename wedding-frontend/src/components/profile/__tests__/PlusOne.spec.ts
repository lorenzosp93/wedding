import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { type VueWrapper, mount } from "@vue/test-utils";
import PlusOne from "../PlusOne.vue";
import type { ComponentPublicInstance } from "vue";
import { createTestingPinia } from "@pinia/testing";
import { useAuthStore } from "@/stores";
import type { Store } from "pinia";
import i18n from "@/i18n";

describe("Plus one tests", () => {
  let wrapper: VueWrapper<ComponentPublicInstance<any>>;
  let store: Store<"auth">;

  beforeEach(() => {
    wrapper = mount(PlusOne, {
      global: {
        plugins: [createTestingPinia()],
        mocks: {
          $t: (t: string, obj: Record<string, unknown>) => {
            return i18n.global.t(t, "en", obj);
          },
        },
      },
    });
    store = useAuthStore();
  });

  it("Submits plus one user", () => {
    let firstName = wrapper.find("#first_name_input");
    let lastName = wrapper.find("#last_name_input");
    let email = wrapper.find("#email_input");
    firstName.setValue("someName");
    lastName.setValue("someLastName");
    email.setValue("some@email.com");

    let mockSetup = ((store as any).setupPlusOne as Mock).mockImplementation(
      async () => {}
    );
    email.trigger("submit");

    expect(mockSetup).toBeCalledWith({
      first_name: "someName",
      last_name: "someLastName",
      email: "some@email.com",
    });
  });

  it("Displays errors", async () => {
    store.$patch({
      registerError: {
        email: ["invalid email"],
        non_field_errors: ["other error"],
      },
    });
    await wrapper.vm.$nextTick();
    expect(wrapper.text()).toContain("invalid email");
    expect(wrapper.text()).toContain("other error");
  });
});

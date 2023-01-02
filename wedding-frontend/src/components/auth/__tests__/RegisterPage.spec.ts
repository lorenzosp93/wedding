import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { mount } from "@vue/test-utils";
import { createTestingPinia } from "@pinia/testing";
import RegisterPage from "../RegisterPage.vue";
import { useAuthStore } from "@/stores";

describe("Register page tests", () => {
  it("Registers a user", async () => {
    let wrapper = mount(RegisterPage, {
      global: {
        plugins: [createTestingPinia()],
        mocks: {
          $t: (t: string) => t,
        },
      },
    });
    let store = useAuthStore();

    let firstNameInput = wrapper.get("#first_name_input");
    await firstNameInput.setValue("testName");
    let lastNameInput = wrapper.get("#last_name_input");
    await lastNameInput.setValue("testLastName");
    let emailInput = wrapper.get("#email_input");
    await emailInput.setValue("test@email.com");
    await emailInput.trigger("submit");

    expect(store.register).toBeCalled();
    expect(store.register).toBeCalledWith({
      first_name: "testName",
      last_name: "testLastName",
      email: "test@email.com",
    });
  });
});

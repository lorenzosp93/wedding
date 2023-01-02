import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { mount } from "@vue/test-utils";
import LoginPage from "../LoginPage.vue";
import * as login from "@/services/login.service";

describe("Login page test", () => {
  it("Loads email from query", async () => {
    let wrapper = mount(LoginPage, {
      global: {
        mocks: {
          $t: (t: string) => t,
          $route: {
            query: { email: "test@email.com" },
          },
        },
      },
    });
    expect(wrapper.vm.email).toBe("test@email.com");
  });

  it("Calls login endpoint on email submit", async () => {
    let wrapper = mount(LoginPage, {
      global: {
        mocks: {
          $t: (t: string) => t,
          $route: () => {},
        },
      },
    });
    let emailInput = wrapper.find('[data-test="email-input"]');
    let formButton = wrapper.find('[data-test="form-button"]');
    await emailInput.setValue("test@email.com");
    expect(wrapper.vm.email).toBe("test@email.com");

    let mockLogin = vi.spyOn(login, "login").mockImplementation(async () => {});
    await emailInput.trigger("submit");
    await formButton.trigger("click");
    expect(mockLogin).toBeCalledWith("test@email.com");
    expect(mockLogin).toBeCalledTimes(2);
    // only show button if not loading
    expect(wrapper.find('[data-test="form-button"]')).toBeNull;
  });
});

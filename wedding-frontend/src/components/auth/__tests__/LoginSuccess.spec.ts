import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { mount } from "@vue/test-utils";
import LoginSuccess from "../LoginSuccess.vue";
import * as login from "@/services/login.service";

describe("Login success page test", async () => {
  it("Submits the OTP token", async () => {
    let wrapper = mount(LoginSuccess, {
      global: {
        mocks: {
          $t: (t: string) => t,
          $route: { query: { email: "test@email.com" } },
        },
      },
    });
    let input = wrapper.get('[data-test="token-input"]');
    await input.setValue(123456);
    let button = wrapper.get('[data-test="form-button"]');
    let mockGet = vi
      .spyOn(login, "getToken")
      .mockImplementation(async () => {});

    await input.trigger("submit");
    await button.trigger("click");

    expect(wrapper.vm.token).toBe("123456");
    expect(mockGet).toBeCalledTimes(2);
    expect(mockGet).toBeCalledWith("test@email.com", "123456");
  });
});

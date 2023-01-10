import { describe, it, vi, beforeEach, expect, type Mock } from "vitest";
import { type VueWrapper, mount } from "@vue/test-utils";
import LoginSuccess from "../LoginSuccess.vue";
import * as login from "@/services/login.service";

describe("Login success page test", async () => {
  let wrapper: VueWrapper<any>;
  beforeEach(() => {
    wrapper = mount(LoginSuccess, {
      global: {
        mocks: {
          $t: (t: string) => t,
          $route: { query: { email: "test@email.com" } },
        },
      },
    });
  });
  it("Submits the OTP token", async () => {
    let inputs = wrapper.findAll("input");
    await inputs[0].setValue("1");
    await inputs[1].setValue("2");
    await inputs[2].setValue("3");
    await inputs[3].setValue("4");
    await inputs[4].setValue("5");
    await inputs[5].setValue("6");
    let button = wrapper.get('[data-test="form-button"]');
    let mockGet = vi
      .spyOn(login, "getToken")
      .mockImplementation(async () => {});

    await inputs[0].trigger("submit");
    await button.trigger("click");

    expect(mockGet).toBeCalledTimes(2);
    expect(mockGet).toBeCalledWith("test@email.com", "123456");
  });
});

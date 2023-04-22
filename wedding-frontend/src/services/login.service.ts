import router from "@/router";
import type { AxiosResponse } from "axios";
import { apiServicePublic } from "./api.service";

export async function login(email: string) {
  return apiServicePublic
    .login(email)
    .then(() => {
      router.push({ name: "login-success", query: { email } });
    })
    .catch((error) => {
      console.log(error.message);
      if (error.response.data?.non_field_errors.length) {
        router.push({ name: "register", query: { email: email } });
      } else {
        throw error;
      }
    });
}

export async function getToken(
  email: string,
  token: string
): Promise<void | AxiosResponse<string>> {
  return apiServicePublic.getToken(email, token).then((response) => {
    let token = response.data.token;
    router.push({ name: "home", query: { token: token } });
  });
}

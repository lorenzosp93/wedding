import { useAuthStore } from "@/stores";

export default function authHeader() {
  const auth = useAuthStore();
  const isLoggedIn = !!auth?.token;

  if (isLoggedIn) {
    return {
      Authorization: `Token ${auth.token}`,
      'Accept-Language': auth?.profile?.language ?? 'en',
    };
  } else {
    return {};
  }
}

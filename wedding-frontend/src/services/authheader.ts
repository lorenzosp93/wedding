import { useAuthStore } from "@/stores";
import i18n from '@/i18n'

export default function authHeader() {
  const auth = useAuthStore();
  const isLoggedIn = !!auth?.token;

  let header = {
      'Accept-Language': auth?.profile?.language || i18n.global.locale.value,
  }

  if (isLoggedIn) {
    return {...header, ...{
      Authorization: `Token ${auth.token}`,
    }};
  } else {
  }
}

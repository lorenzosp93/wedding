import i18n from "@/i18n";
import { useAuthStore } from "@/stores";
import axios, {
  type InternalAxiosRequestConfig,
  type AxiosError,
  type AxiosInstance,
  type AxiosResponse,
} from "axios";

function getCookie(name: string): string {
  let cookieValue = "";
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export abstract class HttpClient {
  protected readonly instance: AxiosInstance;

  public constructor(baseURL: string) {
    this.instance = axios.create({
      baseURL,
    });
    this._initializeRequestInterceptor();
    this._initializeResponseInterceptor();
  }

  protected _initializeRequestInterceptor = () => {
    this.instance.interceptors.request.use(
      this._handleRequest,
      this._handleError
    );
  };

  protected _initializeResponseInterceptor = () => {
    this.instance.interceptors.response.use(
      this._handleResponse,
      this._handleError
    );
  };

  protected _handleRequest(config: InternalAxiosRequestConfig) {
    return {
      ...config,
      headers: {
        ...config.headers,
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept-Language": i18n.global.locale.value,
      },
    } as unknown as InternalAxiosRequestConfig;
  }

  protected _handleResponse(response: AxiosResponse) {
    return response;
  }

  protected _handleError(error: AxiosError) {
    console.log(error);
    return Promise.reject(error);
  }
}

export abstract class HttpClientProtected extends HttpClient {
  private readonly useAuth: typeof useAuthStore;
  public constructor(useAuth: typeof useAuthStore, baseURL: string) {
    super(baseURL);

    this.useAuth = useAuth;

    this._initializeResponseInterceptor();
    this._initializeRequestInterceptor();
  }

  protected _initializeRequestInterceptor = () => {
    this.instance.interceptors.request.use(
      this._handleRequest,
      this._handleError
    );
  };

  protected _initializeResposeInterceptor = () => {
    this.instance.interceptors.response.use(
      super._handleResponse,
      this._handleError
    );
  };

  protected _handleRequest = (config: InternalAxiosRequestConfig) => {
    config = super._handleRequest(config);

    let authStore = this.useAuth();

    return {
      ...config,
      headers: {
        ...config.headers,
        Authorization: `Token ${authStore.token}`,
        "Accept-Language": authStore?.profile?.language,
      },
    } as unknown as InternalAxiosRequestConfig;
  };

  protected _handleError = (error: AxiosError) => {
    console.log(error);
    if ([401, 403].includes(error?.response?.status ?? 0)) {
      let auth = this.useAuth();
      auth.logout();
    }
    return Promise.reject(error);
  };
}

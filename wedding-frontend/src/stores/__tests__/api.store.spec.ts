import { describe, it, expect, vi, beforeEach } from "vitest";
import { createPinia, setActivePinia } from "pinia";
import {
  useInfoStore,
  useInboxStore,
  useGalleryStore,
  useGuestBookStore,
  GALLERY_LIMIT,
  GUESTBOOK_LIMIT,
} from "../api.store";
import { apiService } from "@/services/api.service";
import type {
  Information,
  Message,
  Response,
} from "@/models/listObjects.interface";
import type { AxiosError, AxiosResponse } from "axios";
import type { Gallery } from "@/models/gallery.interface";
import type { GuestBook } from "@/models/guestbook.interface";

let axiosResponse = {
  data: [],
  status: 200,
  statusText: "fulfilled",
  headers: {},
  config: {},
} as AxiosResponse;

let testInfo = [
  {
    uuid: "abc123",
    content: "someTestContent",
    subject: "someTestSubject",
    type: "Events",
    picture: "https://link.to.pic",
    thumbnail: "https://link.to.thumb",
  },
  {
    uuid: "abc321",
    content: "someOtherTestContent",
    subject: "someOtherTestSubject",
    type: "Travel",
    picture: "https://link.to.pic",
    thumbnail: "https://link.to.thumb",
  },
] as Information[];

describe("Info store test", () => {
  beforeEach(() => {
    const pinia = createPinia();
    setActivePinia(pinia);
  });

  it("Gets Infos", () => {
    let store = useInfoStore();

    let mock = vi.spyOn(apiService, "getInfoContent").mockResolvedValue({
      ...axiosResponse,
      data: testInfo,
    });

    store.getInfo().then(() => {
      expect(mock).toBeCalled();
      expect(store.infos).toStrictEqual(testInfo);
      expect(store.activeType).toBe("events");
      expect(store.expiry).toBeGreaterThan(Date.now());
      expect(store.infoTypes).toStrictEqual(["events", "travel"]);
      expect(store.infosActiveType).toStrictEqual([testInfo[0]]);
    });
  });
});

let testInbox = [
  {
    uuid: "abc123",
    content: "someTestContent",
    subject: "someTestSubject",
    questions: [
      {
        uuid: "cba321",
        content: "someQuestionTestContent",
        subject: "someQuestionTestContent",
        options: [
          {
            uuid: "acb231",
            content: "someOptionContent",
          },
        ],
        response: null,
        multi_select: true,
        free_text: true,
        mandatory: true,
      },
    ],
  },
  {
    uuid: "abc321",
    content: "someOtherTestContent",
    subject: "someOtherTestSubject",
    questions: [],
  },
] as Message[];

let testResponse = {
  option: ["acb231"],
  text: "someTextResponse",
  question: "cba321",
} as Response;

describe("Inbox store test", () => {
  beforeEach(() => {
    const pinia = createPinia();
    setActivePinia(pinia);
  });

  it("Gets inbox", () => {
    let store = useInboxStore();

    let mock = vi.spyOn(apiService, "getInboxContent").mockResolvedValue({
      ...axiosResponse,
      data: testInbox,
    });

    store.getInbox().then(() => {
      expect(mock).toBeCalled();
      expect(store.inbox).toStrictEqual(testInbox);
      expect(store.expiry).toBeGreaterThan(Date.now());
    });
  });

  it("Submits responses", () => {
    let store = useInboxStore();

    let mockPost = vi
      .spyOn(apiService, "postInboxResponse")
      .mockResolvedValue(axiosResponse);
    let mockGet = vi.spyOn(store, "getInbox").mockResolvedValue();

    store
      .submitResponse([testResponse, testResponse], testInbox[0].uuid)
      .then(() => {
        expect(mockPost).toBeCalledTimes(2);
        expect(store.submitSuccess).toBe(true);
        expect(mockGet).toBeCalledWith({ force: true });
      });
  });

  it("Fails to submit responses", () => {
    let store = useInboxStore();

    vi.spyOn(apiService, "postInboxResponse").mockImplementation((_) => {
      return Promise.reject({ response: { data: "someError" } } as AxiosError);
    });
    vi.spyOn(store, "getInbox").mockResolvedValue();

    store.submitResponse([testResponse], testInbox[0].uuid).then(() => {
      expect(store.submitError).toStrictEqual([
        {
          q: testInbox[0].questions[0].uuid,
          e: "someError",
        },
      ]);
    });
  });

  it("Deletes responses", () => {
    let store = useInboxStore();

    let mockDelete = vi
      .spyOn(apiService, "deleteInboxResponse")
      .mockResolvedValue(axiosResponse);
    let mockGet = vi.spyOn(store, "getInbox").mockResolvedValue();

    store.deleteResponses(testInbox[0].uuid).then(() => {
      expect(mockDelete).toBeCalled();
      expect(store.deleteSuccess).toBe(true);
      expect(mockGet).toBeCalledWith({ force: true });
    });
  });

  it("Fails to delete responses", () => {
    let store = useInboxStore();

    vi.spyOn(apiService, "deleteInboxResponse").mockImplementation((_) => {
      return Promise.reject({ response: { data: "someError" } } as AxiosError);
    });
    vi.spyOn(store, "getInbox").mockResolvedValue();

    store.deleteResponses(testInbox[0].uuid).then(() => {
      expect(store.deleteError).toStrictEqual([
        {
          q: testInbox[0].questions[0].uuid,
          e: "someError",
        },
      ]);
    });
  });
});

let testGallery = {
  count: 2,
  next: "https://next.url",
  previous: "",
  results: [
    {
      picture: "https://picture1.url",
      thumbnail: "https://thumbnail1.url",
      content: "testContent",
      id: 0,
    },
    {
      picture: "https://picture2.url",
      thumbnail: "https://thumbnail2.url",
      content: "testContent",
      id: 1,
    },
  ],
} as Gallery;

describe("Gallery store test", () => {
  beforeEach(() => {
    const pinia = createPinia();
    setActivePinia(pinia);
  });

  it("Gets gallery content", () => {
    let store = useGalleryStore();

    let mock = vi
      .spyOn(apiService, "getGalleryContent")
      .mockResolvedValue({ ...axiosResponse, data: testGallery });

    store.getGalleryContent({ force: false }).then(() => {
      expect(store.next).toBe(testGallery.next);
      expect(store.gallery).toStrictEqual(testGallery.results);
      expect(store.expiry).toBeGreaterThan(Date.now());
      expect(mock).toBeCalledWith({ overrideLink: "", limit: GALLERY_LIMIT });
    });
  });

  it("Gets next gallery content", () => {
    let store = useGalleryStore();

    let mock = vi.spyOn(apiService, "getGalleryContent").mockResolvedValue({
      ...axiosResponse,
      data: testGallery,
    });

    store.getGalleryContent({ force: false }).then(() => {
      let expiry = store.expiry;
      store.getGalleryContent({ force: true }).then(() => {
        expect(mock).lastCalledWith({
          overrideLink: testGallery.next,
          limit: GALLERY_LIMIT,
        });
        expect(store.gallery).toStrictEqual([
          ...testGallery.results,
          ...testGallery.results,
        ]);
        expect(store.expiry).toBeGreaterThan(expiry);
      });
    });
  });
});

let testGuestbook = {
  count: 2,
  next: "https://next.url",
  previous: "",
  results: [
    {
      uuid: "abc123",
      user_fullname: "Some Name",
      user: 0,
      text: "someEntry",
      created_at: "2022-12-31T17:37:00.000Z",
    },
    {
      uuid: "abc234",
      user_fullname: "Some OtherName",
      user: 1,
      text: "someOtherEntry",
      created_at: "2022-12-31T16:37:00.000Z",
    },
  ],
} as GuestBook;

describe("Gallery store test", () => {
  beforeEach(() => {
    const pinia = createPinia();
    setActivePinia(pinia);
  });

  it("Gets entries content", () => {
    let store = useGuestBookStore();

    let mock = vi
      .spyOn(apiService, "getGuestBookContent")
      .mockResolvedValue({ ...axiosResponse, data: testGuestbook });

    store.getEntries({ force: false, limit: 8 }).then(() => {
      expect(mock).toBeCalledWith({ limit: 8, overrideLink: "" });
      expect(store.entries).toStrictEqual(testGuestbook.results);
      expect(store.next).toBe(testGuestbook.next);
    });
  });

  it("Submits entry", () => {
    let store = useGuestBookStore();

    let mockSubmit = vi
      .spyOn(apiService, "postGuestBookEntry")
      .mockResolvedValue(axiosResponse);
    let mockGet = vi.spyOn(store, "getEntries").mockResolvedValue();

    store.submitEntry(testGuestbook.results[0].text).then(() => {
      expect(mockSubmit).toBeCalledWith(testGuestbook.results[0].text);
      expect(mockGet).toBeCalledWith({ force: true });
    });
  });

  it("Submits entry", () => {
    let store = useGuestBookStore();

    let mockSubmit = vi
      .spyOn(apiService, "deleteGuestBookContent")
      .mockResolvedValue(axiosResponse);
    let mockGet = vi.spyOn(store, "getEntries").mockResolvedValue();

    store.deleteEntry(testGuestbook.results[0].uuid).then(() => {
      expect(mockSubmit).toBeCalledWith(testGuestbook.results[0].uuid);
      expect(mockGet).toBeCalledWith({ force: true });
    });
  });
});

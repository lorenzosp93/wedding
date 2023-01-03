import { defineComponent } from "vue";
import { marked } from "marked";

export default defineComponent({
  methods: {
    itemContent(content: string, chars: number = 40): string {
      return content
        ? this.removeHtml(marked.parse(this.truncate(content, chars)))
        : "";
    },
    removeHtml(value: string): string {
      const div = document.createElement("div");
      div.innerHTML = value;
      const text = div.textContent || div.innerText || "";
      return text;
    },
    truncate(value: string, length: number): string {
      if (!value) return "";
      value = value.toString();
      if (value.length > length) {
        return value.substring(0, length) + "...";
      } else {
        return value;
      }
    },
  },
});

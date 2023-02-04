import { marked } from "marked";

export function itemContent(content: string, chars: number = 40): string {
  return content ? removeHtml(marked.parse(truncate(content, chars))) : "";
}
export function removeHtml(value: string): string {
  const div = document.createElement("div");
  div.innerHTML = value;
  const text = div.textContent || div.innerText || "";
  return text;
}
export function truncate(value: string, length: number): string {
  if (!value) return "";
  value = value.toString();
  if (value.length > length) {
    return value.substring(0, length) + "...";
  } else {
    return value;
  }
}

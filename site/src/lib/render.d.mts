export interface Heading { depth: number; id: string; text: string }
export interface Chapter { slug: string; title: string; minutes: string | null; html: string; headings: Heading[] }
export interface Rendered {
  chapters: Chapter[];
  debats: { html: string; headings: Heading[] };
}
export function renderAll(): Rendered;

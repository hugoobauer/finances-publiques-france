export interface Heading { depth: number; id: string; text: string }
export interface Chapter { slug: string; title: string; minutes: string | null; html: string; headings: Heading[] }
export interface ChipEntry { key: string; kind: string; id: string; label: string; value: string | null; source?: string; url?: string | null }
export interface Answer {
  slug: string; title: string; phrase: string | null;
  sujets: string[]; leviers: string[]; debats: string[];
  montant: ChipEntry | null; html: string; headings: Heading[];
}
export interface Rendered {
  chapters: Chapter[];
  answers: Answer[];
  debats: { html: string; headings: Heading[] };
}
export function renderAll(): Rendered;

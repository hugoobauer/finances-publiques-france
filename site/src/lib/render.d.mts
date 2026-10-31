export interface Heading { depth: number; id: string; text: string }
export interface Chapter { slug: string; title: string; titleHtml: string; minutes: string | null; html: string; sourcesHtml: string; headings: Heading[] }
export interface ChipEntry { key: string; kind: string; id: string; label: string; value: string | null; source?: string | null; sourcePrefix?: string; url?: string | null }
export interface Section { id: string; titleHtml: string; title: string; html: string }
export interface Source { name: string; date: string | null; url: string | null; internal: boolean; formula?: string }
export interface Amount {
  id: string; origin: 'fig' | 'yard' | 'calc'; low: number; high: number; mid: number; unit: string; negative: boolean;
  text: string; textBare: string; label: string; year: string | null; source: Source;
}
export interface Answer {
  slug: string; title: string; phrase: string | null;
  sujets: { slug: string; label: string }[]; leviers: string[]; debats: string[];
  montant: ChipEntry | null; montantId: string | null; montantN: number | null; amount: Amount | null;
  brief: string | null; briefText: string; summary: string; sections: Section[];
  sourcesHtml: string; html: string; headings: Heading[];
}
export interface Rendered {
  chapters: Chapter[];
  answers: Answer[];
  debats: { html: string; titleHtml: string; title: string; sourcesHtml: string; headings: Heading[] };
}
export function renderAll(): Rendered;
export function plainText(html: string): string;

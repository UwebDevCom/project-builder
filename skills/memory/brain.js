// Brain — project knowledge base backed by a local JSON store
// All memory skill operations route through these functions.

import { readFileSync, writeFileSync, existsSync } from "fs";
import { join } from "path";

const STORE_PATH = join(process.cwd(), ".claude", "plugins", "project-builder", "memory.json");

function load() {
  if (!existsSync(STORE_PATH)) return {};
  return JSON.parse(readFileSync(STORE_PATH, "utf8"));
}

function persist(data) {
  writeFileSync(STORE_PATH, JSON.stringify(data, null, 2), "utf8");
}

export function save({ category, key, value, tags = [] }) {
  const db = load();
  const slug = `${category}:${key}`;
  db[slug] = { category, key, value, tags, updatedAt: new Date().toISOString() };
  persist(db);
  return db[slug];
}

export function get(key) {
  const db = load();
  // Support both "category:key" and bare "key" lookups
  if (db[key]) return db[key];
  const match = Object.values(db).find((e) => e.key === key);
  return match ?? null;
}

export function search(query) {
  const db = load();
  const q = query.toLowerCase();
  return Object.values(db)
    .filter((e) => e.value.toLowerCase().includes(q) || e.key.includes(q) || e.tags.some((t) => t.includes(q)))
    .sort((a, b) => new Date(b.updatedAt) - new Date(a.updatedAt));
}

export function list(category) {
  const db = load();
  const entries = Object.values(db);
  return category ? entries.filter((e) => e.category === category) : entries;
}

export function remove(key) {
  const db = load();
  const slug = Object.keys(db).find((k) => k === key || k.endsWith(`:${key}`));
  if (!slug) return false;
  delete db[slug];
  persist(db);
  return true;
}

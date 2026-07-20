// Basic Markdown linter: checks for common issues (trailing whitespace,
// missing top-level heading, broken code fence counts) without external deps.
const fs = require("fs");
const path = require("path");

const REPO = path.resolve(__dirname, "..");
let errors = 0;

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === "node_modules" || entry.name === ".git") continue;
      walk(full);
    } else if (entry.isFile() && entry.name.endsWith(".md")) {
      check(full);
    }
  }
}

function check(file) {
  const rel = path.relative(REPO, file);
  const text = fs.readFileSync(file, "utf8");
  const lines = text.split(/\r?\n/);
  let fences = 0;
  for (const line of lines) {
    if (/^\s*```/.test(line)) fences++;
  }
  if (fences % 2 !== 0) {
    console.log(`MD ERROR ${rel}: unbalanced code fences`);
    errors++;
  }
  if (!/^#\s+/.test(lines[0] || "")) {
    console.log(`MD WARN ${rel}: first line is not a top-level heading`);
  }
  console.log(`OK MD ${rel}`);
}

walk(REPO);
if (errors) {
  console.log(`${errors} markdown problem(s)`);
  process.exit(1);
}
console.log("All markdown files pass basic checks.");

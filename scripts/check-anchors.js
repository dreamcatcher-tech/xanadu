const fs = require('fs');
const path = require('path');

function slugify(text) {
  return text
    .trim()
    .toLowerCase()
    .replace(/[\s]+/g, '-')
    .replace(/[^a-z0-9-_]/g, '');
}

function getMarkdownFiles(dir) {
  let results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === 'node_modules') continue;
    const res = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(getMarkdownFiles(res));
    } else if (entry.isFile() && res.endsWith('.md')) {
      results.push(res);
    }
  }
  return results;
}

function checkFile(file) {
  const content = fs.readFileSync(file, 'utf8');
  const headingSlugRegex = /^#+\s*(.+)$/gm;
  const anchors = new Set();
  let match;
  while ((match = headingSlugRegex.exec(content))) {
    anchors.add(slugify(match[1]));
  }
  const linkRegex = /\[[^\]]*\]\(#([^\)]+)\)/g;
  const missing = [];
  while ((match = linkRegex.exec(content))) {
    const target = match[1];
    if (!anchors.has(target)) {
      missing.push(target);
    }
  }
  if (missing.length) {
    console.error(`Missing anchors in ${file}:`, missing.join(', '));
    return false;
  }
  return true;
}

let ok = true;
for (const file of getMarkdownFiles(process.cwd())) {
  ok &= checkFile(file);
}
if (!ok) {
  console.error('Anchor check failed');
  process.exit(1);
}

const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const preconnectTags = `  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n`;

let changed = 0;

for (const file of files) {
  const fullPath = path.join(dir, file);
  let content = fs.readFileSync(fullPath, 'utf8');

  // Skip if already has preconnect
  if (content.includes('rel="preconnect" href="https://fonts.googleapis.com"')) {
    continue;
  }

  // Find the first Google Fonts link (either <link or @import)
  const regex = /(<link[^>]*href="https:\/\/fonts\.googleapis\.com[^>]*>)/i;
  
  if (regex.test(content)) {
    content = content.replace(regex, preconnectTags + '$1');
    fs.writeFileSync(fullPath, content, 'utf8');
    console.log(`Updated ${file}`);
    changed++;
  }
}

console.log(`Done. Updated ${changed} files.`);

const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const imagesDir = path.join(__dirname, 'images');

async function processDirectory(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    
    if (stat.isDirectory()) {
      await processDirectory(fullPath);
    } else if (file.match(/\.(jpg|jpeg|png|webp)$/i)) {
      if (stat.size > 500 * 1024) { 
        console.log(`Compressing: ${file} (${(stat.size / 1024 / 1024).toFixed(2)} MB)`);
        const tempPath = fullPath + '.tmp.webp';
        try {
          const inputBuffer = fs.readFileSync(fullPath);
          await sharp(inputBuffer)
            .resize({ width: 1200, withoutEnlargement: true })
            .webp({ quality: 75 })
            .toFile(tempPath);
            
          fs.unlinkSync(fullPath);
          fs.renameSync(tempPath, fullPath);
          const newStat = fs.statSync(fullPath);
          console.log(`  -> Reduced to ${(newStat.size / 1024).toFixed(2)} KB`);
        } catch (err) {
          console.error(`  -> Failed to compress ${file}:`, err.message);
          if (fs.existsSync(tempPath)) fs.unlinkSync(tempPath);
        }
      }
    }
  }
}

async function run() {
  console.log('Starting compression...');
  await processDirectory(imagesDir);
  console.log('Compression complete!');
}

run();

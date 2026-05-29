import fs from 'fs';

const content = "---\ntitle: \"Физика и VR: Первые тесты\"\ndate: 2026-05-29\n---\nСегодня я настроил базовую систему коллизий. Жду приезда PSVR2, чтобы протестировать механики для The Last Light Fades в реальных условиях!";

fs.writeFileSync('./src/content/posts/update-01.md', content, 'utf8');
console.log('✅ Идеальный файл update-01.md успешно создан!');
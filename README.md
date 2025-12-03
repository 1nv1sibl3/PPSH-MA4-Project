# PPSH-MA4-Project
Fully static Art-Integration showcase for Maharashtra × Sikkim, built by Pawar Public School Hinjewadi Class 10A. The redesigned site now lives on GitHub Pages and highlights tourism, governance, cuisine, language, and more through a modern responsive layout.

## Live Site
- https://ppsh.any-platform.xyz/

## Highlights
- 🎨 Unified dark/glassmorphism UI across every page, including Hindi translations.
- 🗂️ Chapter hubs for Maharashtra (`/MH`) and Sikkim (`/SK`) plus their Hindi counterparts.
- 👥 Credits page featuring the 7-person team and their roles.
- 💬 FormSubmit-powered feedback form that emails submissions to `ctf.omhonrao@gmail.com`.
- 📱 Responsive navigation, hero cards, and alternating content sections optimized for mobile through desktop.

## Project Structure
```
.
├── index.html / compare.html / contact.html / credits.html / admin.html / login.html
├── MH/ & SK/          # English content chapters per topic
├── MH_hn/ & SK_hn/    # Hindi translations for each topic
├── static/
│   ├── css/
│   │   ├── global.css           # base layout + shared components
│   │   ├── credits.css          # credits page styling
│   │   ├── compare.css, contact.css, style.css
│   │   ├── chapter-shared.css   # shared styling for state chapters
│   │   └── MH/ & SK/            # thin wrappers importing shared styles
│   └── images/                  # logos, portraits, chapter illustrations
├── .github/workflows/main_ppsh.yml  # GitHub Pages deployment
└── README.md
```


## Credits
Seven classmates researched, translated, wrote, and designed every chapter, with Om Honrao leading website design. Full acknowledgements live at https://ppsh.any-platform.xyz/credits.

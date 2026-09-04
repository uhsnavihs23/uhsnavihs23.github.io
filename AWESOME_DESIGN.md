# 🎨 Awesome Design System Guidelines

Welcome to the **Shivanshu Sharma Portfolio Design System**. 

Developers and designers often maintain an `AWESOME_DESIGN.md` or `DESIGN.md` file in their repositories. It serves as a **Single Source of Truth (SSOT)** for all UI/UX decisions, ensuring that anyone contributing to the site (or you, when you build new projects 6 months from now) maintains 100% visual consistency.

By adopting this file, you guarantee that your site will never suffer from "frankenstein design" (where every page looks like it was built by a different person).

---

## 1. 🔤 Typography

We utilize a highly technical, developer-centric typographic scale.

- **Primary Font:** `Geist` (sans-serif)
- **Monospace Font:** `JetBrains Mono` (for code snippets and technical data)
- **Font Rendering:** We strictly enforce `-webkit-font-smoothing: antialiased;` to ensure text renders crisply on macOS and high-DPI displays.
- **Hierarchy:**
  - `h1`: `text-3xl` or `text-4xl`, `font-extrabold` (Reserved for main page titles)
  - `h2`: `text-2xl`, `font-bold` (Reserved for section headers)
  - `p`: `text-base` or `text-sm`, `text-secondary`, `leading-relaxed` (For high legibility)

## 2. 🎨 Color Palette (The "Zinc-Vercel" Hybrid)

We utilize a hybrid design approach. We take the structural geometry of Vercel (Geist) and combine it with the softer, eye-friendly "Zinc" color palette for Dark Mode.

### Light Mode Variables
- Background: `#f9fafb` (Soft Gray)
- Card Background: `#ffffff` (Pure White)
- Primary Text: `#0f172a` (Deep Slate)
- Secondary Text: `#475569` (Muted Slate)
- Borders: `#e5e7eb` (Subtle Gray)
- Accent: `#0070f3` (Vercel Blue)

### Dark Mode Variables
- Background: `#18181b` (Zinc 900)
- Card Background: `#27272a` (Zinc 800)
- Primary Text: `#f4f4f5` (Zinc 100)
- Secondary Text: `#d4d4d8` (Zinc 300)
- Borders: `#3f3f46` (Zinc 700)
- Accent: `#3291ff` (Vercel Light Blue)

> **⚠️ Rule:** Never hardcode `bg-white` or `text-black` directly unless absolutely necessary. Always rely on `bg-cardBg` and `text-primary` so the theme toggler can seamlessly invert the colors.

## 3. 📐 Geometry & Borders

We follow a structural, technical UI philosophy. We avoid overly "bubbly" or "Web3" aesthetics in favor of clean, professional lines.

- **Standard Containers:** Use `rounded-lg` or `rounded-xl`. 
- **Prohibited:** Do not use `rounded-2xl` or `rounded-3xl` for standard cards.
- **Exceptions:** `rounded-full` is exclusively reserved for Avatars, Badges/Pills, and Icon Buttons.

## 4. ☁️ Elevation & Shadows

Shadows should imply physical depth without looking artificial or heavy.

- **Standard Cards:** Use `shadow-sm` or `border border-borderColor`. 
- **Hover States:** Elevate slightly using `hover:-translate-y-1 hover:shadow-md transition-all duration-300`.
- **Prohibited:** Do not use massive drop shadows like `shadow-xl` or `shadow-2xl` on standard UI elements.
- **Prohibited:** Avoid colored background blur glows (`blur-3xl`, `opacity-10`) as they muddy the structural aesthetic.

## 5. 🌐 Retro Mode (IE6 Emulation)

Retro Mode is a strictly enforced, immersive feature that overrides modern aesthetics.
- **Theme Lock:** Dark Mode is explicitly **disabled** when Retro Mode is active. It operates exclusively in Light Mode to preserve the authentic Windows XP aesthetic.
- **Typography Override:** Forces `Tahoma` and `Microsoft Sans Serif`.
- **Components:** Injects fixed absolute Chrome overlays (`div#ie-chrome-top` and `div#ie-chrome-bottom`). 

## 6. 🛠 Component Rules

### Footers
Every `.html` page **must** conclude with the standard footer block containing:
1. Dynamic Copyright Year
2. GoatCounter Analytics Tracker (`<script data-goatcounter...`)
3. GitHub SVG Icon Link
4. LinkedIn SVG Icon Link

### Tables & Inputs
Always map `<input>`, `<select>`, and `<table>` backgrounds to `bg-cardBg` so they do not render as glaring white boxes when Dark Mode is enabled.


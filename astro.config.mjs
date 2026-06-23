// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

// GitHub Pages: published at https://zivl.github.io/msc-thesis-research/
// `site` + `base` make Astro emit correct asset/link URLs under the repo sub-path.
export default defineConfig({
  site: "https://zivl.github.io",
  base: "/msc-thesis-research",
  // LaTeX math (the thesis uses regression formulas) rendered with KaTeX.
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
  integrations: [
    starlight({
      title: "Android Malware Classification",
      description:
        "MSc thesis — A Machine-Learning permission-based classifier for detecting malicious Android applications. Ziv Levy.",
      // ----------------------------------------------------------------------
      // THREE SWAPPABLE THEMES — pick exactly ONE line below.
      // To switch theme: uncomment the desired file and comment the other two,
      // then restart `yarn dev` (or rebuild). theme-classic is the default.
      // ----------------------------------------------------------------------
      customCss: [
        "./src/styles/base.css", // shared: figures, captions, tables (always on)
        "./src/styles/theme-classic.css", // default: clean academic white, Georgia serif
        // "./src/styles/theme-modern.css",  // Inter sans-serif, navy accent, airy spacing
        // "./src/styles/theme-dark.css",    // dark background, high contrast for long reading
      ],
      // On-page table of contents depth (chapter pages use H2 subsections).
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      pagination: true,
      social: [
        {
          icon: "github",
          label: "GitHub",
          href: "https://github.com/zivl/msc-thesis-research",
        },
      ],
      sidebar: [
        { label: "Title & Abstract", link: "/" },
        { label: "1. Introduction", link: "/introduction/" },
        {
          label: "2. Android Security Model and Permissions",
          link: "/android-security-model/",
        },
        {
          label: "3. Android Permissions Statistics",
          link: "/android-permissions-statistics/",
        },
        { label: "4. Related Work", link: "/related-work/" },
        {
          label: "5. Machine-Learning Based Classifier",
          link: "/ml-classifier/",
        },
        {
          label: "6. The Algorithm Implementation",
          link: "/algorithm-implementation/",
        },
        {
          label: "7. Evaluation Methodology",
          link: "/evaluation-methodology/",
        },
        { label: "Results", link: "/results/" },
        {
          label: "8. Conclusions and Future Work",
          link: "/conclusions/",
        },
        {
          label: "Appendices",
          items: [
            { label: "Appendix A — Permissions Histograms", link: "/appendix-a/" },
            {
              label: "Appendix B — Selective Group of Android Permissions",
              link: "/appendix-b/",
            },
          ],
        },
      ],
    }),
  ],
});

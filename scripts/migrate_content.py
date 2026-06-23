#!/usr/bin/env python3
"""
Split the pandoc-extracted thesis Markdown (_full.md) into per-chapter Starlight
pages under src/content/docs/, transcribing the text VERBATIM.

Text-preserving transforms only:
  * drop the auto-generated Table of Contents and the Hebrew abstract (out of range)
  * drop pandoc empty-bold artifact lines ("**\\**")
  * unwrap RTL direction spans  <span dir="rtl">X</span> -> X   (X is just punctuation)
  * convert pandoc GFM math delimiters to KaTeX:  $`x`$ -> $x$  and  ```math блоки -> $$
  * replace the embedded image tags / insert the regenerated chart images at the
    exact caption positions, wrapped in semantic <figure>/<figcaption>
  * the chapter's own top heading becomes the page `title`; sub-headings are demoted H1->H2

No word, sentence, number or ordering of the thesis prose is changed.
"""
import re, os

SRC = "_full.md"
OUT = "src/content/docs"
IMG_BASE = "/msc-thesis-research/images"

# (filename, reconstructed title, first line, last line) — 1-indexed inclusive, on _full.md
PAGES = [
    ("index.md", "Is This Safe or Not?", 1, 52),
    ("introduction.md", "1. Introduction", 116, 154),
    ("android-security-model.md", "2. Android Security Model and Permissions", 155, 247),
    ("android-permissions-statistics.md", "3. Android Permissions Statistics", 248, 299),
    ("related-work.md", "4. Related Work", 300, 431),
    ("ml-classifier.md", "5. Machine-Learning Based Classifier – Our Proposal and Motivation", 432, 515),
    ("algorithm-implementation.md", "6. The Algorithm Implementation", 516, 662),
    ("evaluation-methodology.md", "7. Evaluation Methodology", 663, 753),
    ("results.md", "Results", 754, 948),
    ("conclusions.md", "8. Conclusions and Future Work", 949, 1082),
    ("appendix-a.md", "Appendix A – Permissions Histograms", 1083, 1329),
    ("appendix-b.md", "Appendix B - Selective Group of Android Permissions", 1330, 1484),
]

# embedded images:  source media file -> (output png, optional width, is_logo)
IMG_MAP = {
    "image1.emf": ("logo-idc.png", "260px", True),
    "image2.emf": ("figure1-android-infected-apps.png", None, False),
    "image3.emf": ("figure2-malware-ter.png", None, False),
    "image4.emf": ("figure3-permissions-approval-screen.png", "340px", False),
    "image5.png": ("figure8-ksl-syntax.png", "480px", False),
    "image6.png": ("figure9-classification-workflow.png", None, False),
}

# regenerated charts: exact caption text -> output png
CHART_MAP = {
    "Figure 4 - Distribution over Google Play Categories": "figure4-apps-distribution-categories.png",
    "Figure 5 - Histogram ratio of how many apps require a certain amount of permissions": "figure5-apps-permissions-histogram.png",
    "Figure 6 - Top 15 Most Required Permissions": "figure6-top15-permissions.png",
    "Figure 7 - Dangerous Permissions Usage": "figure7-dangerous-permissions.png",
    "Figure 7 - INTERNET Permission Usage": "figure7-internet-permission.png",
    "Figure 10 - Evaluation results over different levels of confidence threshold": "figure10-threshold-confidence.png",
    "Figure 11 - Comparison of different groups of modeled permissions": "figure11-permissions-modeling-comparison.png",
    "Figure 12 - Comparing Results of Different Solutions": "figure12-comparing-solutions.png",
}

CAPTION_RE = re.compile(r"^(Figure|Table)\s+\d+\b")
IMG_RE = re.compile(r'<img src="\./_pandoc_media/media/(image\d+\.\w+)"')


def html_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def figure_block(png, caption, width=None, logo=False):
    style = f' style="width:{width}"' if width else ""
    alt = html_escape(caption) if caption else "IDC Herzliya — Efi Arazi School of Computer Science"
    cls = ' class="logo"' if logo else ""
    out = ["", f"<figure{cls}>", f'<img src="{IMG_BASE}/{png}" alt="{alt}"{style} />']
    if caption:
        out.append(f"<figcaption>{html_escape(caption)}</figcaption>")
    out += ["</figure>", ""]
    return out


def next_nonblank(lines, i):
    j = i
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    return j


def process_figures(lines):
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        # pandoc <figure> block (image4 / Figure 3)
        if line.strip() == "<figure>":
            block = [line]
            j = i + 1
            while j < n and lines[j].strip() != "</figure>":
                block.append(lines[j]); j += 1
            if j < n:
                block.append(lines[j])
            btext = "\n".join(block)
            m = IMG_RE.search(btext)
            cap = re.search(r"<figcaption>.*?<p>(.*?)</p>.*?</figcaption>", btext, re.S)
            caption = cap.group(1).strip() if cap else ""
            if m and m.group(1) in IMG_MAP:
                png, width, logo = IMG_MAP[m.group(1)]
                out += figure_block(png, caption, width, logo)
            i = j + 1
            continue
        # inline <img ... /> tag
        m = IMG_RE.search(line)
        if m and m.group(1) in IMG_MAP:
            png, width, logo = IMG_MAP[m.group(1)]
            k = next_nonblank(lines, i + 1)
            caption = ""
            if not logo and k < n and CAPTION_RE.match(lines[k].strip()):
                caption = lines[k].strip()
                i = k  # consume caption line
            out += figure_block(png, caption, width, logo)
            i += 1
            continue
        # standalone chart caption -> insert regenerated chart image
        if line.strip() in CHART_MAP:
            cap = line.strip()
            out += figure_block(CHART_MAP[cap], cap)
            i += 1
            continue
        out.append(line)
        i += 1
    return out


def transform_text(text):
    # display math fences -> $$ ... $$
    text = re.sub(r"```\s*math\s*\n(.*?)\n```", lambda m: "$$\n" + m.group(1) + "\n$$", text, flags=re.S)
    # inline math  $`...`$  -> $...$   (drop empties)
    text = re.sub(r"\$`(.*?)`\$", lambda m: ("$" + m.group(1) + "$") if m.group(1).strip() else "", text)
    # unwrap RTL spans (content is punctuation only)
    text = re.sub(r'<span dir="rtl">(.*?)</span>', r"\1", text, flags=re.S)
    # drop pandoc empty-bold artifact lines
    text = re.sub(r"(?m)^\*\*\\\*\*\s*$\n?", "", text)
    return text


def build_page(lines, title, strip_first):
    lines = list(lines)
    if strip_first:
        if lines and lines[0].startswith("# "):
            lines = lines[1:]
        else:  # setext heading: drop through the '====' underline
            for k, l in enumerate(lines):
                if re.match(r"^=+\s*$", l):
                    lines = lines[k + 1:]
                    break
    # demote remaining ATX H1 -> H2
    lines = ["#" + l if l.startswith("# ") else l for l in lines]
    lines = process_figures(lines)
    body = transform_text("\n".join(lines)).strip("\n")
    fm = f'---\ntitle: "{title}"\n---\n\n'
    return fm + body + "\n"


def main():
    with open(SRC, encoding="utf-8") as f:
        all_lines = [l.rstrip("\n") for l in f]
    os.makedirs(OUT, exist_ok=True)
    for fname, title, a, b in PAGES:
        seg = all_lines[a - 1:b]
        strip_first = fname != "index.md"
        page = build_page(seg, title, strip_first)
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  wrote {fname:42s} ({b - a + 1} src lines)")


if __name__ == "__main__":
    main()

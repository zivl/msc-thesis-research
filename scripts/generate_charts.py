#!/usr/bin/env python3
"""
Regenerate the 8 native Microsoft Word charts embedded in the thesis .docx as PNG
figures, using the exact data values stored inside the document (word/charts/chartN.xml).

Pandoc cannot extract Word-native (DrawingML) charts, so these figures would otherwise be
lost. The numeric data, series names, titles and axis labels are read verbatim from the
chart XML; only the visual rendering is reproduced (styling differs from the original Word
charts, as agreed with the author).

Usage:
    .chartvenv/bin/python scripts/generate_charts.py <charts_xml_dir> <output_dir>
Outputs: chart1.png .. chart8.png
"""
import sys, os, glob
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

C = "{http://schemas.openxmlformats.org/drawingml/2006/chart}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
           "#8c564b", "#e377c2", "#17becf", "#bcbd22", "#7f7f7f"]


def cell_text(e):
    t = "".join(x.text or "" for x in e.iter(A + "t"))
    if t:
        return t
    return "".join((x.text or "") for x in e.iter(C + "v"))


def axis_titles(root):
    out = {}
    for tag in ("catAx", "valAx", "dateAx"):
        for ax in root.iter(C + tag):
            ti = ax.find(C + "title")
            if ti is not None:
                out.setdefault(tag, cell_text(ti))
    return out


def chart_type(root):
    for t in ("barChart", "lineChart", "scatterChart", "pieChart", "areaChart"):
        if root.find(f".//{C}{t}") is not None:
            return t
    return None


def chart_title(root):
    ch = root.find(f".//{C}chart")
    ti = ch.find(C + "title") if ch is not None else None
    return cell_text(ti) if ti is not None else ""


def series_data(root):
    out = []
    for ser in root.findall(f".//{C}ser"):
        tx = ser.find(C + "tx")
        name = cell_text(tx) if tx is not None else ""
        cat = ser.find(C + "cat")
        cats = ["".join(x.text or "" for x in p.iter(C + "v")) for p in cat.iter(C + "pt")] if cat is not None else []
        val = ser.find(C + "val") or ser.find(C + "yVal")
        vals = [float("".join(x.text or "" for x in p.iter(C + "v"))) for p in val.iter(C + "pt")] if val is not None else []
        xv = ser.find(C + "xVal")
        xs = [float("".join(x.text or "" for x in p.iter(C + "v"))) for p in xv.iter(C + "pt")] if xv is not None else []
        out.append(dict(name=name, cats=cats, vals=vals, xs=xs))
    return out


def style(ax, title, xlabel, ylabel, percent=False):
    ax.set_title(title, fontsize=13, fontweight="bold", pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=10)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=10)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if percent:
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0))


def render(path, out):
    root = ET.parse(path).getroot()
    n = int("".join(filter(str.isdigit, os.path.basename(path))))
    ctype = chart_type(root)
    title = chart_title(root)
    axt = axis_titles(root)
    sers = series_data(root)
    valname = axt.get("valAx", "")
    catname = axt.get("catAx", "")

    if n == 1:  # Figure 4 - Apps Distribution Over Categories (vertical bars, %)
        s = sers[0]
        fig, ax = plt.subplots(figsize=(11, 4.5))
        ax.bar(range(len(s["cats"])), s["vals"], color=PALETTE[0])
        ax.set_xticks(range(len(s["cats"])))
        ax.set_xticklabels(s["cats"], rotation=60, ha="right", fontsize=8)
        style(ax, title, "", valname, percent=True)

    elif n == 2:  # Figure 5 - Apps / Permissions Histogram (scatter)
        s = sers[0]
        fig, ax = plt.subplots(figsize=(9, 4.5))
        ax.scatter(s["xs"], s["vals"], color=PALETTE[0], s=28, zorder=3)
        ax.plot(s["xs"], s["vals"], color=PALETTE[0], alpha=0.35, zorder=2)
        # two valAx titles: x = amount of permissions, y = apps
        style(ax, title, "Amount of Permissions Required", "Apps", percent=True)

    elif n == 3:  # Figure 6 - Top 15 Most Required Permissions
        s = sers[0]
        fig, ax = plt.subplots(figsize=(10, 4.8))
        ax.bar(range(len(s["cats"])), s["vals"], color=PALETTE[0])
        ax.set_xticks(range(len(s["cats"])))
        ax.set_xticklabels(s["cats"], rotation=55, ha="right", fontsize=8)
        style(ax, title, "", valname or "Apps", percent=True)

    elif n == 4:  # Figure 7 - 10 of the Most Dangerous Permissions Usage
        s = sers[0]
        fig, ax = plt.subplots(figsize=(9, 4.8))
        ax.bar(range(len(s["cats"])), s["vals"], color=PALETTE[3])
        ax.set_xticks(range(len(s["cats"])))
        ax.set_xticklabels(s["cats"], rotation=55, ha="right", fontsize=8)
        style(ax, title, "", valname or "Apps", percent=True)

    elif n == 5:  # Figure 7 - INTERNET Permission Usage Over Categories (series=category)
        labels = [s["name"] for s in sers]
        vals = [s["vals"][0] for s in sers]
        fig, ax = plt.subplots(figsize=(10, 4.8))
        ax.bar(range(len(labels)), vals, color=PALETTE[0])
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=55, ha="right", fontsize=8)
        style(ax, title, "", valname or "Apps", percent=True)

    elif n == 6:  # Figure 10 - Threshold Over Different Confidence Levels (lines)
        cats = sers[0]["cats"]
        fig, ax = plt.subplots(figsize=(9, 5))
        for i, s in enumerate(sers):
            ax.plot(cats, s["vals"], marker="o", label=s["name"], color=PALETTE[i % len(PALETTE)])
        style(ax, title, catname or "Confidence Threshold Level", valname or "Evaluation Results")
        ax.legend(fontsize=8, ncol=2)

    elif n == 7:  # Figure 11 - Comparison of Permissions Modeling (grouped bars)
        cats = sers[0]["cats"]
        x = range(len(cats))
        w = 0.38
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar([i - w / 2 for i in x], sers[0]["vals"], w, label=sers[0]["name"], color=PALETTE[0])
        ax.bar([i + w / 2 for i in x], sers[1]["vals"], w, label=sers[1]["name"], color=PALETTE[1])
        ax.set_xticks(list(x))
        ax.set_xticklabels(cats, rotation=25, ha="right", fontsize=9)
        style(ax, title, catname, valname)
        ax.legend(fontsize=9)

    elif n == 8:  # Figure 12 - Comparing Results with Previous Solutions
        s = sers[0]
        colors = [PALETTE[7]] * len(s["cats"])
        colors[-2] = PALETTE[2]; colors[-1] = PALETTE[0]
        fig, ax = plt.subplots(figsize=(9.5, 5))
        ax.bar(range(len(s["cats"])), s["vals"], color=colors)
        ax.set_xticks(range(len(s["cats"])))
        ax.set_xticklabels(s["cats"], rotation=30, ha="right", fontsize=9)
        style(ax, title, "", valname or "Malicious Detection Rate", percent=True)
    else:
        return

    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  wrote {out}  ({ctype}, {len(sers)} series)")


def main():
    src, dst = sys.argv[1], sys.argv[2]
    os.makedirs(dst, exist_ok=True)
    for f in sorted(glob.glob(os.path.join(src, "chart*.xml")),
                    key=lambda x: int("".join(filter(str.isdigit, os.path.basename(x))))):
        n = int("".join(filter(str.isdigit, os.path.basename(f))))
        render(f, os.path.join(dst, f"chart{n}.png"))


if __name__ == "__main__":
    main()

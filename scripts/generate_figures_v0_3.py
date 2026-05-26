from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures_v0.3"
SOURCE = OUT / "source_data"

INITIAL_METRICS = (
    ROOT
    / "AUDIT_FMEA_public_artifact_v0.1"
    / "original_reproducibility_package"
    / "outputs"
    / "metrics_all_methods_recomputed.json"
)
STABILITY_JSON = ROOT / "experiment_extension" / "data" / "stability_summary.json"
RUN_MANIFEST = ROOT / "experiment_extension" / "data" / "run_manifest.csv"


mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "font.size": 7,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.linewidth": 0.7,
        "axes.labelsize": 7,
        "xtick.labelsize": 6.5,
        "ytick.labelsize": 6.5,
        "legend.frameon": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


COLORS = {
    "navy": "#2f4057",
    "blue": "#6f9fca",
    "teal": "#76b7a0",
    "amber": "#d8a657",
    "rose": "#c96f6f",
    "plum": "#9b7aa8",
    "ink": "#1f2933",
    "muted": "#6b7280",
    "line": "#d1d5db",
    "pale_blue": "#e8f0f8",
    "pale_teal": "#e8f5ef",
    "pale_amber": "#fbf2df",
    "pale_rose": "#f8e9e8",
    "pale_gray": "#f3f4f6",
}


def mm(value: float) -> float:
    return value / 25.4


def ensure_dirs() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    SOURCE.mkdir(parents=True, exist_ok=True)


def save_pub(fig: plt.Figure, stem: str) -> None:
    fig.savefig(OUT / f"{stem}.svg", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.png", dpi=600, bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.tiff", dpi=600, bbox_inches="tight")
    plt.close(fig)


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def load_initial_metrics() -> pd.DataFrame:
    data = json.loads(INITIAL_METRICS.read_text(encoding="utf-8"))["dfmea_metrics"]
    rows = []
    for method, values in data.items():
        rows.append({"method": method, **values})
    df = pd.DataFrame(rows)
    order = ["M1", "M2", "M3", "M4"]
    df["method"] = pd.Categorical(df["method"], categories=order, ordered=True)
    return df.sort_values("method").reset_index(drop=True)


def load_stability_summary() -> pd.DataFrame:
    data = json.loads(STABILITY_JSON.read_text(encoding="utf-8"))
    rows = []
    for run in data["runs"]:
        row = {
            "variant": run["variant"],
            "run_id": run["run_id"],
            "file": run["file"],
            **run["metrics"],
        }
        rows.append(row)
    df = pd.DataFrame(rows)
    order = ["M2", "M3", "M4_full", "M4_no_critic", "M4_no_integrity"]
    df["variant"] = pd.Categorical(df["variant"], categories=order, ordered=True)
    return df.sort_values(["variant", "run_id"]).reset_index(drop=True)


def rounded_box(ax, xy, width, height, text, fc, ec, fontsize=6.4, weight="normal"):
    box = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.018,rounding_size=0.025",
        linewidth=0.8,
        edgecolor=ec,
        facecolor=fc,
    )
    ax.add_patch(box)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight=weight,
        color=COLORS["ink"],
        wrap=True,
    )


def arrow(ax, start, end, color=COLORS["muted"], mutation_scale=8):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=mutation_scale,
            linewidth=0.8,
            color=color,
            shrinkA=4,
            shrinkB=4,
        )
    )


def make_figure_1() -> None:
    roles = [
        ("Function\nmapping", COLORS["pale_blue"]),
        ("Evidence\nattribution", COLORS["pale_teal"]),
        ("Failure-mode\ngeneration", COLORS["pale_amber"]),
        ("Cause-effect\nreasoning", COLORS["pale_amber"]),
        ("Risk\nscoring", COLORS["pale_blue"]),
        ("Critic\nreview", COLORS["pale_rose"]),
        ("Mitigation\nrefinement", COLORS["pale_teal"]),
        ("Integrity\nchecking", COLORS["pale_gray"]),
    ]
    artifacts = [
        ("Evidence pack", COLORS["pale_teal"]),
        ("Candidate rows", COLORS["pale_amber"]),
        ("Critic notes", COLORS["pale_rose"]),
        ("Final DFMEA", COLORS["pale_blue"]),
        ("Metric report", COLORS["pale_gray"]),
    ]
    source_payload = {
        "core_conclusion": (
            "AUDIT-FMEA treats LLM-assisted DFMEA as an auditable artifact "
            "pipeline with evidence, critic, and integrity gates."
        ),
        "roles": [r[0].replace("\n", " ") for r in roles],
        "artifacts": [a[0] for a in artifacts],
        "claim_boundary": [
            "structural traceability",
            "duplicate and invalid-row checks",
            "RPN arithmetic checks",
            "not expert validation",
            "not physical braking testing",
            "not safety certification",
        ],
    }
    write_json(SOURCE / "Figure_1_source_data.json", source_payload)

    fig = plt.figure(figsize=(mm(180), mm(116)))
    gs = fig.add_gridspec(3, 1, height_ratios=[1.1, 0.78, 0.56], hspace=0.34)

    ax = fig.add_subplot(gs[0])
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.0, 1.03, "a  Role-separated DFMEA workflow", fontsize=8, fontweight="bold")
    left, gap = 0.02, 0.012
    w = (0.96 - gap * 7) / 8
    y, h = 0.35, 0.36
    for idx, (label, fc) in enumerate(roles):
        x = left + idx * (w + gap)
        rounded_box(ax, (x, y), w, h, label, fc, COLORS["line"], fontsize=5.8, weight="bold" if idx in (1, 5, 7) else "normal")
        if idx < len(roles) - 1:
            arrow(ax, (x + w, y + h / 2), (x + w + gap, y + h / 2), mutation_scale=7)
    ax.text(
        0.02,
        0.12,
        "Each role emits an inspectable artifact before the final DFMEA table is accepted.",
        color=COLORS["muted"],
        fontsize=6.6,
    )

    ax = fig.add_subplot(gs[1])
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.0, 1.04, "b  Audit trail preserved for review", fontsize=8, fontweight="bold")
    left, gap = 0.08, 0.04
    w = (0.84 - gap * 4) / 5
    y, h = 0.38, 0.32
    for idx, (label, fc) in enumerate(artifacts):
        x = left + idx * (w + gap)
        rounded_box(ax, (x, y), w, h, label, fc, COLORS["line"], fontsize=6.1)
        if idx < len(artifacts) - 1:
            arrow(ax, (x + w, y + h / 2), (x + w + gap, y + h / 2), mutation_scale=7)
    ax.text(
        0.08,
        0.12,
        "Review points: source IDs, engineering-inference tags, critic comments, required-field checks, and RPN arithmetic.",
        color=COLORS["muted"],
        fontsize=6.4,
    )

    ax = fig.add_subplot(gs[2])
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.0, 1.04, "c  Evidence boundary", fontsize=8, fontweight="bold")
    rounded_box(ax, (0.05, 0.22), 0.39, 0.43, "Inside scope\nstructural auditability\ntraceability and consistency", COLORS["pale_teal"], COLORS["teal"], fontsize=6.5, weight="bold")
    rounded_box(ax, (0.56, 0.22), 0.39, 0.43, "Outside scope\nexpert correctness\nphysical braking safety", COLORS["pale_rose"], COLORS["rose"], fontsize=6.5, weight="bold")
    arrow(ax, (0.45, 0.43), (0.55, 0.43), color=COLORS["muted"], mutation_scale=8)

    save_pub(fig, "Figure_1_AUDIT_FMEA_workflow_v0.3")


def make_figure_2(initial: pd.DataFrame) -> None:
    cols = [
        "method",
        "row_count",
        "evidence_trace_rate",
        "high_risk_rpn_count",
        "high_severity_count",
        "invalid_rate",
        "duplicate_pair_count",
        "rpn_mismatch_count",
    ]
    initial[cols].to_csv(SOURCE / "Figure_2_source_data.csv", index=False)

    labels = ["M1", "M2", "M3", "M4"]
    x = np.arange(len(initial))
    method_colors = [COLORS["muted"], COLORS["blue"], COLORS["teal"], COLORS["navy"]]

    fig = plt.figure(figsize=(mm(180), mm(112)))
    gs = fig.add_gridspec(2, 3, height_ratios=[1, 1], wspace=0.35, hspace=0.48)

    panels = [
        ("a", "Row count", "Rows", "row_count", None),
        ("b", "Evidence traceability", "Rate", "evidence_trace_rate", (0, 1.08)),
        ("c", "High-severity items", "Count", "high_severity_count", None),
        ("d", "High-RPN items", "Count", "high_risk_rpn_count", None),
        ("e", "Invalid row rate", "Rate", "invalid_rate", (0, 0.12)),
        ("f", "Duplicate/RPN defects", "Count", None, (0, 1.2)),
    ]

    for idx, (letter, title, ylabel, metric, ylim) in enumerate(panels):
        ax = fig.add_subplot(gs[idx // 3, idx % 3])
        if metric:
            vals = initial[metric].to_numpy(dtype=float)
            ax.bar(x, vals, color=method_colors, width=0.62)
            for xi, val in zip(x, vals):
                label = f"{val:.1f}" if val % 1 else f"{int(val)}"
                if metric.endswith("rate"):
                    label = f"{val:.2f}"
                ax.text(xi, val + (0.03 if metric.endswith("rate") else max(vals.max() * 0.03, 0.15)), label, ha="center", va="bottom", fontsize=5.7)
        else:
            duplicate = initial["duplicate_pair_count"].to_numpy(dtype=float)
            mismatch = initial["rpn_mismatch_count"].to_numpy(dtype=float)
            ax.bar(x - 0.16, duplicate, color=COLORS["amber"], width=0.30, label="Duplicate pairs")
            ax.bar(x + 0.16, mismatch, color=COLORS["rose"], width=0.30, label="RPN mismatches")
            ax.legend(loc="upper left", fontsize=5.8, handlelength=1.0)
        ax.set_title(f"{letter}  {title}", loc="left", fontsize=8, fontweight="bold", pad=4)
        ax.set_ylabel(ylabel)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.grid(axis="y", color=COLORS["line"], linewidth=0.5, alpha=0.7)
        if ylim:
            ax.set_ylim(*ylim)

    fig.text(
        0.01,
        0.022,
        "M1, template-only; M2, single-LLM; M3, RAG-LLM; M4, AUDIT-FMEA.",
        fontsize=6.2,
        color=COLORS["muted"],
    )
    fig.text(
        0.01,
        0.002,
        "Metrics evaluate structural auditability and internal consistency only; they do not validate braking safety or expert correctness.",
        fontsize=6.2,
        color=COLORS["muted"],
    )

    save_pub(fig, "Figure_2_structural_metrics_v0.3")


def grouped_summary(stability: pd.DataFrame) -> pd.DataFrame:
    metrics = [
        "row_count",
        "invalid_rate",
        "duplicate_pair_count",
        "evidence_trace_rate",
        "high_risk_rpn_count",
        "high_severity_count",
        "rpn_mismatch_count",
    ]
    rows = []
    for variant, group in stability.groupby("variant", observed=False):
        if group.empty:
            continue
        row = {"variant": str(variant), "n": int(len(group))}
        for metric in metrics:
            values = group[metric].astype(float)
            row[f"{metric}_mean"] = float(values.mean())
            row[f"{metric}_sd"] = float(values.std(ddof=1)) if len(values) > 1 else 0.0
        rows.append(row)
    return pd.DataFrame(rows)


def make_figure_3(stability: pd.DataFrame) -> None:
    summary = grouped_summary(stability)
    summary.to_csv(SOURCE / "Figure_3_source_data.csv", index=False)

    variants = ["M2", "M3", "M4_full", "M4_no_critic", "M4_no_integrity"]
    display = ["M2\nSingle", "M3\nRAG", "M4\nFull", "No\ncritic", "No\nintegrity"]
    summary = summary.set_index("variant").loc[variants].reset_index()
    x = np.arange(len(summary))
    colors = [COLORS["blue"], COLORS["teal"], COLORS["navy"], COLORS["amber"], COLORS["rose"]]

    fig = plt.figure(figsize=(mm(180), mm(124)))
    gs = fig.add_gridspec(2, 3, height_ratios=[1.05, 0.88], wspace=0.42, hspace=0.52)

    ax = fig.add_subplot(gs[0, 0])
    vals = summary["invalid_rate_mean"].to_numpy()
    errs = summary["invalid_rate_sd"].fillna(0).to_numpy()
    ax.bar(x, vals, yerr=errs, color=colors, width=0.62, capsize=2, linewidth=0.6)
    ax.set_title("a  Invalid-row rate", loc="left", fontsize=8, fontweight="bold")
    ax.set_ylabel("Mean +/- sd")
    ax.set_xticks(x)
    ax.set_xticklabels(display)
    ax.set_ylim(0, max(0.14, float((vals + errs).max() * 1.25)))
    ax.grid(axis="y", color=COLORS["line"], linewidth=0.5, alpha=0.7)

    ax = fig.add_subplot(gs[0, 1])
    width = 0.28
    dup = summary["duplicate_pair_count_mean"].to_numpy()
    dup_e = summary["duplicate_pair_count_sd"].fillna(0).to_numpy()
    rpn = summary["rpn_mismatch_count_mean"].to_numpy()
    rpn_e = summary["rpn_mismatch_count_sd"].fillna(0).to_numpy()
    ax.bar(x - width / 2, dup, yerr=dup_e, color=COLORS["amber"], width=width, capsize=2, label="Duplicate pairs")
    ax.bar(x + width / 2, rpn, yerr=rpn_e, color=COLORS["rose"], width=width, capsize=2, label="RPN mismatches")
    ax.set_title("b  Defects exposed by ablation", loc="left", fontsize=8, fontweight="bold")
    ax.set_ylabel("Mean count")
    ax.set_xticks(x)
    ax.set_xticklabels(display)
    ax.set_ylim(0, 1.35)
    ax.grid(axis="y", color=COLORS["line"], linewidth=0.5, alpha=0.7)
    ax.legend(loc="upper left", fontsize=5.8)

    ax = fig.add_subplot(gs[0, 2])
    vals = summary["evidence_trace_rate_mean"].to_numpy()
    errs = summary["evidence_trace_rate_sd"].fillna(0).to_numpy()
    ax.bar(x, vals, yerr=errs, color=colors, width=0.62, capsize=2)
    ax.set_title("c  Evidence traceability", loc="left", fontsize=8, fontweight="bold")
    ax.set_ylabel("Mean rate")
    ax.set_xticks(x)
    ax.set_xticklabels(display)
    ax.set_ylim(0, 1.1)
    ax.grid(axis="y", color=COLORS["line"], linewidth=0.5, alpha=0.7)

    ax = fig.add_subplot(gs[1, :2])
    ax.set_title("d  High-consequence candidates remain inspectable", loc="left", fontsize=8, fontweight="bold")
    high_rpn = summary["high_risk_rpn_count_mean"].to_numpy()
    high_rpn_e = summary["high_risk_rpn_count_sd"].fillna(0).to_numpy()
    high_sev = summary["high_severity_count_mean"].to_numpy()
    high_sev_e = summary["high_severity_count_sd"].fillna(0).to_numpy()
    ax.bar(x - width / 2, high_rpn, yerr=high_rpn_e, color=COLORS["blue"], width=width, capsize=2, label="High RPN")
    ax.bar(x + width / 2, high_sev, yerr=high_sev_e, color=COLORS["plum"], width=width, capsize=2, label="High severity")
    ax.set_ylabel("Mean count")
    ax.set_xticks(x)
    ax.set_xticklabels(display)
    ax.grid(axis="y", color=COLORS["line"], linewidth=0.5, alpha=0.7)
    ax.legend(loc="upper left", fontsize=5.8)

    ax = fig.add_subplot(gs[1, 2])
    ax.set_axis_off()
    ax.set_title("e  Reviewer-facing interpretation", loc="left", fontsize=8, fontweight="bold")
    rounded_box(ax, (0.05, 0.60), 0.90, 0.25, "No critic\nvague or duplicate rows", COLORS["pale_amber"], COLORS["amber"], fontsize=6.4, weight="bold")
    rounded_box(ax, (0.05, 0.28), 0.90, 0.25, "No integrity\nmissing fields or RPN defects", COLORS["pale_rose"], COLORS["rose"], fontsize=6.4, weight="bold")
    ax.text(
        0.05,
        0.07,
        "Generated runs test structural failure modes under the documented workflow.",
        fontsize=6.0,
        color=COLORS["muted"],
        wrap=True,
    )

    save_pub(fig, "Figure_3_repeated_run_ablation_v0.3")


def make_manifest() -> None:
    rows = []
    for file in sorted(OUT.glob("Figure_*_v0.3.*")):
        rows.append({"file": file.name, "bytes": file.stat().st_size})
    with (OUT / "figure_file_manifest.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "bytes"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    ensure_dirs()
    initial = load_initial_metrics()
    stability = load_stability_summary()
    make_figure_1()
    make_figure_2(initial)
    make_figure_3(stability)
    make_manifest()
    print(f"Wrote figures to {OUT}")


if __name__ == "__main__":
    main()

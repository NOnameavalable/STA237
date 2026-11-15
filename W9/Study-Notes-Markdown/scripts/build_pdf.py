#!/usr/bin/env python3
"""
Convert STA237 Week 9 Study-Notes.md into a practice-edition PDF that matches
Markdown rendering cleanly (markdown-it-py + offline MathJax 3 SVG + Headless Chrome + PyMuPDF).

Each Problem Type (PT-01..PT-07) retains only its heading, Classification badge, and
Question prompt, placed on its own dedicated page with blank writing space below.
"""

import html
import os
import pathlib
import re
import subprocess
import tempfile
import markdown_it
import pymupdf

BASE_DIR = "/Users/stevenli/Documents/University of toronto/STA237/W9/Study-Notes-Markdown"
MD_PATH = os.path.join(BASE_DIR, "Study-Notes.md")
OUT_PDF = os.path.join(BASE_DIR, "Study-Notes.pdf")

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
MATHJAX_CANDIDATES = [
    "/Users/stevenli/.gemini/antigravity/brain/aafeee4d-d2de-49c1-9aba-cb7d6e8bfec7/scratch/tex-svg.js",
]

PT_SOL_REFS = {
    "01": "`SQ-03`, `SQ-05`",
    "02": "`SQ-04`",
    "03": "`MMSA #39(h–j)`, `SQ-06(a)`",
    "04": "`SQ-06(b)`, `MMSA #40–#42`",
    "05": "`SQ-07(a–e)`",
    "06": "`SQ-08`, `SQ-07` (CDF/PDF)",
    "07": "`MMSA #116`",
}


def find_mathjax():
    for path in MATHJAX_CANDIDATES:
        if os.path.exists(path):
            return path
    raise FileNotFoundError("Local MathJax tex-svg.js bundle not found.")


def github_slug(heading_text):
    """Generate GitHub/Markdown-compatible heading anchor IDs (keeps C-01 / PT-01 hyphens cleanly)."""
    s = re.sub(r"`([^`]+)`", r"\1", heading_text)
    s = s.replace("$", "")
    for cmd, rep in [
        (r"\Gamma", "gamma"),
        (r"\alpha", "alpha"),
        (r"\beta", "beta"),
        (r"\mu", "mu"),
        (r"\sigma", "sigma"),
        (r"\theta", "theta"),
        (r"\lambda", "lambda"),
        (r"\sim", "sim"),
        (r"\not", "not"),
    ]:
        s = s.replace(cmd, rep)
    s = s.replace("\\", "").lower()
    out = []
    for ch in s:
        if ch.isalnum() or ch in ("-", "_"):
            out.append(ch)
        elif ch == " ":
            out.append("-")
        elif ch in ("—", "–"):
            pass
    return "".join(out)


def render_md_fragment(md_text):
    """Render a Markdown fragment to HTML while protecting code spans and MathJax $ / $$ expressions."""
    code_store = {}

    def save_code(m):
        key = f"CODEBLOCKTOKEN{len(code_store)}ENDTOKEN"
        code_store[key] = m.group(0)
        return key

    text = re.sub(r"^[ \t]*```[a-zA-Z0-9_-]*\s*\n[\s\S]*?\n[ \t]*```", save_code, md_text, flags=re.MULTILINE)
    text = re.sub(r"`[^`\n]+`", save_code, text)

    math_store = {}

    def save_math(m):
        key = f"MATHBLOCKTOKEN{len(math_store)}ENDTOKEN"
        raw = m.group(0)
        # Convert table-safe \lvert / \rvert cleanly or keep MathJax standard delimiters
        raw = raw.replace(r"\|", "|")
        math_store[key] = raw
        return key

    text = re.sub(r"\$\$[\s\S]*?\$\$", save_math, text)
    text = re.sub(r"(?<!\\)\$(?!\s)[^\$\n]+?(?<!\s)(?<!\\)\$", save_math, text)
    text = re.sub(r"\((MATHBLOCKTOKEN\d+ENDTOKEN)\)", r'<span class="nowrap">(\1)</span>', text)

    for key, val in code_store.items():
        text = text.replace(key, val)

    md = markdown_it.MarkdownIt("commonmark").enable("table").enable("strikethrough")

    def render_heading_open(self, tokens, idx, options, env):
        token = tokens[idx]
        inline_tok = tokens[idx + 1] if idx + 1 < len(tokens) else None
        raw_content = inline_tok.content if inline_tok else ""
        for mk, mv in math_store.items():
            raw_content = raw_content.replace(mk, mv)
        slug = github_slug(raw_content)
        tag = token.tag
        cls_attr = ' class="concept-heading"' if tag == "h2" and raw_content.startswith("Concept C-") else ""
        return f'<{tag} id="{html.escape(slug)}"{cls_attr}>'

    md.renderer.rules["heading_open"] = render_heading_open.__get__(md.renderer, type(md.renderer))

    body_html = md.render(text)

    for key, raw_math in math_store.items():
        safe_math = html.escape(raw_math, quote=False)
        body_html = body_html.replace(key, safe_math)

    # Render GitHub-style [!TIP] / [!NOTE] blockquotes cleanly
    body_html = re.sub(
        r"<blockquote>\s*<p>\[!(TIP|NOTE|IMPORTANT|WARNING)\]\s*(?:<br\s*/?>|\n)?",
        lambda m: f'<blockquote class="callout callout-{m.group(1).lower()}"><p><span class="callout-badge">{m.group(1)}</span> ',
        body_html,
    )

    # Convert relative image paths to absolute file:// URIs and wrap figures with captions
    def fix_img_para(m):
        attrs_before = m.group(1)
        src = m.group(2)
        alt = m.group(3)
        attrs_after = m.group(4)
        if not src.startswith(("http://", "https://", "file://", "/")):
            abs_src = os.path.normpath(os.path.join(BASE_DIR, src))
            src = pathlib.Path(abs_src).as_uri()
        img_tag = f'<img {attrs_before}src="{src}" alt="{alt}"{attrs_after}>'
        caption_txt = re.sub(r"\^(\d+)", r"<sup>\1</sup>", alt)
        caption_html = f'<figcaption class="fig-caption">{caption_txt}</figcaption>' if alt.strip() else ""
        return f'<figure class="md-figure">{img_tag}{caption_html}</figure>'

    body_html = re.sub(
        r'<p><img ([^>]*)src="([^"]+)" alt="([^"]*)"([^>]*)></p>',
        fix_img_para,
        body_html,
    )

    def fix_other_img(m):
        src = m.group(1)
        if not src.startswith(("http://", "https://", "file://", "/")):
            abs_src = os.path.normpath(os.path.join(BASE_DIR, src))
            return f'src="{pathlib.Path(abs_src).as_uri()}"'
        return m.group(0)

    body_html = re.sub(r'src="([^"]+)"', fix_other_img, body_html)

    # Style external Answers-and-Practice links cleanly without broken local PDF targets
    body_html = re.sub(
        r'<a href="Answers-and-Practice\.md[^"]*">(.*?)</a>',
        r'<span class="answer-ref">\1</span>',
        body_html,
    )

    return body_html


def strip_trailing_hr(md_block):
    """Remove standalone trailing '---' horizontal rules before forced page breaks."""
    return re.sub(r"\n+---\s*$", "", md_block.rstrip()) + "\n"


def parse_pt_worksheet(pt_block_md, pt_num, pt_title_raw):
    """Strip PT explanations/hints and return pure Markdown + slug for one blank-space PT page."""
    m_cls = re.search(r"^- \*\*Classification:\*\*\s*(.+)$", pt_block_md, re.M)
    cls_text = m_cls.group(1).strip() if m_cls else "Core"

    m_rep = re.search(
        r"^(?:- )?\*\*Representative question \((.+?)\)\.\*\*\s*\n(.*?)(?=\n(?:- )?\*\*A complete answer|\Z)",
        pt_block_md,
        re.S | re.M,
    )
    if not m_rep:
        raise ValueError(f"Could not locate Representative question block for PT-{pt_num}")

    rep_source = m_rep.group(1).strip()
    rep_body_lines = m_rep.group(2).splitlines()

    cleaned_lines = []
    for line in rep_body_lines:
        if "Answers-and-Practice.md" in line and ("View" in line or "canonical worked solution" in line):
            continue
        cleaned_lines.append(line)

    rep_body_md = "\n".join(cleaned_lines).strip()
    pt_heading_md = f"### Problem Type PT-{pt_num}: {pt_title_raw}"
    pt_md = (
        f"{pt_heading_md}\n\n"
        f"**Classification:** {cls_text}\n\n"
        f"**Question** *({rep_source}):*\n\n{rep_body_md}\n"
    )

    slug = github_slug(f"Problem Type PT-{pt_num}: {pt_title_raw}")
    return pt_md, slug, cls_text, rep_source


def build_html_document(mathjax_path):
    with open(MD_PATH, "r", encoding="utf-8") as f:
        full_md = f.read()

    segments = re.split(r"(?=^### Problem Type PT-\d{2}: )", full_md, flags=re.M)

    html_chunks = []
    pt_index_rows = []
    current_owner = "C-01"

    for idx, seg in enumerate(segments):
        if idx == 0:
            c_matches = re.findall(r"^## Concept (C-\d{2}):", seg, re.M)
            if c_matches:
                current_owner = c_matches[-1]
            seg_clean = strip_trailing_hr(seg)
            html_chunks.append(render_md_fragment(seg_clean))
        else:
            m_next_c = re.search(r"(?m)^---\s*\n+## Concept (C-\d{2}):|^## Concept (C-\d{2}):", seg)
            if m_next_c:
                pt_raw = seg[: m_next_c.start()]
                tail_raw = seg[m_next_c.start() :]
                tail_raw = re.sub(r"^---\s*\n+", "", tail_raw)
            else:
                pt_raw = seg
                tail_raw = ""

            first_line = pt_raw.splitlines()[0].strip()
            m_hdr = re.match(r"^### Problem Type PT-(\d{2}):\s*(.+)$", first_line)
            if not m_hdr:
                raise ValueError(f"Malformed PT header: {first_line}")
            pt_num = m_hdr.group(1)
            pt_title_raw = m_hdr.group(2).strip()

            pt_md, pt_slug, cls_raw, rep_source = parse_pt_worksheet(pt_raw, pt_num, pt_title_raw)
            pt_inner_html = render_md_fragment(pt_md)

            html_chunks.append(
                f'<section class="pt-worksheet">\n'
                f'  <div class="pt-question-area">\n{pt_inner_html}\n  </div>\n'
                f'  <div class="pt-workspace-footer">Workspace for written solution. Worked solution is in <code>Answers-and-Practice.md</code>.</div>\n'
                f'</section>'
            )

            if "Supplementary" in cls_raw and "Core" in cls_raw:
                if "z_\\alpha" in cls_raw or "z_\u03b1" in cls_raw:
                    idx_cls = "Core / Supp ($z_\\alpha$)"
                elif "reversal" in cls_raw.lower():
                    idx_cls = "Core / Supp (reversal)"
                else:
                    idx_cls = "Core / Supp"
            elif "Supplementary" in cls_raw:
                idx_cls = "Supplementary"
            else:
                idx_cls = "Core"

            owner_slug_match = re.search(
                rf"^## Concept {current_owner}: (.+)$", full_md, re.M
            )
            owner_slug = (
                github_slug(f"Concept {current_owner}: {owner_slug_match.group(1)}")
                if owner_slug_match
                else f"concept-{current_owner.lower()}"
            )
            short_src = rep_source.replace("Paraphrase of ", "").strip()
            pt_index_rows.append((pt_num, pt_slug, current_owner, owner_slug, idx_cls, short_src, PT_SOL_REFS[pt_num]))

            if tail_raw.strip():
                c_matches = re.findall(r"^## Concept (C-\d{2}):", tail_raw, re.M)
                if c_matches:
                    current_owner = c_matches[-1]
                tail_clean = strip_trailing_hr(tail_raw)
                html_chunks.append(render_md_fragment(tail_clean))

    # Build final Problem Type Index section in Markdown
    index_lines = [
        "## Problem Type Index",
        "",
        "Each Problem Type worksheet page above contains only its representative question and blank writing space; full worked solutions live under Sections B and C of `Answers-and-Practice.md`.",
        "",
        "| PT | Owner | Classification | Representative Source | Worked Solution |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]
    for pt_num, pt_slug, owner, owner_slug, idx_cls, src, sol in pt_index_rows:
        index_lines.append(
            f"| [`PT-{pt_num}`](#{pt_slug}) | [`{owner}`](#{owner_slug}) | {idx_cls} | {src} | {sol} |"
        )
    index_lines.extend([
        "",
        "All Week 9 Problem Types (`PT-01`–`PT-07`) are established exclusively by the Week 9 lecture tasks (`W9/Week9-L0401-annotated.pdf`) and the MMSA Basic exercises (`#39(h–j)`, `#40–#42`, `#116`), using the **Course Distribution (CDF) Method** without the excluded Transformation Theorem.",
    ])
    index_html = f'<section class="pt-index-page">\n{render_md_fragment("\n".join(index_lines))}\n</section>'

    body_html = "\n".join(html_chunks) + "\n" + index_html
    mathjax_uri = pathlib.Path(mathjax_path).as_uri()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>STA237 Week 9 Study Notes — Practice Edition</title>
  <script>
  window.MathJax = {{
    tex: {{
      inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
      displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
      processEscapes: true
    }},
    svg: {{
      fontCache: 'global'
    }},
    options: {{
      renderActions: {{
        addMenu: []
      }}
    }},
    startup: {{
      pageReady: () => {{
        return MathJax.startup.defaultPageReady().then(() => {{
          document.body.setAttribute('data-mathjax-done', 'true');
        }});
      }}
    }}
  }};
  </script>
  <script id="MathJax-script" async src="{mathjax_uri}"></script>
  <style>
    @page {{
      size: A4;
      margin: 18mm 15mm 18mm 15mm;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 9.7pt;
      line-height: 1.52;
      color: #1f2937;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }}
    h1 {{
      font-size: 18pt;
      line-height: 1.25;
      border-bottom: 2.5px solid #2563eb;
      padding-bottom: 8px;
      margin-top: 0;
      margin-bottom: 13px;
      color: #1e3a8a;
      break-after: avoid;
      page-break-after: avoid;
    }}
    h2 {{
      font-size: 13.5pt;
      line-height: 1.3;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 4px;
      margin-top: 18px;
      margin-bottom: 9px;
      color: #1e40af;
      break-after: avoid;
      page-break-after: avoid;
    }}
    h2.concept-heading {{
      break-before: page;
      page-break-before: always;
      margin-top: 0;
    }}
    h3 {{
      font-size: 11.2pt;
      line-height: 1.35;
      margin-top: 15px;
      margin-bottom: 7px;
      color: #0f172a;
      break-after: avoid;
      page-break-after: avoid;
    }}
    p {{
      margin-top: 0;
      margin-bottom: 8.5px;
      text-align: left;
    }}
    a {{
      color: #1d4ed8;
      text-decoration: none;
    }}
    .answer-ref {{
      color: #0f766e;
      font-weight: 500;
    }}
    ul, ol {{
      margin-top: 0;
      margin-bottom: 8.5px;
      padding-left: 20px;
    }}
    li {{
      margin-bottom: 3.5px;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    li > ul, li > ol {{
      margin-top: 3px;
      margin-bottom: 3px;
    }}
    .mjx-chtml, mjx-container {{
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    mjx-container {{
      font-size: 90% !important;
    }}
    mjx-container[display="true"] {{
      font-size: 90% !important;
      margin: 7px 0 !important;
      max-width: 100%;
    }}
    mjx-container[display="true"] svg {{
      max-width: 100%;
      height: auto;
    }}
    .nowrap {{
      white-space: nowrap;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 10px 0 12px 0;
      font-size: 8.4pt;
      line-height: 1.4;
    }}
    thead {{
      display: table-header-group;
    }}
    tr {{
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 5px 7px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background-color: #f1f5f9;
      font-weight: 600;
      color: #0f172a;
    }}
    tr:nth-child(even) td {{
      background-color: #f8fafc;
    }}
    code {{
      font-family: "SFMono-Regular", Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      font-size: 8.2pt;
      background-color: #f1f5f9;
      color: #0f172a;
      padding: 1.5px 4px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
      white-space: nowrap;
    }}
    td code, th code, .pt-question-area code {{
      white-space: normal;
      overflow-wrap: break-word;
      font-size: 7.9pt;
      padding: 1px 3.5px;
    }}
    pre {{
      background-color: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 10px 12px;
      font-size: 8.2pt;
      line-height: 1.45;
      break-inside: avoid;
      page-break-inside: avoid;
      margin: 10px 0;
    }}
    pre code {{
      border: none;
      background: none;
      padding: 0;
      white-space: pre-wrap;
    }}
    blockquote {{
      border-left: 4px solid #3b82f6;
      border-radius: 0 6px 6px 0;
      margin: 10px 0;
      padding: 8px 12px;
      background-color: #eff6ff;
      color: #1e293b;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    blockquote.callout-tip {{
      border-left-color: #0d9488;
      background-color: #f0fdfa;
    }}
    .callout-badge {{
      display: inline-block;
      font-size: 7.3pt;
      font-weight: 700;
      letter-spacing: 0.04em;
      padding: 1px 6px;
      border-radius: 4px;
      background-color: #0d9488;
      color: #ffffff;
      vertical-align: middle;
      margin-right: 4px;
    }}
    blockquote p:last-child {{
      margin-bottom: 0;
    }}
    blockquote ul:last-child, blockquote ol:last-child {{
      margin-bottom: 0;
    }}
    hr {{
      border: none;
      border-top: 1px solid #e2e8f0;
      margin: 14px 0;
    }}
    figure.md-figure {{
      margin: 10px auto 12px auto;
      text-align: center;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    figure.md-figure img {{
      max-width: 94%;
      max-height: 66mm;
      width: auto;
      height: auto;
      display: block;
      margin: 0 auto;
      border-radius: 6px;
      border: 1px solid #e2e8f0;
      padding: 3px;
      background: #ffffff;
    }}
    figcaption.fig-caption {{
      margin-top: 5px;
      font-size: 8.2pt;
      font-style: italic;
      color: #475569;
    }}
    .pt-worksheet {{
      break-before: page;
      page-break-before: always;
      break-inside: avoid;
      page-break-inside: avoid;
      height: 258mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .pt-question-area h3 {{
      margin-top: 0;
      font-size: 12pt;
      color: #1e3a8a;
      border-bottom: 1.5px solid #cbd5e1;
      padding-bottom: 6px;
      margin-bottom: 10px;
    }}
    .pt-workspace-footer {{
      font-size: 8.2pt;
      font-style: italic;
      color: #64748b;
      border-top: 1px dashed #cbd5e1;
      padding-top: 6px;
    }}
    .pt-index-page {{
      break-before: page;
      page-break-before: always;
    }}
    .pt-index-page h2 {{
      margin-top: 0;
    }}
    .pt-index-page td:nth-child(1) code, .pt-index-page td:nth-child(2) code {{
      white-space: nowrap;
    }}
  </style>
</head>
<body>
{body_html}
</body>
</html>
"""


def compile_raw_pdf(html_path, raw_pdf_path, chrome_profile_dir, virtual_time=35000):
    cmd = [
        CHROME_BIN,
        "--headless",
        "--disable-gpu",
        f"--user-data-dir={chrome_profile_dir}",
        "--allow-file-access-from-files",
        "--run-all-compositor-stages-before-draw",
        f"--virtual-time-budget={virtual_time}",
        "--no-pdf-header-footer",
        f"--print-to-pdf={raw_pdf_path}",
        pathlib.Path(html_path).as_uri(),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if res.returncode != 0:
        raise RuntimeError(f"Headless Chrome failed ({res.returncode}):\n{res.stderr}")
    if not os.path.exists(raw_pdf_path):
        raise RuntimeError(f"Expected raw PDF not found at {raw_pdf_path}")


def postprocess_with_pymupdf(raw_pdf_path, final_pdf_path):
    doc = pymupdf.open(raw_pdf_path)
    total_pages = len(doc)

    header_left = "STA237: Probability (Week 9)"
    header_right = "Named Continuous Distributions & Transformations — Study Notes (Practice Edition)"
    footer_left = "STA237: Probability — University of Toronto"

    for idx, page in enumerate(doc):
        rect = page.rect
        page_num = idx + 1

        if page_num > 1:
            page.draw_line(
                pymupdf.Point(42, 36),
                pymupdf.Point(rect.width - 42, 36),
                color=(0.82, 0.85, 0.88),
                width=0.5,
            )
            page.insert_text(
                pymupdf.Point(42, 30),
                header_left,
                fontsize=7.5,
                fontname="helv",
                color=(0.45, 0.48, 0.52),
            )
            r_len = pymupdf.get_text_length(header_right, fontname="helv", fontsize=7.5)
            page.insert_text(
                pymupdf.Point(rect.width - 42 - r_len, 30),
                header_right,
                fontsize=7.5,
                fontname="helv",
                color=(0.45, 0.48, 0.52),
            )

        page.draw_line(
            pymupdf.Point(42, rect.height - 36),
            pymupdf.Point(rect.width - 42, rect.height - 36),
            color=(0.82, 0.85, 0.88),
            width=0.5,
        )
        page.insert_text(
            pymupdf.Point(42, rect.height - 24),
            footer_left,
            fontsize=7.5,
            fontname="helv",
            color=(0.45, 0.48, 0.52),
        )
        footer_right = f"Page {page_num} of {total_pages}"
        rf_len = pymupdf.get_text_length(footer_right, fontname="helv", fontsize=7.5)
        page.insert_text(
            pymupdf.Point(rect.width - 42 - rf_len, rect.height - 24),
            footer_right,
            fontsize=7.5,
            fontname="helv",
            color=(0.45, 0.48, 0.52),
        )

    doc.set_metadata({
        "title": "STA237 Week 9: Named Continuous Distributions & Transformations — Study Notes (Practice Edition)",
        "author": "Department of Statistical Sciences, University of Toronto",
        "subject": "STA237 Week 9 Study Notes: Gamma, Normal, R pgamma/pnorm/qnorm, Transformations via Course CDF Method",
        "keywords": "STA237, Gamma, Normal, Chebyshev, Transformations, Distribution Method, CDF Method",
        "creator": "markdown-it-py, MathJax 3 SVG, Headless Chrome & PyMuPDF",
    })
    doc.save(final_pdf_path, garbage=4, deflate=True)
    doc.close()
    print(f"Saved final PDF: {final_pdf_path} ({total_pages} pages, {os.path.getsize(final_pdf_path):,} bytes)")


def main():
    mathjax_path = find_mathjax()
    html_content = build_html_document(mathjax_path)

    with tempfile.TemporaryDirectory(prefix="w9_pdf_build_") as tmpdir:
        html_path = os.path.join(tmpdir, "Study-Notes.html")
        raw_pdf_path = os.path.join(tmpdir, "Study-Notes_raw.pdf")
        chrome_profile = os.path.join(tmpdir, "chrome_profile")

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        compile_raw_pdf(html_path, raw_pdf_path, chrome_profile)
        postprocess_with_pymupdf(raw_pdf_path, OUT_PDF)


if __name__ == "__main__":
    main()

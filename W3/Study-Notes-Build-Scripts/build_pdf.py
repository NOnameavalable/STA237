#!/usr/bin/env python3
"""
Convert STA237 Week 3 Study Notes and Answers & Practice Markdown files to publication-grade PDFs.
Uses markdown-it-py, MathJax 3 (offline local bundle), headless Google Chrome, and PyMuPDF post-processing.
"""

import os
import re
import html
import subprocess
import pathlib
import pymupdf

BASE_DIR = "/Users/stevenli/Documents/University of toronto/STA237/W3/Study-Notes-Markdown"
SCRATCH_DIR = os.environ.get("W3_PDF_SCRATCH_DIR", "/Users/stevenli/.gemini/antigravity/brain/b3221430-a13c-47f6-885c-e7725efbf4d7/scratch")
OUTPUT_DIR = os.environ.get("W3_PDF_OUTPUT_DIR", BASE_DIR)
MATHJAX_LOCAL = "/Users/stevenli/.gemini/antigravity/brain/aafeee4d-d2de-49c1-9aba-cb7d6e8bfec7/scratch/tex-svg.js"
CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

os.makedirs(SCRATCH_DIR, exist_ok=True)

def convert_md_to_html(md_path, html_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Step 1: Protect code blocks so math regexes do not match $ or { inside code
    code_store = {}
    def save_code(m):
        key = f"CODEBLOCKTOKEN{len(code_store)}END"
        code_store[key] = m.group(0)
        return key

    text_protected = re.sub(r"^[ \t]*```[a-zA-Z0-9_-]*\s*\n[\s\S]*?\n[ \t]*```", save_code, md_text, flags=re.MULTILINE)
    text_protected = re.sub(r"`[^`\n]+`", save_code, text_protected)

    # Step 2: Protect math blocks ($$ ... $$ and $ ... $) from CommonMark parser
    math_store = {}
    def save_math(m):
        key = f"MATHBLOCKTOKEN{len(math_store)}END"
        math_store[key] = m.group(0)
        return key

    # Display math ($$ ... $$)
    text_protected = re.sub(r"\$\$[\s\S]*?\$\$", save_math, text_protected)
    # Inline math ($ ... $)
    text_protected = re.sub(r"\$(?!\s)[^\$\n]+?(?<!\s)\$", save_math, text_protected)

    # Step 3: Restore code blocks before markdown parsing
    for key, val in code_store.items():
        text_protected = text_protected.replace(key, val)

    # Step 4: Convert GitHub alerts
    alert_pattern = re.compile(r">\s*\[!(NOTE|IMPORTANT|WARNING|CAUTION|TIP)\]\s*(.*?)(?=\n\n|\n[^\s>]|\Z)", re.DOTALL)
    def replace_alert(match):
        alert_type = match.group(1).lower()
        content = match.group(2).strip()
        content_lines = [re.sub(r"^>\s?", "", line) for line in content.split("\n")]
        clean_content = "\n".join(content_lines)
        return f'<div class="callout callout-{alert_type}"><div class="callout-title">{match.group(1)}</div>\n\n{clean_content}\n\n</div>'

    text_protected = alert_pattern.sub(replace_alert, text_protected)

    # Step 5: Render Markdown with markdown-it
    import markdown_it
    md = markdown_it.MarkdownIt("commonmark").enable("table").enable("strikethrough")
    body_html = md.render(text_protected)

    # Step 6: Restore math blocks into HTML with escaped XML entities
    for key, raw_math in math_store.items():
        safe_math = html.escape(raw_math, quote=False)
        body_html = body_html.replace(key, safe_math)

    # Step 7: Fix relative image paths to absolute file:// URLs
    def fix_img_src(match):
        src = match.group(1)
        if not src.startswith(("http://", "https://", "file://", "/")):
            abs_src = os.path.abspath(os.path.join(BASE_DIR, src))
            uri = pathlib.Path(abs_src).as_uri()
            return f'src="{uri}"'
        return match.group(0)

    body_html = re.sub(r'src="([^"]+)"', fix_img_src, body_html)

    # MathJax script URL: use local file URI
    mathjax_uri = pathlib.Path(MATHJAX_LOCAL).as_uri()
    doc_title = os.path.basename(md_path).replace(".md", "").replace("-", " ")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{doc_title}</title>
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
      margin: 18mm 16mm 18mm 16mm;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 10pt;
      line-height: 1.55;
      color: #1f2937;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }}
    h1 {{
      font-size: 19pt;
      border-bottom: 2.5px solid #2563eb;
      padding-bottom: 8px;
      margin-top: 0;
      margin-bottom: 16px;
      color: #1e3a8a;
      page-break-after: avoid;
      break-after: avoid;
    }}
    h2 {{
      font-size: 14pt;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 4px;
      margin-top: 24px;
      margin-bottom: 12px;
      color: #1e40af;
      page-break-after: avoid;
      break-after: avoid;
    }}
    h3 {{
      font-size: 12pt;
      margin-top: 18px;
      margin-bottom: 8px;
      color: #1f2937;
      page-break-after: avoid;
      break-after: avoid;
    }}
    h4 {{
      font-size: 10.5pt;
      margin-top: 14px;
      margin-bottom: 6px;
      color: #374151;
      page-break-after: avoid;
      break-after: avoid;
    }}
    p {{
      margin-top: 0;
      margin-bottom: 10px;
      text-align: justify;
    }}
    ul, ol {{
      margin-top: 0;
      margin-bottom: 10px;
      padding-left: 24px;
    }}
    li {{
      margin-bottom: 4px;
    }}
    ol > li {{
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    .mjx-chtml, mjx-container {{
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 14px 0;
      font-size: 9pt;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 6px 9px;
      text-align: left;
    }}
    th {{
      background-color: #f1f5f9;
      font-weight: 600;
      color: #0f172a;
    }}
    tr:nth-child(even) {{
      background-color: #f8fafc;
    }}
    code {{
      font-family: "SFMono-Regular", Menlo, Monaco, Consolas, monospace;
      font-size: 8.5pt;
      background-color: #f1f5f9;
      color: #0f172a;
      padding: 2px 4px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }}
    pre {{
      background-color: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 12px;
      overflow-x: auto;
      font-size: 8.5pt;
      line-height: 1.45;
      page-break-inside: avoid;
      break-inside: avoid;
      margin: 12px 0;
    }}
    pre code {{
      border: none;
      background: none;
      padding: 0;
    }}
    img {{
      max-width: 82%;
      height: auto;
      display: block;
      margin: 14px auto;
      border-radius: 6px;
      border: 1px solid #e2e8f0;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    hr {{
      border: none;
      border-top: 1px solid #e2e8f0;
      margin: 20px 0;
    }}
    blockquote {{
      border-left: 4px solid #94a3b8;
      margin: 12px 0;
      padding: 6px 14px;
      background-color: #f8fafc;
      color: #475569;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    .callout {{
      border-left: 4px solid #3b82f6;
      border-radius: 0 6px 6px 0;
      padding: 10px 14px;
      margin: 14px 0;
      background-color: #eff6ff;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    .callout-title {{
      font-weight: bold;
      font-size: 9.5pt;
      margin-bottom: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .callout-note {{
      border-left-color: #3b82f6;
      background-color: #eff6ff;
      color: #1e40af;
    }}
    .callout-note .callout-title {{ color: #1d4ed8; }}
    .callout-important {{
      border-left-color: #0d9488;
      background-color: #f0fdfa;
      color: #115e59;
    }}
    .callout-important .callout-title {{ color: #0f766e; }}
    .callout-warning {{
      border-left-color: #f59e0b;
      background-color: #fffbeb;
      color: #92400e;
    }}
    .callout-warning .callout-title {{ color: #b45309; }}
    .callout-caution {{
      border-left-color: #ef4444;
      background-color: #fef2f2;
      color: #991b1b;
    }}
    .callout-caution .callout-title {{ color: #b91c1c; }}
    .callout-tip {{
      border-left-color: #10b981;
      background-color: #ecfdf5;
      color: #065f46;
    }}
    .callout-tip .callout-title {{ color: #047857; }}
    /* MathJax defaults visually overpower the surrounding 10pt body text. */
    mjx-container {{ font-size: 90% !important; }}
    mjx-container[display="true"] {{ font-size: 90% !important; }}
  </style>
</head>
<body>
{body_html}
</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated HTML: {html_path} ({len(full_html):,} bytes)")

def compile_raw_pdf(html_path, pdf_path, virtual_time=35000):
    chrome_profile = os.path.join(SCRATCH_DIR, "chrome-profile-" + pathlib.Path(pdf_path).stem)
    cmd = [
        CHROME_BIN,
        "--headless",
        "--disable-gpu",
        f"--user-data-dir={chrome_profile}",
        "--allow-file-access-from-files",
        "--run-all-compositor-stages-before-draw",
        f"--virtual-time-budget={virtual_time}",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file://{html_path}"
    ]
    print(f"Compiling raw PDF: {pdf_path} (virtual budget: {virtual_time}ms)...")
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"Chrome timed out after 120 seconds while generating {pdf_path}") from exc
    if res.returncode != 0:
        print("Chrome error:", res.stderr)
        raise RuntimeError(f"Failed to generate PDF {pdf_path}")
    size = os.path.getsize(pdf_path)
    print(f"Raw PDF generated: {pdf_path} ({size:,} bytes)")

def repair_single_bullet_tail(doc):
    """Move the known lone Study Notes closing bullet when geometry has room."""
    if len(doc) < 2:
        return doc

    previous = doc[-2]
    last = doc[-1]
    width, height = last.rect.width, last.rect.height
    body_clip = pymupdf.Rect(40, 40, width - 40, height - 42)
    tail_text = re.sub(r"\s+", " ", last.get_text("text", clip=body_clip, sort=True)).strip()
    expected_start = "Misapplying conditional probability to PMFs:"
    if not tail_text.startswith(expected_start):
        return doc

    # The tail must consist of exactly one meaningful text block. This avoids
    # moving a page that contains another heading, paragraph, or list item.
    meaningful_blocks = []
    for block in last.get_text("dict")["blocks"]:
        if "lines" not in block or not pymupdf.Rect(block["bbox"]).intersects(body_clip):
            continue
        text = " ".join(span["text"] for line in block["lines"] for span in line["spans"])
        if re.search(r"[A-Za-z]{3,}", text):
            meaningful_blocks.append((block, text))
    if len(meaningful_blocks) != 1:
        return doc

    bullet_words = [
        word for word in last.get_text("words")
        if 45 <= word[1] and word[3] <= 85 and word[0] >= 45 and word[2] <= width - 45
    ]
    previous_words = [
        word for word in previous.get_text("words")
        if word[3] < previous.rect.height - 42
    ]
    if not bullet_words or not previous_words:
        return doc

    shift_up = 5.0
    gap = 3.0
    previous_bottom = max(word[3] for word in previous_words)
    bullet_top = min(word[1] for word in bullet_words)
    bullet_bottom = max(word[3] for word in bullet_words)
    source_clip = pymupdf.Rect(45, 45, width - 45, 85)
    target_top = previous_bottom - shift_up + gap - (bullet_top - source_clip.y0)
    target_bottom = target_top + source_clip.height
    placed_bullet_bottom = target_top + (bullet_bottom - source_clip.y0)
    footer_rule_y = height - 38

    # Keep a small gap above the existing footer rule and ensure the body shift
    # leaves room below the previous page's last line.
    if previous_bottom - shift_up < 42 or placed_bullet_bottom > footer_rule_y - 7:
        return doc
    if target_top < 0 or target_bottom > height:
        return doc

    repaired = pymupdf.open()
    repaired.insert_pdf(doc, from_page=0, to_page=len(doc) - 3)
    page = repaired.new_page(width=width, height=height)

    # Preserve source vectors and selectable text while shifting the prior body
    # up by five points. Headers and footers are added afterward as usual.
    body_source = pymupdf.Rect(0, 0, width, height - 42)
    page.show_pdf_page(
        pymupdf.Rect(0, -shift_up, width, height - 42 - shift_up),
        doc, len(doc) - 2, clip=body_source, keep_proportion=False
    )
    page.show_pdf_page(
        pymupdf.Rect(source_clip.x0, target_top, source_clip.x1, target_bottom),
        doc, len(doc) - 1, clip=source_clip, keep_proportion=False
    )

    # Retain links from the shifted page body.
    for link in previous.get_links():
        link["from"] = pymupdf.Rect(
            link["from"].x0, link["from"].y0 - shift_up,
            link["from"].x1, link["from"].y1 - shift_up
        )
        page.insert_link(link)

    repaired.set_metadata(doc.metadata)
    repaired.set_toc(doc.get_toc())
    print("Repaired single-bullet final page; the closing bullet now fits on the prior page.")
    return repaired

def postprocess_with_pymupdf(raw_pdf_path, final_pdf_path, header_left, header_right, metadata):
    source_doc = pymupdf.open(raw_pdf_path)
    doc = repair_single_bullet_tail(source_doc)
    if doc is not source_doc:
        source_doc.close()
    total_pages = len(doc)
    print(f"Postprocessing {final_pdf_path} ({total_pages} pages) with PyMuPDF...")

    for idx, page in enumerate(doc):
        rect = page.rect
        page_num = idx + 1

        # Running Header on pages 2..N
        if page_num > 1:
            # Thin top rule
            page.draw_line(
                pymupdf.Point(45, 38),
                pymupdf.Point(rect.width - 45, 38),
                color=(0.82, 0.85, 0.88),
                width=0.5
            )
            # Left header
            page.insert_text(
                pymupdf.Point(45, 32),
                header_left,
                fontsize=7.5,
                fontname="helv",
                color=(0.45, 0.48, 0.52)
            )
            # Right header
            right_len = pymupdf.get_text_length(header_right, fontname="helv", fontsize=7.5)
            page.insert_text(
                pymupdf.Point(rect.width - 45 - right_len, 32),
                header_right,
                fontsize=7.5,
                fontname="helv",
                color=(0.45, 0.48, 0.52)
            )

        # Running Footer on all pages
        page.draw_line(
            pymupdf.Point(45, rect.height - 38),
            pymupdf.Point(rect.width - 45, rect.height - 38),
            color=(0.82, 0.85, 0.88),
            width=0.5
        )
        footer_left = "STA237: Probability — University of Toronto"
        footer_right = f"Page {page_num} of {total_pages}"
        page.insert_text(
            pymupdf.Point(45, rect.height - 26),
            footer_left,
            fontsize=7.5,
            fontname="helv",
            color=(0.45, 0.48, 0.52)
        )
        right_len_f = pymupdf.get_text_length(footer_right, fontname="helv", fontsize=7.5)
        page.insert_text(
            pymupdf.Point(rect.width - 45 - right_len_f, rect.height - 26),
            footer_right,
            fontsize=7.5,
            fontname="helv",
            color=(0.45, 0.48, 0.52)
        )

    # Set metadata
    doc.set_metadata({
        "title": metadata.get("title", ""),
        "author": metadata.get("author", "Department of Statistical Sciences, University of Toronto"),
        "subject": metadata.get("subject", "STA237 Probability"),
        "keywords": metadata.get("keywords", "STA237, Probability, Conditional Probability, Independence, Bayes Rule, Discrete Random Variables, PMF"),
        "creator": "PyMuPDF & Google Chrome Headless"
    })

    doc.save(final_pdf_path)
    doc.close()
    final_size = os.path.getsize(final_pdf_path)
    print(f"Final PDF saved: {final_pdf_path} ({final_size:,} bytes, {total_pages} pages)")

def main():
    tasks = [
        {
            "name": "Study-Notes",
            "header_left": "STA237: Probability (Week 3)",
            "header_right": "Conditional Probability, Independence, Bayes' Rule, and Discrete RVs",
            "meta": {
                "title": "STA237 Week 3: Conditional Probability, Independence, Bayes' Rule, and Discrete RVs — Comprehensive Study Notes",
                "author": "Department of Statistical Sciences, University of Toronto",
                "subject": "STA237 Week 3 Study Notes: Conditional Probability, Independence, Total Probability, Bayes, PMFs",
                "keywords": "STA237, Probability, Conditional Probability, Independence, Bayes Rule, Discrete Random Variables, PMF"
            },
            "virtual_time": 35000
        },
        {
            "name": "Answers-and-Practice",
            "header_left": "STA237: Probability (Week 3)",
            "header_right": "Answers, Worked Solutions, and Practice Exercises",
            "meta": {
                "title": "STA237 Week 3: Answers, Worked Solutions, and Practice Exercises",
                "author": "Department of Statistical Sciences, University of Toronto",
                "subject": "STA237 Week 3 Solutions: Lecture Examples, MMSA Ch 2-3, PAR Ch 2-3 Exercises",
                "keywords": "STA237, Solutions, Bayes Rule, System Reliability, Total Probability, Discrete RVs, PMF, MMSA, PAR"
            },
            "virtual_time": 45000
        }
    ]

    for task in tasks:
        name = task["name"]
        print(f"\n==========================================")
        print(f"Processing: {name}")
        print(f"==========================================")
        md_file = os.path.join(BASE_DIR, f"{name}.md")
        html_file = os.path.join(SCRATCH_DIR, f"{name}.html")
        raw_pdf = os.path.join(SCRATCH_DIR, f"{name}_raw.pdf")
        final_pdf = os.path.join(OUTPUT_DIR, f"{name}.pdf")

        convert_md_to_html(md_file, html_file)
        compile_raw_pdf(html_file, raw_pdf, virtual_time=task["virtual_time"])
        postprocess_with_pymupdf(raw_pdf, final_pdf, task["header_left"], task["header_right"], task["meta"])

if __name__ == "__main__":
    main()

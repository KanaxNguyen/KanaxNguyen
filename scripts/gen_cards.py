"""Render the profile README cards as SVG from live GitHub data.

Needs GITHUB_TOKEN in the environment. Writes assets/*.svg. Standard library only.
"""
import base64
import json
import os
import textwrap
import urllib.request
from html import escape
from pathlib import Path

USER = os.environ.get("USERNAME", "KanaxNguyen")
OUT = Path(__file__).resolve().parent.parent / "assets"

BG, PANEL, BORDER = "#0d1117", "#161b22", "#30363d"
TEXT, MUTED, DIM = "#e6edf3", "#8b949e", "#6e7681"
GREEN = "#3fb950"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

# Notebooks and markup inflate byte counts without saying much about the code itself.
SKIP_LANGS = {"Jupyter Notebook", "HTML", "CSS", "TSQL", "Dockerfile", "Makefile", "Procfile"}

PROJECTS = [
    {
        "file": "project-cabinsentinel.svg",
        "title": "CabinSentinel",
        "meta": "Sep 2026 – now · team of 4 · backend, IoT, iOS",
        "en": "Detects children and pets left behind in parked cars. FastAPI safety engine "
              "(490+ tests), Raspberry Pi 5 edge service, native SwiftUI app with Live "
              "Activities and on-device Core ML.",
        "vi": "Luật “không phát hiện ≠ ghế trống”: báo trống sai từ 288/288 xuống 0/288.",
        "chips": ["FastAPI", "SwiftUI", "Core ML", "Raspberry Pi 5"],
        "accent": "#3fb950",
    },
    {
        "file": "project-huce.svg",
        "title": "HUCE Teaching Assignment",
        "meta": "Jul 2026 – now · piloted with a lecturer",
        "en": "Imports messy Excel schedules and auto-assigns lecturers with OR-Tools "
              "CP-SAT: no clashes, balanced workload. Improved from real user feedback.",
        "vi": "Tự động phân công giảng dạy cho Bộ môn Toán, chạy thử với giảng viên thật.",
        "chips": ["Next.js", "FastAPI", "OR-Tools"],
        "accent": "#58a6ff",
    },
    {
        "file": "project-adas.svg",
        "title": "ADAS for Vietnamese Roads",
        "meta": "Jan – Mar 2026 · team lead",
        "en": "ResNet-FPN multi-task network for Vietnamese speed signs and lane "
              "segmentation, with IoU tracking and a speed-limit rule engine "
              "(Circular 38/2024).",
        "vi": "Tự thu thập và gán nhãn 300 ảnh đường phố Việt Nam.",
        "chips": ["PyTorch", "ResNet-FPN", "Tracking"],
        "accent": "#f0883e",
    },
    {
        "file": "project-vinfast.svg",
        "title": "VinFast Vehicle Detection",
        "meta": "2026 · Kaggle · no-YOLO constraint",
        "en": "Faster R-CNN detector for VinFast vehicles reaching mAP@0.5 = 0.9523 "
              "with test-time augmentation, weighted boxes fusion and false-positive filtering.",
        "vi": "Nhận diện xe VinFast khi không được dùng YOLO.",
        "chips": ["PyTorch", "Faster R-CNN", "Kaggle"],
        "accent": "#a371f7",
    },
]

QUERY = """
query($login: String!) {
  user(login: $login) {
    name login avatarUrl(size: 200) location company
    followers { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, privacy: PUBLIC) {
      totalCount
      nodes {
        isFork
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      contributionCalendar { totalContributions }
    }
  }
}
"""


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "User-Agent": "profile-cards"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if "errors" in body:
        raise SystemExit(body["errors"])
    return body["data"]["user"]


def avatar_data_uri(url):
    # Images inside an SVG served through <img> cannot load external files, so the avatar is embedded.
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "profile-cards"}), timeout=30) as r:
        kind = r.headers.get_content_type() or "image/png"
        return f"data:{kind};base64,{base64.b64encode(r.read()).decode()}"


def t(s):
    return escape(str(s), quote=True)


def frame(w, h, body, title="README.md"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<defs>
  <radialGradient id="glow" cx="85%" cy="0%" r="70%">
    <stop offset="0%" stop-color="{GREEN}" stop-opacity="0.18"/>
    <stop offset="100%" stop-color="{GREEN}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse">
    <circle cx="1" cy="1" r="1" fill="#ffffff" fill-opacity="0.05"/>
  </pattern>
  <clipPath id="card"><rect width="{w}" height="{h}" rx="16"/></clipPath>
</defs>
<g clip-path="url(#card)">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <rect width="{w}" height="{h}" fill="url(#dots)"/>
  <rect width="{w}" height="{h}" fill="url(#glow)"/>
  <rect width="{w}" height="38" fill="{PANEL}"/>
  <line x1="0" y1="38" x2="{w}" y2="38" stroke="{BORDER}"/>
  <circle cx="22" cy="19" r="6" fill="#ff5f57"/><circle cx="42" cy="19" r="6" fill="#febc2e"/><circle cx="62" cy="19" r="6" fill="#28c840"/>
  <text x="84" y="23.5" font-family="{MONO}" font-size="12" fill="{MUTED}">{t(USER)} / {t(title)}</text>
  {body}
</g>
<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="16" fill="none" stroke="{BORDER}"/>
</svg>
"""


def chips(items, x, y, color=GREEN, size=12):
    out, cx = [], x
    for item in items:
        w = len(item) * size * 0.62 + 20
        out.append(
            f'<rect x="{cx:.1f}" y="{y}" width="{w:.1f}" height="24" rx="12" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-opacity="0.45"/>'
            f'<text x="{cx + w / 2:.1f}" y="{y + 16}" text-anchor="middle" font-family="{MONO}" font-size="{size}" fill="{color}">{t(item)}</text>'
        )
        cx += w + 8
    return "".join(out)


def header(u, contributions):
    w, h = 840, 280
    avatar = avatar_data_uri(u["avatarUrl"])
    tagline = "> AI undergrad · Computer Vision · Edge AI"
    type_w = len(tagline) * 14 * 0.61
    facts = [
        ("FPT University Hanoi", "Đại học FPT Hà Nội"),
        ("Hanoi, Vietnam", "Hà Nội, Việt Nam"),
        (f"{contributions} contributions / year", f"{contributions} đóng góp trong năm"),
    ]
    rows = "".join(
        f'<circle cx="604" cy="{104 + i * 46}" r="4" fill="{GREEN}"/>'
        f'<text x="618" y="{108 + i * 46}" font-family="{SANS}" font-size="13" font-weight="600" fill="{TEXT}">{t(en)}</text>'
        f'<text x="618" y="{125 + i * 46}" font-family="{SANS}" font-size="11.5" fill="{MUTED}">{t(vi)}</text>'
        for i, (en, vi) in enumerate(facts)
    )
    body = f"""
  <style>
    .type {{ animation: type 3.2s steps({len(tagline)}, end) 0.4s both; }}
    .caret {{ animation: blink 1s step-end infinite; }}
    .pulse {{ animation: pulse 2.6s ease-out infinite; transform-origin: 100px 150px; }}
    @keyframes type {{ from {{ width: 0 }} to {{ width: {type_w:.0f}px }} }}
    @keyframes blink {{ 50% {{ opacity: 0 }} }}
    @keyframes pulse {{ 0% {{ opacity: .7; transform: scale(1) }} 100% {{ opacity: 0; transform: scale(1.25) }} }}
  </style>
  <clipPath id="av"><circle cx="100" cy="150" r="58"/></clipPath>
  <clipPath id="typing"><rect class="type" x="182" y="158" height="24" width="{type_w:.0f}"/></clipPath>
  <circle class="pulse" cx="100" cy="150" r="62" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <image href="{avatar}" x="42" y="92" width="116" height="116" clip-path="url(#av)" preserveAspectRatio="xMidYMid slice"/>
  <circle cx="100" cy="150" r="60" fill="none" stroke="{GREEN}" stroke-width="3"/>
  <text x="182" y="92" font-family="{MONO}" font-size="14" fill="{GREEN}">@{t(u["login"])}</text>
  <text x="180" y="138" font-family="{SANS}" font-size="36" font-weight="800" fill="{TEXT}">Nguyễn Nam Khánh</text>
  <g clip-path="url(#typing)"><text x="182" y="176" font-family="{MONO}" font-size="14" fill="#c9d1d9">{t(tagline)}</text></g>
  <rect class="caret" x="{186 + type_w:.0f}" y="162" width="8" height="18" fill="{GREEN}"/>
  <text x="182" y="202" font-family="{SANS}" font-size="13" fill="{MUTED}">Biến bài toán thật thành sản phẩm chạy được</text>
  {chips(["Python", "PyTorch", "SwiftUI", "FastAPI", "Core ML"], 182, 222)}
  <line x1="582" y1="72" x2="582" y2="240" stroke="{BORDER}"/>
  {rows}
"""
    return frame(w, h, body)


def signal(u, contributions):
    w, h = 410, 270
    stats = [
        (contributions, "Contributions", "Đóng góp / năm"),
        (u["contributionsCollection"]["totalCommitContributions"], "Commits", "Commit / năm"),
        (u["repositories"]["totalCount"], "Repositories", "Kho mã công khai"),
        (len(languages(u)), "Languages", "Ngôn ngữ đã dùng"),
    ]
    boxes = []
    for i, (value, en, vi) in enumerate(stats):
        x, y = 20 + (i % 2) * 190, 92 + (i // 2) * 84
        boxes.append(
            f'<rect x="{x}" y="{y}" width="180" height="74" rx="12" fill="{PANEL}" stroke="{BORDER}"/>'
            f'<text x="{x + 16}" y="{y + 36}" font-family="{SANS}" font-size="28" font-weight="800" fill="{GREEN}">{t(value)}</text>'
            f'<text x="{x + 16}" y="{y + 54}" font-family="{SANS}" font-size="12" font-weight="600" fill="{TEXT}">{t(en)}</text>'
            f'<text x="{x + 16}" y="{y + 68}" font-family="{SANS}" font-size="10.5" fill="{MUTED}">{t(vi)}</text>'
        )
    body = f"""
  <text x="20" y="66" font-family="{SANS}" font-size="17" font-weight="700" fill="{TEXT}">Profile Signal</text>
  <text x="390" y="66" text-anchor="end" font-family="{MONO}" font-size="11" fill="{GREEN}">● live · cập nhật mỗi ngày</text>
  {''.join(boxes)}
"""
    return frame(w, h, body, "signal.json")


def languages(u):
    totals = {}
    for repo in u["repositories"]["nodes"]:
        if repo["isFork"]:
            continue
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name in SKIP_LANGS:
                continue
            color = edge["node"]["color"] or MUTED
            size, _ = totals.get(name, (0, color))
            totals[name] = (size + edge["size"], color)
    return sorted(totals.items(), key=lambda kv: -kv[1][0])


def language_card(u):
    w, h = 410, 270
    langs = [l for l in languages(u) if l[1][0] / sum(s for _, (s, _) in languages(u)) >= 0.01][:6]
    total = sum(size for _, (size, _) in langs) or 1
    rows = []
    for i, (name, (size, color)) in enumerate(langs):
        y = 98 + i * 27
        pct = size / total * 100
        bar = max(4, 200 * pct / 100)
        rows.append(
            f'<circle cx="26" cy="{y - 4}" r="5" fill="{color}"/>'
            f'<text x="38" y="{y}" font-family="{MONO}" font-size="12.5" fill="{TEXT}">{t(name)}</text>'
            f'<rect x="146" y="{y - 10}" width="200" height="8" rx="4" fill="#21262d"/>'
            f'<rect x="146" y="{y - 10}" width="{bar:.1f}" height="8" rx="4" fill="{color}"/>'
            f'<text x="390" y="{y}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{MUTED}">{pct:.0f}%</text>'
        )
    body = f"""
  <text x="20" y="66" font-family="{SANS}" font-size="17" font-weight="700" fill="{TEXT}">Language Stack</text>
  <text x="390" y="66" text-anchor="end" font-family="{MONO}" font-size="11" fill="{MUTED}">own repos · by code size</text>
  {''.join(rows)}
  <text x="20" y="258" font-family="{SANS}" font-size="10.5" fill="{DIM}">Ngôn ngữ trong các repo của mình (không tính notebook và HTML/CSS)</text>
"""
    return frame(w, h, body, "languages.json")


def project_card(p):
    w, h = 410, 262
    en = textwrap.wrap(p["en"], 58)[:4]
    vi = textwrap.wrap(p["vi"], 60)[:2]
    lines = "".join(
        f'<text x="20" y="{112 + i * 18}" font-family="{SANS}" font-size="12.5" fill="#c9d1d9">{t(line)}</text>'
        for i, line in enumerate(en)
    )
    vy = 112 + len(en) * 18 + 6
    vlines = "".join(
        f'<text x="20" y="{vy + i * 16}" font-family="{SANS}" font-size="11.5" font-style="italic" fill="{MUTED}">{t(line)}</text>'
        for i, line in enumerate(vi)
    )
    body = f"""
  <rect x="0" y="38" width="{w}" height="3" fill="{p['accent']}"/>
  <text x="20" y="72" font-family="{SANS}" font-size="18" font-weight="800" fill="{TEXT}">{t(p['title'])}</text>
  <text x="390" y="72" text-anchor="end" font-family="{SANS}" font-size="16" fill="{p['accent']}">↗</text>
  <text x="20" y="91" font-family="{MONO}" font-size="11" fill="{p['accent']}">{t(p['meta'])}</text>
  {lines}
  {vlines}
  {chips(p['chips'], 20, h - 40, p['accent'], 11)}
"""
    return frame(w, h, body, p["file"].removeprefix("project-").removesuffix(".svg"))


def main():
    u = fetch()
    contributions = u["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    OUT.mkdir(exist_ok=True)
    (OUT / "header.svg").write_text(header(u, contributions), encoding="utf-8")
    (OUT / "signal.svg").write_text(signal(u, contributions), encoding="utf-8")
    (OUT / "languages.svg").write_text(language_card(u), encoding="utf-8")
    for p in PROJECTS:
        (OUT / p["file"]).write_text(project_card(p), encoding="utf-8")
    print(f"wrote {len(PROJECTS) + 3} cards to {OUT}")


if __name__ == "__main__":
    main()

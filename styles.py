"""Blue-and-white theme. Plain CSS only (no JavaScript)."""
CSS = """
<style>
.block-container {padding-top: 1.4rem; max-width: 1200px;}
h1, h2, h3 {color: #0b2a6f; letter-spacing: -0.01em;}
[data-testid="stSidebar"] {
    background-color: #eff6ff !important;
    color: #0f172a !important;
    border-right: 1px solid #dbeafe;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label,
[data-testid="stSidebar"] [data-testid="stRadio"] label *,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #0f172a !important;
    opacity: 1 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    font-weight: 600 !important;
}
.cc-brand {padding: .4rem .2rem 1rem .2rem;}
.cc-brand b {font-size: 1.35rem; color: #0b2a6f;}
.cc-brand span {display:block; font-size:.78rem; color:#475569;}
.cc-hero {background: linear-gradient(120deg, #0b2a6f 0%, #1d4ed8 60%, #3b82f6 100%);
  color: #fff; padding: 1.6rem 1.8rem; border-radius: 16px; margin-bottom: 1.2rem;}
.cc-hero .t {font-size: 2rem; font-weight: 800; line-height: 1.1;}
.cc-hero .s {font-size: 1.05rem; opacity: .95; margin-top: .25rem;}
.cc-hero .u {font-size: .85rem; opacity: .8; margin-top: .5rem; letter-spacing: .06em; text-transform: uppercase;}
.cc-page-title {display:flex; align-items:center; gap:.6rem; margin-bottom:.2rem;}
.cc-stat {background:#fff; border:1px solid #dbeafe; border-left:5px solid #1d4ed8; border-radius:12px;
  padding: .9rem 1.1rem; margin-bottom: .8rem; box-shadow: 0 1px 3px rgba(15,23,42,.06);}
.cc-stat .v {font-size: 1.9rem; font-weight: 800; color:#0b2a6f; line-height:1.1;}
.cc-stat .l {font-size: .85rem; color:#475569;}
.cc-stat.warn {border-left-color:#d97706;} .cc-stat.bad {border-left-color:#dc2626;} .cc-stat.good {border-left-color:#16a34a;}
.cc-note {background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:.7rem 1rem; color:#1e3a8a; font-size:.9rem; margin:.6rem 0;}
.cc-demo {background:#fffbeb; border:1px solid #fde68a; border-radius:10px; padding:.55rem .9rem; color:#92400e; font-size:.85rem; margin-bottom:.8rem;}
.cc-match {background:#fff; border:1px solid #dbeafe; border-radius:14px; padding: 1rem 1.2rem; margin-bottom:.8rem;
  box-shadow: 0 1px 3px rgba(15,23,42,.06);}
.cc-match .top {display:flex; justify-content:space-between; align-items:center; gap:1rem; flex-wrap:wrap;}
.cc-match .name {font-weight:700; font-size:1.05rem; color:#0b2a6f;}
.cc-match .meta {color:#475569; font-size:.88rem; margin-top:.2rem;}
.cc-match .score {font-size:1.7rem; font-weight:800; color:#1d4ed8; text-align:right; line-height:1;}
.cc-match .score small {display:block; font-size:.72rem; font-weight:600; color:#475569;}
.cc-bar {height:8px; border-radius:6px; background:#e2e8f0; margin:.7rem 0 .4rem 0; overflow:hidden;}
.cc-bar > div {height:100%; background: linear-gradient(90deg,#60a5fa,#1d4ed8);}
.cc-break {font-size:.8rem; color:#475569;}
.cc-badge {display:inline-block; padding:.12rem .6rem; border-radius:999px; font-size:.75rem; font-weight:700;}
.cc-low {background:#dcfce7; color:#166534;} .cc-medium {background:#fef3c7; color:#92400e;} .cc-high {background:#fee2e2; color:#991b1b;}
.cc-flow {display:flex; flex-wrap:wrap; align-items:center; gap:.4rem; margin:.5rem 0 1rem 0;}
.cc-step {background:#1d4ed8; color:#fff; border-radius:8px; padding:.35rem .7rem; font-size:.85rem; font-weight:600;}
.cc-arrow {color:#1d4ed8; font-weight:800;}
@media (max-width: 640px) {
  .cc-hero .t {font-size: 1.5rem;} .cc-stat .v {font-size: 1.5rem;} .cc-match .score {text-align:left;}
}
/* ===== CampusConnect Professional Blue Theme ===== */

.stApp,
[data-testid="stAppViewContainer"] {
    background-color: #EAF1F7 !important;
}

[data-testid="stMain"] {
    background-color: #EAF1F7 !important;
}

[data-testid="stHeader"] {
    background-color: #EAF1F7 !important;
}

[data-testid="stSidebar"] {
    background-color: #DCEAF5 !important;
    border-right: 1px solid #C5D9E9 !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] a {
    color: #172F49 !important;
}

[data-testid="stMain"] h1,
[data-testid="stMain"] h2,
[data-testid="stMain"] h3 {
    color: #164E7A !important;
}

.cc-stat,
.cc-match {
    background-color: #FFFFFF !important;
    color: #172F49 !important;
    border-color: #D5E2ED !important;
}

.stButton > button {
    background-color: #256DA8 !important;
    color: #FFFFFF !important;
    border: 1px solid #256DA8 !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background-color: #FFFFFF !important;
}

.stTextInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #172F49 !important;
}
</style>
"""

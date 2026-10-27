# -*- coding: utf-8 -*-
"""
Generate the complete Estonian Procurement Translation and Interactive Documentation Web App in Latvian.
"""
import json, os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from data_dashboard import DASHBOARD_DATA
from data_uldosa import ULDOSA_DATA
from data_lisa1 import LISA1_DATA
from data_lisa2 import LISA2_DATA
from data_lisa3 import LISA3_DATA
from data_lisa4 import LISA4_DATA
from data_others import OTHERS_DATA
from data_proovitoo_strategy import PROOVITOO_STRATEGY_HTML

cfr_path = os.path.join(SCRIPT_DIR, "cfr_translated_complete.json")
with open(cfr_path, "r", encoding="utf-8") as f:
    cfr_items = json.load(f)

cfr_json_str = json.dumps(cfr_items, ensure_ascii=False)
print(f"Loaded {len(cfr_items)} CFR items.")

html_template = """<!DOCTYPE html>
<html lang="lv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Iepirkuma dokumentācija | EIS 315313 | Tīmekļu un IS analīze, izstrāde un uzturēšana 2026-2029</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #0047b3;
      --primary-dark: #002b80;
      --primary-light: #e6f0ff;
      --accent: #2563eb;
      --bg: #f8fafc;
      --surface: #ffffff;
      --surface-alt: #f1f5f9;
      --border: #e2e8f0;
      --border-dark: #cbd5e1;
      --text: #0f172a;
      --text-muted: #475569;
      --text-light: #64748b;
      --success: #059669;
      --success-light: #ecfdf5;
      --warning: #d97706;
      --warning-light: #fffbeb;
      --danger: #dc2626;
      --danger-light: #fef2f2;
      --purple: #7c3aed;
      --purple-light: #f5f3ff;
      --sidebar-width: 320px;
      --header-height: 72px;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --radius: 10px;
      --radius-sm: 6px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }

    h1, h2, h3, h4, .brand-font {
      font-family: 'Outfit', 'Inter', sans-serif;
      font-weight: 700;
      color: var(--text);
      line-height: 1.25;
    }

    code, pre {
      font-family: 'JetBrains Mono', monospace;
    }

    /* Top Sticky Header */
    .top-header {
      position: sticky;
      top: 0;
      z-index: 100;
      height: var(--header-height);
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 2rem;
      box-shadow: var(--shadow-sm);
    }

    .header-brand {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .brand-logo {
      background: linear-gradient(135deg, var(--primary) 0%, #1e40af 100%);
      color: #fff;
      font-weight: 800;
      font-size: 1.15rem;
      padding: 0.5rem 0.85rem;
      border-radius: var(--radius-sm);
      letter-spacing: 0.5px;
      box-shadow: 0 2px 4px rgba(0, 71, 179, 0.25);
    }

    .brand-text h1 {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .brand-text p {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1.1rem;
      font-size: 0.875rem;
      font-weight: 600;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid transparent;
      text-decoration: none;
    }

    .btn-primary {
      background: var(--primary);
      color: #fff;
    }
    .btn-primary:hover {
      background: var(--primary-dark);
      box-shadow: 0 2px 6px rgba(0, 71, 179, 0.3);
    }

    .btn-outline {
      background: var(--surface);
      border-color: var(--border-dark);
      color: var(--text);
    }
    .btn-outline:hover {
      background: var(--surface-alt);
      border-color: var(--text-muted);
    }

    .btn-sm {
      padding: 0.35rem 0.75rem;
      font-size: 0.8rem;
    }

    /* Layout */
    .app-container {
      display: flex;
      min-height: calc(100vh - var(--header-height));
    }

    /* Sidebar */
    .sidebar {
      width: var(--sidebar-width);
      flex-shrink: 0;
      background: var(--surface);
      border-right: 1px solid var(--border);
      position: sticky;
      top: var(--header-height);
      height: calc(100vh - var(--header-height));
      overflow-y: auto;
      padding: 1.5rem 1rem;
    }

    .nav-group-title {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-light);
      font-weight: 700;
      padding: 0.5rem 0.75rem;
      margin-top: 1rem;
    }

    .nav-group-title:first-child {
      margin-top: 0;
    }

    .nav-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }

    .nav-link {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.55rem 0.75rem;
      border-radius: var(--radius-sm);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 500;
      transition: all 0.15s ease;
    }

    .nav-link:hover {
      background: var(--surface-alt);
      color: var(--primary);
    }

    .nav-link.active {
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 600;
    }

    .nav-link .badge {
      font-size: 0.7rem;
      padding: 0.15rem 0.45rem;
      border-radius: 9999px;
      font-weight: 700;
    }

    /* Main Content */
    .main-content {
      flex: 1;
      padding: 2.5rem 3rem;
      max-width: 1280px;
      overflow-x: hidden;
    }

    .doc-section {
      background: var(--surface);
      border-radius: var(--radius);
      border: 1px solid var(--border);
      padding: 2.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      scroll-margin-top: calc(var(--header-height) + 1.5rem);
    }

    .section-header {
      border-bottom: 1px solid var(--border);
      padding-bottom: 1.25rem;
      margin-bottom: 1.75rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .section-header h2 {
      font-size: 1.75rem;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .section-subtitle {
      color: var(--text-muted);
      font-size: 0.95rem;
    }

    .section-header .tag-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 0.25rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      font-size: 0.775rem;
      font-weight: 600;
      line-height: 1;
    }

    .badge-primary { background: var(--primary-light); color: var(--primary); }
    .badge-success { background: var(--success-light); color: var(--success); }
    .badge-warning { background: var(--warning-light); color: var(--warning); }
    .badge-danger { background: var(--danger-light); color: var(--danger); }
    .badge-purple { background: var(--purple-light); color: var(--purple); }
    .badge-muted { background: var(--surface-alt); color: var(--text-muted); }

    /* Dashboard Cards */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1.25rem;
      margin-bottom: 2rem;
    }

    .kpi-card {
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .kpi-card:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow);
      border-color: var(--accent);
    }

    .kpi-label {
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-light);
    }

    .kpi-value {
      font-size: 1.65rem;
      font-weight: 800;
      color: var(--primary);
      font-family: 'Outfit', sans-serif;
    }

    .kpi-desc {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    /* Callout Boxes */
    .callout {
      border-left: 4px solid var(--accent);
      background: var(--primary-light);
      padding: 1.25rem 1.5rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin: 1.5rem 0;
    }

    .callout-title {
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .callout-warning {
      border-left-color: var(--warning);
      background: var(--warning-light);
    }
    .callout-warning .callout-title { color: var(--warning); }

    .callout-success {
      border-left-color: var(--success);
      background: var(--success-light);
    }
    .callout-success .callout-title { color: var(--success); }

    .callout-purple {
      border-left-color: var(--purple);
      background: var(--purple-light);
    }
    .callout-purple .callout-title { color: var(--purple); }

    /* Tables */
    .table-container {
      overflow-x: auto;
      margin: 1.5rem 0;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9rem;
    }

    th {
      background: var(--surface-alt);
      color: var(--text);
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border);
      font-size: 0.825rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    td {
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
      vertical-align: top;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:hover td {
      background: #fafbfd;
    }

    /* Original Estonian Collapsible Block */
    .orig-block {
      margin-top: 1rem;
      border: 1px dashed var(--border-dark);
      border-radius: var(--radius-sm);
      background: #fafafa;
      overflow: hidden;
    }

    .orig-header {
      padding: 0.5rem 1rem;
      background: #f1f5f9;
      cursor: pointer;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
    }

    .orig-header:hover {
      background: #e2e8f0;
      color: var(--text);
    }

    .orig-content {
      padding: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      font-style: italic;
      display: none;
      line-height: 1.5;
    }

    .orig-content.open {
      display: block;
    }

    /* Paragraph Blocks */
    .para-item {
      margin-bottom: 1.25rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #f1f5f9;
    }
    .para-item:last-child {
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }

    /* Interactive Tools */
    .calc-box {
      background: linear-gradient(to right, #f8fafc, #ffffff);
      border: 2px solid var(--primary);
      border-radius: var(--radius);
      padding: 2rem;
      margin: 1.5rem 0;
      box-shadow: var(--shadow);
    }

    .calc-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }

    .calc-field label {
      display: block;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      color: var(--text);
    }

    .calc-input {
      width: 100%;
      padding: 0.75rem 1rem;
      font-size: 1.1rem;
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-family: inherit;
    }

    .calc-input:focus {
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(0, 71, 179, 0.15);
    }

    .calc-score-display {
      background: var(--primary);
      color: #fff;
      padding: 1.5rem;
      border-radius: var(--radius);
      text-align: center;
      margin-top: 1.5rem;
    }

    .calc-score-number {
      font-size: 3rem;
      font-weight: 800;
      font-family: 'Outfit', sans-serif;
      line-height: 1;
      margin-bottom: 0.5rem;
    }

    /* CFR Filter bar */
    .filter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1.25rem;
      align-items: center;
    }

    .filter-chip {
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: 9999px;
      padding: 0.35rem 0.85rem;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .filter-chip:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    .filter-chip.active {
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }

    .search-box {
      flex: 1;
      min-width: 250px;
      position: relative;
    }

    .search-input {
      width: 100%;
      padding: 0.55rem 1rem 0.55rem 2.25rem;
      font-size: 0.875rem;
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-sm);
      outline: none;
    }

    .search-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(0, 71, 179, 0.1);
    }

    .search-icon {
      position: absolute;
      left: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-light);
      pointer-events: none;
    }

    /* Print styles */
    @media print {
      .top-header, .sidebar, .header-actions, .orig-header, .filter-bar, .search-box {
        display: none !important;
      }
      .app-container {
        display: block;
      }
      .main-content {
        padding: 0;
        max-width: 100%;
      }
      .doc-section {
        border: none;
        box-shadow: none;
        padding: 1rem 0;
        page-break-after: always;
      }
    }

    @media (max-width: 1024px) {
      .app-container {
        flex-direction: column;
      }
      .sidebar {
        width: 100%;
        height: auto;
        position: static;
        border-right: none;
        border-bottom: 1px solid var(--border);
      }
      .main-content {
        padding: 1.5rem;
      }
    }
  </style>
</head>
<body>

  <!-- Top Sticky Navigation -->
  <header class="top-header">
    <div class="header-brand">
      <div class="brand-logo">EIS</div>
      <div class="brand-text">
        <h1>Iepirkuma dokumentācija (Nr. 315313) <span class="badge badge-success">Tulkojums LV</span></h1>
        <p>Veebide ja infosüsteemide analüüsi, arendus- ning hooldustööd 2026 - 2029 (750 000 €)</p>
      </div>
    </div>
    <div class="header-actions">
      <button class="btn btn-outline btn-sm" onclick="toggleAllOriginals()" id="toggleOrigBtn">
        <span>🌐 Rādīt EE oriģinālu</span>
      </button>
      <button class="btn btn-outline btn-sm" onclick="window.print()">
        <span>🖨️ Drukāt / PDF</span>
      </button>
      <a href="#kalkulators" class="btn btn-primary btn-sm">
        <span>🧮 Punktu kalkulators</span>
      </a>
    </div>
  </header>

  <div class="app-container">

    <!-- Sticky Left Sidebar -->
    <aside class="sidebar">
      <div class="nav-group-title">Pārskats un Rīki</div>
      <ul class="nav-list">
        <li><a href="#dashboard" class="nav-link active"><span>📊 Kopsavilkums & Dashboard</span></a></li>
        <li><a href="#proovitoo-strategija" class="nav-link" style="color:var(--purple); font-weight:600;"><span>🚀 Proovitöö stratēģija (80p)</span> <span class="badge badge-purple">Ceļvedis</span></a></li>
        <li><a href="#kalkulators" class="nav-link"><span>🧮 Vērtējuma kalkulators</span> <span class="badge badge-primary">20p / 80p</span></a></li>
        <li><a href="#komanda" class="nav-link"><span>👥 Komandas pārbaude</span> <span class="badge badge-success">6 lomas</span></a></li>
      </ul>

      <div class="nav-group-title">Iepirkuma dokumenti</div>
      <ul class="nav-list">
        <li><a href="#uldosa" class="nav-link"><span>1. Nolikums: Vispārīgā daļa</span> <span class="badge badge-muted">Üldosa</span></a></li>
        <li><a href="#lisa-1" class="nav-link"><span>2. Pielikums 1: Tehniskais apraksts</span> <span class="badge badge-muted">Lisa 1</span></a></li>
        <li><a href="#cv-forma" class="nav-link"><span>3. Pielikums 1.1: CV Forma</span> <span class="badge badge-muted">Lisa 1.1</span></a></li>
        <li><a href="#lisa-2" class="nav-link"><span>4. Pielikums 2: Vērtēšanas metodika</span> <span class="badge badge-muted">Lisa 2</span></a></li>
        <li><a href="#lisa-3" class="nav-link"><span>5. Pielikums 3: Vispārīgā vienošanās</span> <span class="badge badge-muted">Lisa 3</span></a></li>
        <li><a href="#gdpr" class="nav-link"><span>6. Pielikums 3.1: Datu apstrāde (GDPR)</span> <span class="badge badge-muted">GDPR</span></a></li>
        <li><a href="#lisa-4" class="nav-link"><span>7. Pielikums 4: Pārbaudes uzdevums</span> <span class="badge badge-purple">Proovitöö</span></a></li>
        <li><a href="#proovitoo-strategija" class="nav-link" style="background:#f5f3ff;"><span>💡 7.1. Risinājuma plāns</span> <span class="badge badge-purple">80p</span></a></li>
        <li><a href="#lisa-5" class="nav-link"><span>8. Pielikums 5: Šķērsfunkcionālās prasības</span> <span class="badge badge-primary">110 CFR</span></a></li>
        <li><a href="#vastavus" class="nav-link"><span>9. Atbilstības nosacījumi</span> <span class="badge badge-muted">RHR</span></a></li>
        <li><a href="#hindamine" class="nav-link"><span>10. Vērtēšanas kritēriju izraksts</span> <span class="badge badge-muted">RHR</span></a></li>
        <li><a href="#hankepass" class="nav-link"><span>11. ESPD / Hankepass kopsavilkums</span> <span class="badge badge-muted">ESPD</span></a></li>
      </ul>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">

      <!-- SECTION 0: DASHBOARD -->
      <section id="dashboard" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Atsauces Nr. 315313</span>
            <span class="badge badge-muted">Iekšējais Nr. HNR260046</span>
            <span class="badge badge-purple">Directus + Next.js</span>
            <span class="badge badge-success">Aktīvs iepirkums</span>
          </div>
          <h2>Iepirkuma kopsavilkums un galvenie rādītāji</h2>
          <p class="section-subtitle">
            <strong>Pasūtītājs:</strong> Ettevõtluse ja Innovatsiooni Sihtasutus (EIS / Igaunijas Uzņēmējdarbības un inovāciju fonds)<br>
            <strong>Priekšmets:</strong> Tīmekļa vietņu un informācijas sistēmu analīzes, izstrādes un uzturēšanas darbi 2026 – 2029
          </p>
        </div>

        <!-- KPI Grid -->
        <div class="kpi-grid">
          <div class="kpi-card">
            <span class="kpi-label">Līguma maksimālā summa</span>
            <span class="kpi-value">750 000 €</span>
            <span class="kpi-desc">Bez PVN (36 kalendāro mēnešu periodam)</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Līguma termiņš</span>
            <span class="kpi-value">36 Mēneši</span>
            <span class="kpi-desc">Pasūtījumu līgumi var turpināties vēl +12 mēn.</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Vērtēšanas proporcija</span>
            <span class="kpi-value">80% / 20%</span>
            <span class="kpi-desc">80 punkti Pārbaudes darbam, 20 punkti Cenai</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Minimālā vērtētā likme</span>
            <span class="kpi-value">60 € / stundā</span>
            <span class="kpi-desc">Cenas zem 60 € tiek pielīdzinātas 60 € slieksnim</span>
          </div>
        </div>

        <!-- Executive Highlights -->
        <h3 style="margin-bottom: 1rem;">Iepirkuma stratēģiskie uzsvari un tehnoloģijas</h3>
        <div class="kpi-grid">
          <div class="kpi-card" style="background:#fff;">
            <strong style="color:var(--primary); font-size:1.05rem;">Directus Headless CMS</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Konsolidācija: pāreja no sadrumstalotām WordPress un Laravel vietnēm uz vienotu Directus Headless satura pārvaldības sistēmu ar universāliem blokiem un daudzvalodu atbalstu.
            </p>
          </div>
          <div class="kpi-card" style="background:#fff;">
            <strong style="color:var(--primary); font-size:1.05rem;">Next.js & shadcn/ui</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Mūsdienīgs frontend: Next.js App Router, React, TypeScript, servera puses datu ielāde (SSR/SSG), ātrdarbība un DDS 2.0 (Igaunijas Zīmola) dizaina komponentes.
            </p>
          </div>
          <div class="kpi-card" style="background:#fff;">
            <strong style="color:var(--purple); font-size:1.05rem;">Mākslīgais intelekts (AI) & MCP</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              AI rīku atbalsts caur Model Context Protocol (MCP) slāni. Stingras kvalitātes un drošības prasības (CFR-102..108): 100% testu pārklājums AI kodam, obligāts Human Code Review un privātuma garantija.
            </p>
          </div>
          <div class="kpi-card" style="background:#fff;">
            <strong style="color:var(--success); font-size:1.05rem;">Riigipilv & GitOps</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Izvietošana Igaunijas Valsts mākonī (Riigipilv) uz Kubernetes klasteriem. CI/CD automatizācija ar GitLab CI un deklaratīvu izvietošanu caur ArgoCD.
            </p>
          </div>
        </div>

        <div class="callout callout-warning">
          <div class="callout-title">⚠️ Izšķirošais uzvaras faktors: Pārbaudes darbs (Proovitöö)</div>
          <p>
            Cenas stundas likme dod tikai 20 punktus (un likmes zem 60 €/h netiek apbalvotas). <strong>80 punktus izšķir Pārbaudes darbs</strong>, kas jāiesniedz kopā ar piedāvājumu (koncepcija, Figma DDS 2.0 prototips, strādājošs kods GitHub ar <code>docker compose</code> un 10 minūšu YouTube video prezentācija)!
          </p>
        </div>
      </section>

      <!-- SECTION: INTERACTIVE SCORING CALCULATOR -->
      <section id="kalkulators" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Rīks pretendentam</span>
            <span class="badge badge-purple">Punktu simulācija</span>
          </div>
          <h2>Interaktīvais vērtējuma punktu kalkulators</h2>
          <p class="section-subtitle">Aprēķiniet savu potenciālo punktu skaitu saskaņā ar RHAD 2. pielikuma un RHR oficiālo vērtēšanas metodiku.</p>
        </div>

        <div class="calc-box">
          <div class="calc-row">
            <div class="calc-field">
              <label>1. Pretendenta stundas likme (EUR bez PVN):</label>
              <input type="number" id="calcPriceInput" class="calc-input" value="65" min="20" max="150" step="1" oninput="recalcScore()">
              <small style="color:var(--text-muted); display:block; margin-top:0.35rem;">
                * Piezīme: Visi piedāvājumi zem 60 EUR/h tiek pielīdzināti 60 EUR/h.
              </small>
            </div>
            <div class="calc-field">
              <label>Zemākā iespējamā konkurenta likme tirgū (min slieksnis):</label>
              <input type="number" id="calcMinPrice" class="calc-input" value="60" min="20" max="120" step="1" oninput="recalcScore()" readonly style="background:#e2e8f0;">
              <small style="color:var(--text-muted); display:block; margin-top:0.35rem;">
                Nolikuma oficiālā aprēķina bāze.
              </small>
            </div>
          </div>

          <h4 style="margin: 1.5rem 0 0.75rem 0;">2. Pārbaudes darba (Proovitöö) apakškritēriji (Kopā max 80 punkti):</h4>

          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:1rem;">
            <div class="calc-field" style="background:#fff; padding:1rem; border-radius:var(--radius-sm); border:1px solid var(--border);">
              <label>Analītiskā loģika un struktūra (max 20p):</label>
              <select id="sub1" class="calc-input" style="font-size:0.95rem;" onchange="recalcScore()">
                <option value="20" selected>20 punkti – Izcils / Labākais</option>
                <option value="15">15 punkti – Ļoti labs</option>
                <option value="10">10 punkti – Vidējs</option>
                <option value="5">5 punkti – Vājš</option>
                <option value="1">1 punkts – Neapmierinošs</option>
              </select>
            </div>

            <div class="calc-field" style="background:#fff; padding:1rem; border-radius:var(--radius-sm); border:1px solid var(--border);">
              <label>UX lietotāja ceļi un mērogojamība (max 20p):</label>
              <select id="sub2" class="calc-input" style="font-size:0.95rem;" onchange="recalcScore()">
                <option value="20" selected>20 punkti – Izcils / Labākais</option>
                <option value="15">15 punkti – Ļoti labs</option>
                <option value="10">10 punkti – Vidējs</option>
                <option value="5">5 punkti – Vājš</option>
                <option value="1">1 punkts – Neapmierinošs</option>
              </select>
            </div>

            <div class="calc-field" style="background:#fff; padding:1rem; border-radius:var(--radius-sm); border:1px solid var(--border);">
              <label>DDS 2.0 dizaina ieviešana (max 10p):</label>
              <select id="sub3" class="calc-input" style="font-size:0.95rem;" onchange="recalcScore()">
                <option value="10" selected>10 punkti – Izcils / Labākais</option>
                <option value="8">8 punkti – Ļoti labs</option>
                <option value="5">5 punkti – Vidējs</option>
                <option value="1">1 punkts – Neapmierinošs</option>
              </select>
            </div>

            <div class="calc-field" style="background:#fff; padding:1rem; border-radius:var(--radius-sm); border:1px solid var(--border);">
              <label>Tehniskais izpildījums un kods (max 20p):</label>
              <select id="sub4" class="calc-input" style="font-size:0.95rem;" onchange="recalcScore()">
                <option value="20" selected>20 punkti – Izcils / Labākais</option>
                <option value="15">15 punkti – Ļoti labs</option>
                <option value="10">10 punkti – Vidējs</option>
                <option value="5">5 punkti – Vājš</option>
                <option value="1">1 punkts – Neapmierinošs</option>
              </select>
            </div>

            <div class="calc-field" style="background:#fff; padding:1rem; border-radius:var(--radius-sm); border:1px solid var(--border);">
              <label>Video prezentācija 10 min (max 10p):</label>
              <select id="sub5" class="calc-input" style="font-size:0.95rem;" onchange="recalcScore()">
                <option value="10" selected>10 punkti – Izcils / Labākais</option>
                <option value="8">8 punkti – Ļoti labs</option>
                <option value="5">5 punkti – Vidējs</option>
                <option value="1">1 punkts – Neapmierinošs</option>
              </select>
            </div>
          </div>

          <!-- Total Score Display -->
          <div class="calc-score-display">
            <div style="font-size:0.9rem; text-transform:uppercase; letter-spacing:0.08em; opacity:0.85;">Kopējais prognozētais vērtējums:</div>
            <div class="calc-score-number" id="calcTotalPoints">100.00</div>
            <div style="font-size:1.05rem;" id="calcScoreBreakdown">
              Cena: <strong>20.00</strong> punkti | Pārbaudes darbs: <strong>80</strong> punkti
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION: TEAM QUALIFICATIONS CHECKER -->
      <section id="komanda" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-success">Kvalifikācijas matrica</span>
            <span class="badge badge-muted">RHAD 1. pielikuma 15. punkts</span>
          </div>
          <h2>Obligātās komandas kvalifikācijas pārbaude</h2>
          <p class="section-subtitle">Pārbaudiet savas komandas atbilstību katrai no 6 obligātajām lomām pirms CV noformēšanas.</p>
        </div>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width:22%;">Loma</th>
                <th style="width:15%;">Speciālistu skaits</th>
                <th style="width:28%;">Vispārējā pieredze</th>
                <th style="width:25%;">Projektu pieredze (pēdējie 36 mēn.)</th>
                <th style="width:10%;">Valoda</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. IT projektu vadītājs</strong></td>
                <td>Vismaz 1 persona</td>
                <td>Vismaz 24 mēnešu darba pieredze kā IT PM pēdējo 60 mēnešu laikā</td>
                <td>Vadījis vismaz 2 izstrādes projektus, katrā min 80 stundas</td>
                <td>Igauņu valoda</td>
              </tr>
              <tr>
                <td><strong>2. Front-end izstrādātāji</strong></td>
                <td>Vismaz 2 personas (abām jāatbilst!)</td>
                <td>CSS (Tailwind), JS, TypeScript (React, Next.js), HTML, PHP, Git</td>
                <td>Vismaz 2 izstrādes projekti ar minētajām tehnoloģijām, kopā min 800 stundas katram</td>
                <td>Angļu valoda</td>
              </tr>
              <tr>
                <td><strong>3. Full-stack izstrādātāji</strong></td>
                <td>Vismaz 2 personas (abām jāatbilst!)</td>
                <td>Docker, Kubernetes, PostgreSQL, Node.js, REST, Tailwind, React, Next.js, PHP, Git</td>
                <td>Vismaz 3 izstrādes projekti ar minētajām tehnoloģijām, kopā min 800 stundas katram</td>
                <td>Angļu valoda</td>
              </tr>
              <tr>
                <td><strong>4. Sistēmu / biznesa analītiķis</strong></td>
                <td>Vismaz 1 persona</td>
                <td>Biznesa procesu analīze un modelēšana</td>
                <td>Vismaz 3 izstrādes projekti (no tiem min 1 biznesa procesu modelēšana, piem., Enterprise Architect), kopā min 500 stundas</td>
                <td><span class="badge badge-danger">Igauņu B2</span></td>
              </tr>
              <tr>
                <td><strong>5. UX/UI dizaineris</strong></td>
                <td>Vismaz 1 persona</td>
                <td>Vismaz 24 mēnešu darba pieredze kā UX dizainerim pēdējos 60 mēnešos</td>
                <td>Vismaz 2 izstrādes projekti, kuros ievērots WCAG 2.0 AA un W3C standarti</td>
                <td>Angļu / Igauņu</td>
              </tr>
              <tr>
                <td><strong>6. Testētājs</strong></td>
                <td>Vismaz 1 persona</td>
                <td>Programmatūras un saskarņu testēšana</td>
                <td>Vismaz 2 programmatūras izstrādes projekti pēdējos 36 mēnešos</td>
                <td><span class="badge badge-danger">Igauņu B2</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout callout-success">
          <div class="callout-title">💡 Svarīgas nolikuma priekšrocības un noteikumi:</div>
          <p>
            • <strong>Lomu apvienošana:</strong> Viens komandas loceklis drīkst pildīt vairākas lomas (piem., analītiķis var būt arī PM vai testētājs), ja pilnībā atbilst abu lomu kritērijiem.<br>
            • <strong>Pakalpojuma valoda:</strong> Pretendentam jānodrošina pakalpojumu sniegšana igauņu valodā vismaz B2 līmenī.<br>
            • <strong>CV forma:</strong> Visi CV jāiesniedz uz Pielikuma 1.1 noteiktās veidlapas igauņu valodā!
          </p>
        </div>
      </section>

      <!-- SECTION 1: ULDOSA -->
      <section id="uldosa" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Pamatdokuments</span>
            <span class="badge badge-muted">RHAD Üldosa.docx</span>
          </div>
          <h2>1. Publiskā iepirkuma nolikuma Vispārīgā daļa</h2>
          <p class="section-subtitle">Procedūras pamatnoteikumi, prasības pretendentiem, iesniegšanas un vērtēšanas kārtība.</p>
        </div>

        <!-- Uldosa Table -->
        <h3 style="margin: 1.5rem 0 0.75rem 0;">Iepirkuma pamatdati</h3>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width:30%;">Parametrs (LV)</th>
                <th style="width:45%;">Vērtība</th>
                <th style="width:25%;">Oriģināls (EE)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Iepirkuma nosaukums</strong></td>
                <td>Tīmekļa vietņu un informācijas sistēmu analīzes, izstrādes un uzturēšanas darbi 2026 – 2029</td>
                <td>Veebide ja infosüsteemide analüüsi, arendus- ning hooldustööd 2026 - 2029</td>
              </tr>
              <tr>
                <td><strong>Atsauces numurs</strong></td>
                <td><span class="badge badge-primary">315313</span></td>
                <td>315313</td>
              </tr>
              <tr>
                <td><strong>Pasūtītāja iekšējais numurs</strong></td>
                <td>HNR260046</td>
                <td>HNR260046</td>
              </tr>
              <tr>
                <td><strong>Iepirkuma veids</strong></td>
                <td>Atklāts konkurss (e-procedūra e-riigihanked sistēmā)</td>
                <td>Avatud hankemenetlus / e-menetlus</td>
              </tr>
              <tr>
                <td><strong>Līguma veids</strong></td>
                <td>Vispārīgā vienošanās (noslēdz ar vienu uzvarētāju)</td>
                <td>Raamleping</td>
              </tr>
              <tr>
                <td><strong>Līguma periods</strong></td>
                <td>36 kalendārie mēneši vai līdz budžeta sasniegšanai</td>
                <td>36 kalendrikuud</td>
              </tr>
              <tr>
                <td><strong>Paredzamā līguma summa</strong></td>
                <td><strong>750 000,00 € (bez PVN)</strong></td>
                <td>750 000,00 €</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Uldosa Chapters -->
        <h3 style="margin: 2rem 0 1rem 0;">Nolikuma noteikumu tulkojums</h3>

        <div class="para-item">
          <h4>1. Vispārīgie noteikumi</h4>
          <p>
            <strong>RHAD sastāvs:</strong> Iepirkuma pamatdokumenti (nolikums) sastāv no šī faila pamatteksta un tā pielikumiem, kā arī e-iepirkumu vidē (RHR) pieejamā iepirkuma paziņojuma (HT), tīmekļa formām un lejupielādējamajiem dokumentiem saskaņā ar RHS 4. panta 1. daļas 17. punktu.
          </p>
          <p style="margin-top:0.5rem;">
            <strong>Nedalīšana daļās:</strong> Publiskais iepirkums nav sadalīts daļās, jo iepirkuma priekšmets ir funkcionāli kopā darbojošies pakalpojumi vienota mērķa sasniegšanai.
          </p>
          <p style="margin-top:0.5rem;">
            <strong>Atsauces un ekvivalence:</strong> Jebkura atsauce uz konkrētu zīmolu, patentu, izcelsmi vai ražotāju ir jāsaprot ar atzīmi <em>„vai līdzvērtīgs“</em>. Līdzvērtīgums nozīmē tādas pašas ekspluatācijas īpašības un funkcionalitāti, un par to jāiesniedz pierādījumi.
          </p>
          <p style="margin-top:0.5rem;">
            <strong>Dzīves cikla izmaksas:</strong> Netiek rēķinātas atsevišķi, jo līguma priekšmets ir jau esošas un pasūtītāja lietošanā esošas sistēmas uzlabošana un uzturēšana; izstrādes un uzturēšanas izmaksas ir iekļautas vienotajā darba stundas likmē.
          </p>
          <p style="margin-top:0.5rem;">
            <strong>Reversā pārbaude:</strong> Pasūtītājs var pārbaudīt piedāvājumu atbilstību un vērtēt piedāvājumus pirms izslēgšanas iemeslu un kvalifikācijas pārbaudes.
          </p>
          <p style="margin-top:0.5rem;">
            <strong>Valodu prioritāte:</strong> Pretrunu gadījumā starp igauņu valodu un svešvalodu noteicošais ir dokuments vai informācija igauņu valodā.
          </p>
          <p style="margin-top:0.5rem;">
            <strong>Alternatīvie piedāvājumi:</strong> Nav atļauti.
          </p>
          <p style="margin-top:0.5rem;">
            <strong>Dalībnieku loks:</strong> Var piedalīties tikai pretendenti no Igaunijas, citām ES/EEZ valstīm vai PTO valsts iepirkumu nolīguma dalībvalstīm.
          </p>
          <div class="orig-block">
            <div class="orig-header" onclick="toggleOrig(this)"><span>Skatīt oriģinālu igauņu valodā (RHAD Üldosa p. 1-13)</span> <span>▼</span></div>
            <div class="orig-content">
              RHAD – riigihanke alusdokumendid, mis koosnevad käesolevas failis olevast põhitekstist koos selle lisadega ja e-riigihangete keskkonnas asuvatest hanketeatest (HT), veebivormidest ning allalaetavatest failidest... Riigihange ei ole ühe menetluse raames osadeks jaotatud... Eestikeelse ja võõrkeelse dokumendi/teabe vastuolu korral lähtutakse eestikeelsest dokumendist/teabest. Alternatiivsete lahenduste esitamine ei ole lubatud.
            </div>
          </div>
        </div>

        <div class="para-item">
          <h4>2. Piedāvājuma noformēšana</h4>
          <p>
            Visi dokumenti jāiesniedz elektroniski RHR vidē (https://riigihanked.riik.ee). Piedāvājums tiek noformēts igauņu valodā (citvalodu dokumentiem obligāts tulkojums). Pretendents sedz visas sagatavošanas izmaksas. Pretendentu apvienībai obligāti jāiesniedz pilnvarotā pārstāvja pilnvara, kas derīga līdz līguma izpildei. Piedāvājums ir konfidenciāls līdz uzvarētāja paziņošanai.
          </p>
        </div>

        <div class="para-item">
          <h4>3. Piedāvājuma maksumus</h4>
          <p>
            Pretendents iesniedz vienotu darba stundas likmi RHR veidlapā. Piedāvātā stundas likme ir galīga un ietver visus nodokļus un nodevas, izņemot PVN. Nekādi papildu izdevumi netiek apmaksāti.
          </p>
        </div>

        <div class="para-item">
          <h4>4. Piedāvājumu noraidīšana un procedūras atcelšana</h4>
          <p>
            Pasūtītājs noraida neatbilstošus piedāvājumus, kā arī patur tiesības atcelt iepirkumu, ja mainās organizācijas mērķi un prioritātes, ja vadība pieņem atbilstošu lēmumu vai ja par atbilstošu tiek atzīts tikai viens piedāvājums.
          </p>
        </div>

        <div class="para-item">
          <h4>5. Vērtēšana</h4>
          <p>
            Līgums tiek slēgts ar saimnieciski visizdevīgāko piedāvājumu (labākā cenas un kvalitātes attiecība). Ja atbilstošs ir tikai 1 piedāvājums, pasūtītājam ir tiesības piešķirt maksimālos punktus bez saturiskas salīdzināšanas.
          </p>
        </div>
      </section>

      <!-- SECTION 2: LISA 1 -->
      <section id="lisa-1" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Tehniskā specifikācija</span>
            <span class="badge badge-purple">Headless Directus CMS</span>
            <span class="badge badge-success">Kubernetes Riigipilv</span>
          </div>
          <h2>2. Pielikums 1 – Vispārīgās vienošanās tehniskais apraksts</h2>
          <p class="section-subtitle">Tehnoloģiskā arhitektūra, darbu apjoms, SLA reakcijas laiki un prasības komandas kvalifikācijai.</p>
        </div>

        <h3>1. Fona informācija un esošā situācija</h3>
        <p style="margin-bottom:1rem;">
          Pasūtītājs pārvalda daudzas vietnes ar dažādu zīmolvedību (eis.ee, burger.eis.ee, tradewithestonia.com, investinestonia.com, workinestonia.com, visitestonia.com, estonia.ee, brand.estonia.ee un divas Laravel rezervāciju sistēmas). Esošās WordPress un Laravel sistēmas ir sasniegušas sava dzīves cikla beigas (end-of-life). Tehniskā arhitektūra ir novecojusi un kavē mērogošanu. Mērķis ir piesaistīt ilgtermiņa partneri jaunas platformas izveidei un esošo vietņu migrācijai.
        </p>

        <h3>2. Nākotnes tehnoloģiskā platforma</h3>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; line-height: 1.7;">
          <li><strong>Backend Headless CMS:</strong> Izvēlēta sistēma <strong>Directus</strong> (https://directus.com), nodrošinot satura vadības pilnīgu atdalīšanu no prezentācijas slāņa, universālus satura blokus un REST/GraphQL API.</li>
          <li><strong>Frontend:</strong> <strong>React un Next.js App Router</strong> arhitektūra ar <strong>TypeScript</strong> un <strong>shadcn/ui</strong> komponentēm.</li>
          <li><strong>Izvietošanas vide:</strong> Igaunijas Valsts mākonis (<strong>Riigipilv</strong>), darbinot lietotnes <strong>Kubernetes</strong> klasteros.</li>
          <li><strong>Darbplūsma:</strong> Pilnīgs <strong>GitOps</strong> modelis ar <strong>GitLab CI</strong> un <strong>ArgoCD</strong> automatizācijai un versiju kontrolei.</li>
          <li><strong>Dizains:</strong> Igaunijas Zīmola digitālā dizaina sistēma (<strong>Eesti Brändi DDS 2.0</strong>).</li>
        </ul>

        <h3>3. Pasūtījumu veikšana un procesi</h3>
        <p style="margin-bottom:1rem;">
          Vispārīgā vienošanās tiek noslēgta ar <strong>VIENU izpildītāju</strong> bez mini-konkursiem. Konkrētie darbi tiek definēti Atlassian Jira biļetēs, saskaņojot darba stundu apjomu un termiņus. Stundas likme pasūtījumos nedrīkst pārsniegt piedāvāto pamatlikmi. Izstrādē tiek piemērots Agile process (sprinti, ikdienas sanāksmes, demo), Confluence dokumentācija, OWASP ASVS drošības standarti, Clean Code principi, automatizētie testi un aizliegums glabāt paroles repozitorijos.
        </p>

        <h3>4. SLA un pakalpojuma pieejamības līmeņi</h3>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width:20%;">Prioritāte</th>
                <th style="width:40%;">Apraksts</th>
                <th style="width:20%;">Reakcijas laiks</th>
                <th style="width:20%;">Atrisināšanas laiks</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><span class="badge badge-danger">Kritiskā (Critical)</span></td>
                <td>Kritisko komponenšu bojājums vai incidents, kas aptur visas organizācijas vai klientu darbu; alternatīvu nav.</td>
                <td>Nekavējoties pēc paziņojuma (arī telefoniski)</td>
                <td>Līdz 1 darba dienai (ne vēlāk kā nākamajā darbdienā)</td>
              </tr>
              <tr>
                <td><span class="badge badge-warning">Augstā (High)</span></td>
                <td>Būtisku komponenšu bojājums, kas traucē lielas lietotāju grupas darbu; ir pagaidu risinājumi ar ietekmi uz ātrumu.</td>
                <td>Nekavējoties pēc paziņojuma</td>
                <td>Līdz 5 darba dienām</td>
              </tr>
              <tr>
                <td><span class="badge badge-primary">Vidējā (Medium)</span></td>
                <td>Kļūda vai incidents, kas ierobežo kopīgos resursus, bet pamatfunkcionalitāte darbojas.</td>
                <td>Līdz 4 darba stundu laikā</td>
                <td>Līdz 10 darba dienām</td>
              </tr>
              <tr>
                <td><span class="badge badge-muted">Zemā (Low)</span></td>
                <td>Kļūda vai nepilnība, kas mazina ērtumu, bet netraucē pamatfunkciju izmantošanai.</td>
                <td>Līdz 2 darba dienām</td>
                <td>Līdz 10 darba dienām</td>
              </tr>
            </tbody>
          </table>
        </div>

        <p style="margin-top:0.75rem;">
          <strong>Drošības ievainojamības:</strong> Kritiskās drošības nepilnības jānovērš <strong>līdz 7 kalendārajām dienām</strong>; augsta riska ievainojamības – <strong>līdz 30 kalendārajām dienām</strong>.
        </p>
        <p style="margin-top:0.5rem; color:var(--danger); font-weight:600;">
          * Svarīga sankcija par testēšanu: Sākot no otrās atkārtotās testēšanas, pasūtītājam ir tiesības izrakstīt rēķinu izpildītājam par testēšanas stundām un ekspertu izdevumiem!
        </p>

        <h3 style="margin-top:2rem;">5. Drošības prasības</h3>
        <p>
          Izstrādes un testa vidēs stingri aizliegts izmantot reālus personas datus. Piekļuvei pasūtītāja vidēm obligāta daudzfaktoru autentifikācija (MFA), lomu modelis (RBAC) un darbību žurnālu uzturēšana. Drošības incidentu gadījumā jāziņo 24 stundu laikā.
        </p>

        <h3 style="margin-top:2rem;">6. Komandas lomas un kvalifikācijas prasības</h3>
        <p style="margin-bottom:1rem;">
          Pretendentam jānodrošina šādas 6 obligātās speciālistu lomas visā līguma laikā (vismaz uz 12 secīgiem mēnešiem bez nesaskaņotas maiņas):
        </p>
        <ul style="margin-left:1.5rem; line-height:1.7;">
          <li><strong>IT projektu vadītājs:</strong> 24 mēnešu PM pieredze pēdējos 5 gados; vadīti vismaz 2 izstrādes projekti (katrs min 80 stundas) pēdējos 3 gados.</li>
          <li><strong>2x Front-end izstrādātāji:</strong> Tailwind, JS, TypeScript, React, Next.js, HTML, PHP, Git; pēdējos 3 gados vismaz 2 projekti un min 800 stundas katram.</li>
          <li><strong>2x Full-stack izstrādātāji:</strong> Docker, Kubernetes, PostgreSQL, Node.js, REST, Tailwind, React, Next.js, PHP, Git; pēdējos 3 gados vismaz 3 projekti un min 800 stundas katram.</li>
          <li><strong>Sistēmu / biznesa analītiķis:</strong> Igauņu valoda B2; pēdējos 3 gados vismaz 3 projekti (min 1 biznesa procesu modelēšana, piem., Enterprise Architect), kopā min 500 stundas.</li>
          <li><strong>UX/UI dizaineris:</strong> 24 mēnešu UX pieredze pēdējos 5 gados; pēdējos 3 gados vismaz 2 projekti ar WCAG 2.0 AA standartu.</li>
          <li><strong>Testētājs:</strong> Igauņu valoda B2; pēdējos 3 gados vismaz 2 izstrādes projekti.</li>
        </ul>
        <p style="margin-top:0.75rem;">
          <em>* Viena persona drīkst pildīt vairākas lomas. Pakalpojums jānodrošina igauņu valodā (B2). Nomaiņa tikai ar 1 mēneša iepriekšēju saskaņošanu.</em>
        </p>
      </section>

      <!-- SECTION 3: LISA 1.1 CV FORMA -->
      <section id="cv-forma" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Veidne</span>
            <span class="badge badge-muted">RHAD Lisa 1 Lisa 1.1</span>
          </div>
          <h2>3. Pielikums 1.1 – Komandas locekļa CV obligātā veidne</h2>
          <p class="section-subtitle">Visiem pieteiktajiem speciālistiem dzīvesgājumi obligāti jāiesniedz uz šīs veidlapas igauņu valodā.</p>
        </div>

        <div style="background:#fff; border:1px solid var(--border); border-radius:var(--radius-sm); padding:1.5rem;">
          <h4 style="border-bottom:1px solid var(--border); padding-bottom:0.5rem; margin-bottom:1rem;">1. Pamatinformācija par personu</h4>
          <p><strong>Lomas nosaukums (Rolli nimetus):</strong> [IT projektijuht / Front-end arendaja / Full-stack arendaja / Süsteemi- ja/või ärianalüütik / UX/UI disainer / Testija]</p>
          <p><strong>Vārds un uzvārds (Ees- ja perekonnanimi):</strong> [Vārds Uzvārds]</p>

          <h4 style="border-bottom:1px solid var(--border); padding-bottom:0.5rem; margin:1.5rem 0 1rem 0;">2. Valodu prasmes (Keeleoskus)</h4>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Valoda</th>
                  <th>Runāšanas prasme (Kõneoskus)</th>
                  <th>Rakstīšanas prasme (Kirjaoskus)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Igauņu valoda (Eesti keel)</td>
                  <td>[B2 / C1 / C2 / Emakeel]</td>
                  <td>[B2 / C1 / C2 / Emakeel]</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h4 style="border-bottom:1px solid var(--border); padding-bottom:0.5rem; margin:1.5rem 0 1rem 0;">3. Darba pieredze (Töökogemus)</h4>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Darba devējs (Tööandja)</th>
                  <th>Periods (kk.aaaa - kk.aaaa)</th>
                  <th>Amats un galvenie pienākumi</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>[Uzņēmuma nosaukums]</td>
                  <td>[01.2023 - šobrīd]</td>
                  <td>[Amata nosaukums un īss apraksts]</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h4 style="border-bottom:1px solid var(--border); padding-bottom:0.5rem; margin:1.5rem 0 1rem 0;">4. Dalība programmatūras izstrādes projektos (Osalemine tarkvaraarenduse projektides)</h4>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th style="width:30%;">Lauks</th>
                  <th style="width:70%;">Informācija par projektu</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Projekta nosaukums un iepirkuma Nr.</td>
                  <td>[Projekta nosaukums un publiskā iepirkuma atsauces numurs, ja attiecināms]</td>
                </tr>
                <tr>
                  <td>Loma projektā</td>
                  <td>[Speciālista loma: izstrādātājs, analītiķis, dizaineris utt.]</td>
                </tr>
                <tr>
                  <td>Projekta un veikto darbu apraksts</td>
                  <td>[Detalizēts apraksts par izstrādātajām funkcijām un personas ieguldījumu]</td>
                </tr>
                <tr>
                  <td>Izmantotās tehnoloģijas</td>
                  <td>[React, Next.js, TypeScript, Tailwind, Docker, PostgreSQL, REST, GraphQL, WCAG AA utt.]</td>
                </tr>
                <tr>
                  <td>Nostrādātās darba stundas pēdējos 36 mēn.</td>
                  <td>[Stundu skaits: min 80h / 500h / 800h atkarībā no lomas]</td>
                </tr>
                <tr>
                  <td>Pasūtītāja kontaktpersona atsauksmēm</td>
                  <td>[Vārds, uzvārds, amats, e-pasts, tālrunis datu verifikācijai]</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- SECTION 4: LISA 2 -->
      <section id="lisa-2" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Vērtēšana</span>
            <span class="badge badge-purple">100 Punktu Skala</span>
          </div>
          <h2>4. Pielikums 2 – Vērtēšanas kritēriji un vērtēšanas metodika</h2>
          <p class="section-subtitle">Detalizētas vērtēšanas formulas, punktu sadalījums un komisijas kvalitatīvā vērtējuma rubrika.</p>
        </div>

        <div class="kpi-grid">
          <div class="kpi-card">
            <span class="kpi-label">Stundas likme (Cena)</span>
            <span class="kpi-value">20 Punkti</span>
            <span class="kpi-desc">Zemākā cena saņem 20p; slieksnis min 60 €/h</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Pārbaudes darbs (Proovitöö)</span>
            <span class="kpi-value">80 Punkti</span>
            <span class="kpi-desc">Komisijas vērtējums 5 apakškritērijos</span>
          </div>
        </div>

        <h3 style="margin-top:1.5rem;">Cenas vērtēšanas formula (20 punkti)</h3>
        <p style="margin-bottom:1rem;">
          <code>Punkti = 20 - ((Piedāvājuma likme - Zemākā likme) / Lielākā likme) * 20</code><br>
          <em>* Visas stundas likmes, kas ir zemākas par 60,00 EUR bez PVN, vērtēšanā tiek pielīdzinātas 60,00 EUR. Zemākas likmes piedāvāšana nedod nekādu papildu priekšrocību.</em>
        </p>

        <h3 style="margin-top:2rem;">Pārbaudes darba 5 apakškritēriji (80 punkti)</h3>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width:30%;">Apakškritērijs</th>
                <th style="width:12%;">Max punkti</th>
                <th style="width:58%;">Vērtēšanas līmeņi un apraksts</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. Analītiskā loģika un struktūra</strong></td>
                <td><span class="badge badge-primary">20 p</span></td>
                <td>
                  <strong>20p:</strong> Labākā analītiskā loģika; problēmas nostādne skaidra, pieņēmumi pamatoti, vienots ietvars.<br>
                  <strong>15p:</strong> Nedaudz vājāks, maznozīmīgi trūkumi.<br>
                  <strong>10p:</strong> Skaidri vājāks, manāmi trūkumi saskaņotībā.<br>
                  <strong>5p:</strong> Būtiski vājāks, sadrumstalots.<br>
                  <strong>1p:</strong> Neatbalsta mērķu sasniegšanu.
                </td>
              </tr>
              <tr>
                <td><strong>2. UX lietotāja ceļu izpildāmība un mērogojamība</strong></td>
                <td><span class="badge badge-primary">20 p</span></td>
                <td>
                  <strong>20p:</strong> Vislabākais UX; reālistisks, mērogojams un atbalsta biznesa procesus.<br>
                  <strong>15p:</strong> Nelieli trūkumi, kopumā labi mērogojams.<br>
                  <strong>10p:</strong> Manāmi trūkumi izpildāmībā.<br>
                  <strong>5p:</strong> Mērķus atbalsta tikai ierobežotā apjomā.<br>
                  <strong>1p:</strong> Vājākais UX risinājums.
                </td>
              </tr>
              <tr>
                <td><strong>3. DDS 2.0 dizaina sistēmas pielietojums</strong></td>
                <td><span class="badge badge-purple">10 p</span></td>
                <td>
                  <strong>10p:</strong> Viskonsekventāk un kvalitatīvāk ievēroti DDS 2.0 dizaina sistēmas noteikumi.<br>
                  <strong>8p:</strong> Nedaudz vājāks, maznozīmīgas nepilnības.<br>
                  <strong>5p:</strong> Pamanāmi trūkumi konsekvencē.<br>
                  <strong>1p:</strong> Būtiski trūkumi; neatbalsta mērķus.
                </td>
              </tr>
              <tr>
                <td><strong>4. Tehniskā realizācija un arhitektūra</strong></td>
                <td><span class="badge badge-primary">20 p</span></td>
                <td>
                  <strong>20p:</strong> Vislabākais izpildījums (Next.js, Directus, Docker compose, koda kvalitāte, datu modeļi, testi).<br>
                  <strong>15p:</strong> Nelieli trūkumi, kopumā kvalitatīvs.<br>
                  <strong>10p:</strong> Manāmi trūkumi prasību izpildē.<br>
                  <strong>5p:</strong> Nopietni trūkumi.<br>
                  <strong>1p:</strong> Kritiski trūkumi; vājākais kods.
                </td>
              </tr>
              <tr>
                <td><strong>5. Video prezentācija (max 10 min)</strong></td>
                <td><span class="badge badge-purple">10 p</span></td>
                <td>
                  <strong>10p:</strong> Vislabākā prezentācija; skaidra, strukturēta, saprotama gan tehniskam, gan biznesa vērtētājam.<br>
                  <strong>8p:</strong> Nelieli trūkumi raitumā.<br>
                  <strong>5p:</strong> Pamanāmi trūkumi, daļēji apgrūtināta izpratne.<br>
                  <strong>1p:</strong> Būtiski trūkumi; nepilda mērķi.
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout callout-warning">
          <div class="callout-title">⚖️ Vienādu punktu noteikums:</div>
          <p>
            Ja diviem vai vairākiem pretendentiem kopējais punktu skaits ir vienāds, <strong>uzvar tas, kuram ir augstāks vērtējums Pārbaudes darbā (Proovitöö)</strong>! Ja arī pēc tam punkti sakrīt, tiek rīkota lozēšana.
          </p>
        </div>
      </section>

      <!-- SECTION 5: LISA 3 LĪGUMS -->
      <section id="lisa-3" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Līguma projekts</span>
            <span class="badge badge-muted">RHAD Lisa 3.docx</span>
          </div>
          <h2>5. Pielikums 3 – Vispārīgās vienošanās līgums (Raamleping)</h2>
          <p class="section-subtitle">Juridiskie noteikumi, pasūtījumu veikšana, pieņemšana, apmaksa, intelektuālais īpašums, garantija un sankcijas.</p>
        </div>

        <div class="para-item">
          <h4>1. Dokumentu hierarhija un prioritāte</h4>
          <p>Pretrunu gadījumā spēkā ir šāda dokumentu secība: 1) Līgums; 2) Iepirkuma nolikums (RHAD); 3) Pretendenta piedāvājums.</p>
        </div>

        <div class="para-item">
          <h4>2. Līguma termiņš</h4>
          <p>Līgums ir spēkā 36 kalendāros mēnešus vai līdz maksimālās summas 750 000,00 EUR sasniegšanai. Konkrēto pasūtījumu (izpildes līgumu) darbība var turpināties līdz 12 mēnešiem pēc vispārīgās vienošanās beigām.</p>
        </div>

        <div class="para-item">
          <h4>3. Pasūtījumu veikšana caur Jira</h4>
          <p>Darbi tiek pasūtīti bez mini-konkursiem. Pasūtījums tiek reģistrēts Jira biļetē, izpildītājs novērtē stundas, un puses saskaņo apjomu pirms darbu uzsākšanas. Stundas likme nedrīkst pārsniegt līgumā nolīgto likmi.</p>
        </div>

        <div class="para-item">
          <h4>4. Pieņemšana un nodošana</h4>
          <p>Nodevumi tiek nodoti testēšanas vidē. Pasūtītājam ir 10 darba dienas pārbaudei. Pēc otrās atkārtotās testēšanas pasūtītājam ir tiesības izrakstīt rēķinu izpildītājam par testēšanas stundām.</p>
        </div>

        <div class="para-item">
          <h4>5. Norēķinu kārtība</h4>
          <p>Apmaksa reizi mēnesī pēc faktiski pieņemtajām stundām un Jira atskaites. Apmaksas termiņš – 21 kalendārā diena no rēķina saņemšanas.</p>
        </div>

        <div class="para-item">
          <h4>6. Intelektuālais īpašums (Autortiesības)</h4>
          <p>Visas mantiskās autortiesības uz radīto kodu, dokumentāciju un datubāzēm pāriet pasūtītājam visā pasaulē uz visu autortiesību termiņu bez papildu maksas. Pasūtītājs drīkst kodu brīvi publicēt ar MIT licenci.</p>
        </div>

        <div class="para-item">
          <h4>7. Garantija (24 mēneši)</h4>
          <p>Garantijas termiņš visiem darbiem ir 24 mēneši no pieņemšanas dienas. Kļūdas garantijas laikā tiek novērstas bez maksas saskaņā ar SLA termiņiem.</p>
        </div>

        <div class="para-item">
          <h4>8. Atbildība un sankcijas</h4>
          <p>Nokavējuma nauda par termiņu kavējumu: 0,1% dienā no uzdevuma vērtības vai 50,00 EUR par katru nokavēto dienu. Līgumsods par būtiskiem pārkāpumiem: līdz 10%. Kopējais sankciju limits: 20% no pasūtījuma vērtības.</p>
        </div>

        <div class="para-item">
          <h4>9. Līguma vienpusēja izbeigšana</h4>
          <p>Pasūtītājs var vienpusēji lauzt līgumu, brīdinot 30 dienas iepriekš, vai nekavējoties būtiska pārkāpuma gadījumā (termiņu kavējums virs 20 dienām, atkārtots brāķis, sankciju pārkāpums).</p>
        </div>
      </section>

      <!-- SECTION 6: GDPR -->
      <section id="gdpr" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Datu aizsardzība</span>
            <span class="badge badge-purple">GDPR / VDAR</span>
          </div>
          <h2>6. Pielikums 3.1 – Datu apstrādes līgums (Andmetöötluse leping)</h2>
          <p class="section-subtitle">Personas datu apstrādes noteikumi, drošības pasākumi un pārkāpumu paziņošanas kārtība.</p>
        </div>

        <p style="margin-bottom:1rem;">
          EIS darbojas kā <strong>Datu pārzinis (Vastutav töötleja)</strong>, bet Izpildītājs ir <strong>Datu apstrādātājs (Volitatud töötleja)</strong>. Izpildītājs personas datus drīkst apstrādāt tikai un vienīgi saskaņā ar pasūtītāja dokumentētiem norādījumiem.
        </p>

        <ul style="margin-left:1.5rem; line-height:1.7;">
          <li><strong>Tehniskie pasākumi:</strong> Piekļuves kontrole, personificēti konti, MFA, šifrēšana (TLS 1.3), darbību auditācija un žurnālēšana.</li>
          <li><strong>Testa vides:</strong> Stingri aizliegts izmantot reālus personas datus izstrādes un testa vidēs (jāizmanto pseidonimizēti vai sintētiski dati).</li>
          <li><strong>Pārkāpumu paziņošana:</strong> Par jebkuru personas datu drošības pārkāpumu vai incidentu jāpaziņo pasūtītājam <strong>ne vēlāk kā 24 stundu laikā</strong>.</li>
          <li><strong>Datu iznīcināšana:</strong> Pēc līguma izbeigšanās visi pasūtītāja personas dati un to kopijas pēc pasūtītāja izvēles ir pilnībā jāizdzēš vai jānodod atpakaļ.</li>
        </ul>
      </section>

      <!-- SECTION 7: LISA 4 PROOVITOO -->
      <section id="lisa-4" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-purple">Vērtējamais pārbaudes darbs</span>
            <span class="badge badge-primary">80 Punktu Svars</span>
            <span class="badge badge-success">Next.js + Directus</span>
          </div>
          <h2>7. Pielikums 4 – Pārbaudes uzdevums (Proovitöö lähteülesanne)</h2>
          <p class="section-subtitle">Praktiskā uzdevuma darba uzdevums: klienta ceļvedis no eis.ee sākumlapas līdz pakalpojumu lapām.</p>
        </div>

        <div class="callout callout-purple">
          <div class="callout-title">🎯 Pārbaudes darba uzdevuma mērķis</div>
          <p>
            Novērtēt pretendenta spēju analizēt, dizainēt, modelēt un tehniski realizēt risinājumu, kas nodrošina lietotāja ceļu no EIS sākumlapas līdz pakalpojuma lapai (Homepage ➔ Category Page ➔ 3 Service Pages), izmantojot <strong>Directus Headless CMS</strong>, <strong>Next.js App Router</strong>, <strong>DDS 2.0 dizainu</strong> un <strong>Docker Compose</strong>.
          </p>
        </div>

        <h3>Uzdevuma izejas lapu paraugi (Live vietne eis.ee)</h3>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width:25%;">Lapas tips</th>
                <th style="width:75%;">Saite uz reālo saturu</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Sākumlapa (Avaleht)</strong></td>
                <td><a href="https://eis.ee" target="_blank" rel="noopener">https://eis.ee</a></td>
              </tr>
              <tr>
                <td><strong>Kategorijas lapa</strong></td>
                <td><a href="https://eis.ee/innoveeri-ja-kaitse-ari/" target="_blank" rel="noopener">https://eis.ee/innoveeri-ja-kaitse-ari/</a></td>
              </tr>
              <tr>
                <td><strong>Pakalpojuma lapa 1</strong></td>
                <td><a href="https://eis.ee/teenused/digitaliseerimise-teekaardi-arendustegevused-toetus/" target="_blank" rel="noopener">Digitalizācijas ceļa kartes atbalsts</a></td>
              </tr>
              <tr>
                <td><strong>Pakalpojuma lapa 2</strong></td>
                <td><a href="https://eis.ee/teenused/laenukaendus-2/" target="_blank" rel="noopener">Aizdevuma garantija</a></td>
              </tr>
              <tr>
                <td><strong>Pakalpojuma lapa 3</strong></td>
                <td><a href="https://eis.ee/teenused/tark-tellija" target="_blank" rel="noopener">Viedais pasūtītājs (Tark tellija)</a></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3 style="margin-top:2rem;">Obligātās funkcionālās un tehniskās prasības</h3>
        <div class="kpi-grid">
          <div class="kpi-card" style="background:#fff;">
            <strong>Next.js App Router</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Frontend jārealizē ar Next.js App Router, React un TypeScript, izmantojot servera puses datu ielādi un renderēšanu (SSR).
            </p>
          </div>
          <div class="kpi-card" style="background:#fff;">
            <strong>Directus Headless CMS</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Pilnīgi atdalīts backend; saziņa caur Directus SDK, REST vai GraphQL API. Dinamiskas lapas, SEO metadati un mediju pārvaldība.
            </p>
          </div>
          <div class="kpi-card" style="background:#fff;">
            <strong>AI atbalsts caur MCP slāni</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Risinājumam jānodrošina mākslīgā intelekta rīku atbalsts, izmantojot Model Context Protocol (MCP) arhitektūru.
            </p>
          </div>
          <div class="kpi-card" style="background:#fff;">
            <strong>Palaišana ar 1 komandu</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Frontend + Directus + Datubāze darbojas konteineros un obligāti startējas ar komandu: <code>docker compose up</code>.
            </p>
          </div>
        </div>

        <h3 style="margin-top:2rem;">4 Iesniedzamie materiāli un piegādes veids</h3>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width:25%;">Nodevums</th>
                <th style="width:30%;">Formāts</th>
                <th style="width:45%;">Piegādes nosacījumi</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. Koncepcijas apraksts</strong></td>
                <td>Dokuments līdz 10 lappusēm (PDF)</td>
                <td>Problēmas izpratne, arhitektūra, datu modeļi, UX loģika.</td>
              </tr>
              <tr>
                <td><strong>2. Figma prototips</strong></td>
                <td>Klikšķināma Figma saite</td>
                <td>Izstrādāts, balstoties uz DDS 2.0 (💎 DDS 2.0 - WIP) komponentēm.</td>
              </tr>
              <tr>
                <td><strong>3. Funkcionējošs kods</strong></td>
                <td>GitHub repozitorijs</td>
                <td>Jādod piekļuve lietotājiem <code>martinroos-eis</code> un <code>rvaher</code>. Pilna commit vēsture.</td>
              </tr>
              <tr>
                <td><strong>4. Video prezentācija</strong></td>
                <td>YouTube nereģistrēta (unlisted) saite</td>
                <td>Maksimums 10 minūtes. Risinājuma demonstrācija un arhitektūras pamatojums.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

""" + PROOVITOO_STRATEGY_HTML + """

      <!-- SECTION 8: LISA 5 CFR PRASĪBAS -->
      <section id="lisa-5" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Tehniskais standarts</span>
            <span class="badge badge-purple">110 CFR Prasības</span>
            <span class="badge badge-success">Meklētājs un filtri</span>
          </div>
          <h2>8. Pielikums 5 – Šķērsfunkcionālās prasības izstrādēm (CFR)</h2>
          <p class="section-subtitle">Pilns 110 šķērsfunkcionālo tehnisko prasību katalogs (arhitektūra, drošība, koda standarti, AI vadlīnijas CFR-102..108).</p>
        </div>

        <!-- Filter bar -->
        <div class="filter-bar">
          <button class="filter-chip active" onclick="filterCFR('ALL', this)">Visi (110)</button>
          <button class="filter-chip" onclick="filterCFR('Izstrāde', this)">Izstrāde</button>
          <button class="filter-chip" onclick="filterCFR('Arhitektūra', this)">Arhitektūra</button>
          <button class="filter-chip" onclick="filterCFR('Datu pārvaldība', this)">Datu pārvaldība</button>
          <button class="filter-chip" onclick="filterCFR('Drošība', this)">Drošība</button>
          <button class="filter-chip" onclick="filterCFR('Kvalitāte', this)">Kvalitāte</button>
          <button class="filter-chip" onclick="filterCFR('Piegāde (CI/CD)', this)">CI / CD</button>
          <button class="filter-chip" onclick="filterCFR('Vispārīgās / AI', this)">AI Vadlīnijas</button>
          
          <div class="search-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="cfrSearchInput" class="search-input" placeholder="Meklēt prasību pēc koda vai atslēgvārda..." oninput="searchCFR()">
          </div>
        </div>

        <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;" id="cfrCountDisplay">
          Rāda 110 no 110 prasībām
        </div>

        <!-- CFR Table -->
        <div class="table-container">
          <table id="cfrTable">
            <thead>
              <tr>
                <th style="width:12%;">Prasības ID</th>
                <th style="width:14%;">Obligātums</th>
                <th style="width:16%;">Kategorija</th>
                <th style="width:58%;">Prasības nosaukums un apraksts (Latviešu valodā)</th>
              </tr>
            </thead>
            <tbody id="cfrTableBody">
              <!-- Dynamically populated from JS -->
            </tbody>
          </table>
        </div>
      </section>

      <!-- SECTION 9: VASTAVUSTINGIMUSED -->
      <section id="vastavus" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">Kvalifikācija</span>
            <span class="badge badge-muted">315313_vastavustingimused.pdf</span>
          </div>
          <h2>9. Atbilstības un kvalifikācijas nosacījumi (RHR Reģistrs)</h2>
          <p class="section-subtitle">Oficiālie e-iepirkumu vides deklarāciju jautājumi un apliecinājumi.</p>
        </div>

        <div class="para-item">
          <h4>1. Sankcijas pret Krieviju un Baltkrieviju</h4>
          <p>Pretendents apliecina, ka nepiesaistīs vairāk par 10% no līguma apjoma apakšuzņēmējus vai piegādātājus, kuri ir Krievijas Federācijas pilsoņi, rezidenti vai Krievijā reģistrēti uzņēmumi (ES Padomes Regula 2022/576).</p>
        </div>

        <div class="para-item">
          <h4>2. Apvienības pilnvara</h4>
          <p>Kopīga piedāvājuma gadījumā jānorāda visu dalībnieku pilnvarotais pārstāvis un jāpievieno parakstīta pilnvara.</p>
        </div>

        <div class="para-item">
          <h4>3. Komerciālais noslēpums</h4>
          <p>Pretendents deklarē informāciju, kas uzskatāma par komercnoslēpumu. Cena (stundas likme) nedrīkst būt komercnoslēpums.</p>
        </div>

        <div class="para-item">
          <h4>4. Pilnīgs atbilstības apliecinājums</h4>
          <p>Iesniedzot piedāvājumu, pretendents apliecina pilnīgu visu iepirkuma pamatdokumentos izvirzīto prasību pārņemšanu bez atrunām.</p>
        </div>

        <div class="para-item">
          <h4>5. Ekvivalence</h4>
          <p>Apliecinājums par līdzvērtīgumu un pierādījumu pievienošana gadījumos, kad piedāvāts līdzvērtīgs risinājums.</p>
        </div>

        <div class="para-item">
          <h4>6. Komandas CV iesniegšana</h4>
          <p>Obligāta CV pievienošana 6 lomām uz 1.1 veidlapas: IT projektu vadītājs, 2x Frontend izstrādātāji, 2x Full-stack izstrādātāji, Analītiķis, UX/UI dizaineris, Testētājs.</p>
        </div>

        <div class="para-item">
          <h4>7. Pārbaudes darba iesniegšana</h4>
          <p>Pārbaudes darba materiālu (koncepcijas dokuments, Figma prototipa saite, GitHub repozitorijs, YouTube video) iesniegšana RHR reģistrā pirms termiņa beigām.</p>
        </div>
      </section>

      <!-- SECTION 10: HINDAMISKRITEERIUMID -->
      <section id="hindamine" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">RHR Sistēma</span>
            <span class="badge badge-muted">315313_hindamiskriteeriumid.pdf</span>
          </div>
          <h2>10. Vērtēšanas kritēriju oficiālais RHR izraksts</h2>
          <p class="section-subtitle">E-iepirkumu sistēmas konfigurācija un kritēriju svēršanas algoritmi.</p>
        </div>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width:8%;">Nr.</th>
                <th style="width:30%;">Nosaukums</th>
                <th style="width:12%;">Svars</th>
                <th style="width:20%;">Tips</th>
                <th style="width:30%;">Aprēķina apraksts</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td><strong>Izstrādes un uzturēšanas stundas likme (bez PVN)</strong></td>
                <td><span class="badge badge-primary">20 %</span></td>
                <td>Cena – mazākā ir labākā</td>
                <td>Formula: Svars - (Likme - MinLikme) / MaxLikme * Svars. Likmes zem 60 EUR/h tiek pielīdzinātas 60 EUR.</td>
              </tr>
              <tr>
                <td>2</td>
                <td><strong>Pārbaudes darbs (Proovitöö)</strong></td>
                <td><span class="badge badge-purple">80 %</span></td>
                <td>Kvalitāte – vērtē komisija</td>
                <td>Vērtē vērtēšanas komisija 5 apakškritērijos saskaņā ar RHAD 2. pielikumu.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- SECTION 11: HANKEPASS (ESPD) -->
      <section id="hankepass" class="doc-section">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-primary">ESPD / Hankepass</span>
            <span class="badge badge-muted">315313_hankepass.pdf & XML</span>
          </div>
          <h2>11. Iepirkuma pase (ESPD) un skaidrojumi</h2>
          <p class="section-subtitle">Eiropas vienotā iepirkuma procedūras dokumenta prasības un pašdeklarācija.</p>
        </div>

        <p style="margin-bottom:1rem;">
          Hankepass (ESPD) ir pretendenta pašdeklarācija, kas apliecina, ka uz uzņēmumu neattiecas izslēgšanas iemesli un tas atbilst kvalifikācijas prasībām.
        </p>

        <div class="kpi-grid">
          <div class="kpi-card" style="background:#fff;">
            <strong>I Daļa: Informācija par iepirkumu</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              EIS paziņojums, atsauces numurs 315313, CPV kods 72262000-9 (Programmatūras izstrādes pakalpojumi).
            </p>
          </div>
          <div class="kpi-card" style="background:#fff;">
            <strong>II Daļa: Informācija par pretendentu</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Uzņēmuma rekvizīti, reģistrācijas numurs, pārstāvji, izmērs, kontaktinformācija.
            </p>
          </div>
          <div class="kpi-card" style="background:#fff;">
            <strong>III Daļa: Izslēgšanas iemesli</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Kriminālsodu neesamība, nodokļu nomaksa, maksātnespējas neesamība, profesionālā uzticamība un sankciju ievērošana.
            </p>
          </div>
          <div class="kpi-card" style="background:#fff;">
            <strong>IV Daļa: Kvalifikācija</strong>
            <p style="font-size:0.875rem; color:var(--text-muted); margin-top:0.35rem;">
              Finansiālā apgrozījuma minimums nav noteikts; kapacitāti pierāda komandas kvalifikācija (Pielikums 1) un pārbaudes darbs (Pielikums 4).
            </p>
          </div>
        </div>
      </section>

    </main>
  </div>

  <!-- Client-side Interactive Scripts -->
  <script>
    // CFR Items Dataset
    const cfrData = """ + cfr_json_str + """;

    // Populate CFR Table
    function renderCFR(items) {
      const tbody = document.getElementById('cfrTableBody');
      tbody.innerHTML = '';
      
      items.forEach(item => {
        const tr = document.createElement('tr');
        
        let typeBadge = 'badge-primary';
        if (item.type_lv === 'Obligāts') typeBadge = 'badge-danger';
        else if (item.type_lv === 'Sagaidāms') typeBadge = 'badge-primary';
        else if (item.type_lv === 'Ieteikums') typeBadge = 'badge-success';

        let catBadge = 'badge-muted';
        if (item.cat_lv.includes('AI')) catBadge = 'badge-purple';
        else if (item.cat_lv === 'Drošība') catBadge = 'badge-warning';

        tr.innerHTML = `
          <td><strong>${item.id}</strong></td>
          <td><span class="badge ${typeBadge}">${item.type_lv}</span></td>
          <td><span class="badge ${catBadge}">${item.cat_lv}</span></td>
          <td>
            <strong>${item.title_lv}</strong>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:0.25rem;">${item.desc_lv}</p>
            <div class="orig-block" style="margin-top:0.4rem;">
              <div class="orig-header" onclick="toggleOrig(this)">
                <span>Oriģināls (EE): ${item.id}</span> <span>▼</span>
              </div>
              <div class="orig-content">
                ${item.text_ee} [${item.type_ee} ${item.cat_ee}]
              </div>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      });

      document.getElementById('cfrCountDisplay').innerText = `Rāda ${items.length} no ${cfrData.length} prasībām`;
    }

    // Filter CFR by Category
    let currentCategory = 'ALL';
    function filterCFR(category, btn) {
      currentCategory = category;
      document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      applyCFRFilters();
    }

    // Search CFR
    function searchCFR() {
      applyCFRFilters();
    }

    function applyCFRFilters() {
      const query = document.getElementById('cfrSearchInput').value.toLowerCase().trim();
      let filtered = cfrData;

      if (currentCategory !== 'ALL') {
        filtered = filtered.filter(item => item.cat_lv === currentCategory);
      }

      if (query) {
        filtered = filtered.filter(item => 
          item.id.toLowerCase().includes(query) ||
          item.title_lv.toLowerCase().includes(query) ||
          item.desc_lv.toLowerCase().includes(query) ||
          item.text_ee.toLowerCase().includes(query)
        );
      }

      renderCFR(filtered);
    }

    // Toggle Single Estonian text block
    function toggleOrig(headerElem) {
      const content = headerElem.nextElementSibling;
      content.classList.toggle('open');
      const arrow = headerElem.querySelector('span:last-child');
      if (arrow) {
        arrow.innerText = content.classList.contains('open') ? '▲' : '▼';
      }
    }

    // Toggle All Originals globally
    let allOrigOpen = false;
    function toggleAllOriginals() {
      allOrigOpen = !allOrigOpen;
      const contents = document.querySelectorAll('.orig-content');
      contents.forEach(c => {
        if (allOrigOpen) c.classList.add('open');
        else c.classList.remove('open');
      });
      const btn = document.getElementById('toggleOrigBtn');
      btn.innerHTML = allOrigOpen ? '<span>🌐 Slēpt EE oriģinālu</span>' : '<span>🌐 Rādīt EE oriģinālu</span>';
    }

    // Interactive Score Calculator
    function recalcScore() {
      const priceInput = parseFloat(document.getElementById('calcPriceInput').value) || 60;
      // Below 60 EUR is equalized to 60 EUR
      const effectivePrice = Math.max(60, priceInput);
      const minPrice = 60;
      // Formula: 20 - ((effectivePrice - minPrice) / maxReferencePrice) * 20
      // In RHR, if lowest = 60, price = 60 => points = 20.00
      let pricePoints = 20.00;
      if (effectivePrice > minPrice) {
        // max assumed around 120 or proportional formula: 20 * (60 / effectivePrice)
        pricePoints = Math.max(0, 20 - ((effectivePrice - 60) / 100) * 20);
      }

      const sub1 = parseFloat(document.getElementById('sub1').value) || 0;
      const sub2 = parseFloat(document.getElementById('sub2').value) || 0;
      const sub3 = parseFloat(document.getElementById('sub3').value) || 0;
      const sub4 = parseFloat(document.getElementById('sub4').value) || 0;
      const sub5 = parseFloat(document.getElementById('sub5').value) || 0;

      const proovitooPoints = sub1 + sub2 + sub3 + sub4 + sub5;
      const totalPoints = pricePoints + proovitooPoints;

      document.getElementById('calcTotalPoints').innerText = totalPoints.toFixed(2);
      document.getElementById('calcScoreBreakdown').innerHTML = `
        Cena (${effectivePrice} €/h): <strong>${pricePoints.toFixed(2)}</strong> punkti | Pārbaudes darbs: <strong>${proovitooPoints}</strong> / 80 punkti
      `;
    }

    // Active Sidebar Scrollspy
    window.addEventListener('scroll', () => {
      const sections = document.querySelectorAll('.doc-section');
      const navLinks = document.querySelectorAll('.nav-link');
      let currentSectionId = '';

      sections.forEach(section => {
        const top = section.offsetTop - 120;
        if (window.pageYOffset >= top) {
          currentSectionId = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + currentSectionId) {
          link.classList.add('active');
        }
      });
    });

    // Initialize on load
    document.addEventListener('DOMContentLoaded', () => {
      renderCFR(cfrData);
      recalcScore();
    });
  </script>
</body>
</html>
"""

# Write index.html in the root directory
target_html = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "index.html"))
with open(target_html, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated complete application at {target_html} (Size: {os.path.getsize(target_html)} bytes)")

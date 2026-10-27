# -*- coding: utf-8 -*-
"""
Strategic Solution Guide for RHAD Lisa 4 (Proovitöö) to achieve 80/80 points.
"""

PROOVITOO_STRATEGY_HTML = """
      <!-- SECTION: PROOVITOO STRATEGY -->
      <section id="proovitoo-strategija" class="doc-section" style="border: 2px solid var(--purple); background: linear-gradient(to bottom, #ffffff, #faf7ff);">
        <div class="section-header">
          <div class="tag-row">
            <span class="badge badge-purple">Stratēģiskais ceļvedis</span>
            <span class="badge badge-success">Mērķis: 80 / 80 punkti</span>
            <span class="badge badge-primary">Next.js + Directus + MCP + DDS 2.0</span>
          </div>
          <h2>🚀 Pārbaudes darba (Proovitöö) risināšanas stratēģija</h2>
          <p class="section-subtitle">
            Kā praktiski atrisināt <strong>Pielikuma 4 uzdevumu</strong>, lai iepirkuma komisijas vērtējumā iegūtu maksimālos <strong>80 no 80 punktiem</strong>.
          </p>
        </div>

        <!-- Problem & Vision -->
        <div class="callout callout-purple">
          <div class="callout-title">💡 EIS reālā biznesa problēma, ko komisija vēlas redzēt atrisinātu</div>
          <p>
            Apvienojoties <strong>EAS</strong> un <strong>KredEx</strong> vienotajā fondā <strong>EIS</strong>, organizācijai radās simtiem dažādu atbalsta pasākumu, kas pašlaik ir izmētāti novecojušās WordPress un Laravel vietnēs. Klients apmaldās birokrātiskajos tekstos un nesaprot, kurš pakalpojums ir domāts viņam.
            <br><br>
            <strong>Uzvarošā risinājuma atslēga:</strong> Parādīt, ka Jūsu komanda spēj ne tikai programmēt, bet arī izveidot <em>intuitīvu, ātru un uz rezultātu vērstu klienta ceļu</em> ar <strong>Directus Headless CMS</strong> un <strong>Next.js</strong>, integrējot inovatīvo <strong>MCP (Model Context Protocol) AI slāni</strong>.
          </p>
        </div>

        <!-- Visual Architecture -->
        <h3 style="margin: 2rem 0 1rem 0;">1. Tehnoloģiskā arhitektūra (Pilnīga atbilstība nolikumam)</h3>
        
        <div style="background:#0f172a; color:#f8fafc; padding:1.75rem; border-radius:var(--radius); font-family:'JetBrains Mono', monospace; font-size:0.875rem; line-height:1.6; margin-bottom:2rem; overflow-x:auto;">
          <div style="color:#94a3b8; margin-bottom:0.5rem;">// SISTĒMAS ARHITEKTŪRAS SHĒMA (1-KOMANDAS PALAIŠANA: docker compose up)</div>
          <div style="color:#38bdf8;">┌────────────────────────────────────────────────────────────────────────┐</div>
          <div style="color:#38bdf8;">│                FRONTEND: Next.js 15+ (App Router)                      │</div>
          <div style="color:#cbd5e1;">│  • React, TypeScript, Tailwind CSS, shadcn/ui                          │</div>
          <div style="color:#cbd5e1;">│  • Server Components & SSR (Core Web Vitals zaļā zona)                 │</div>
          <div style="color:#cbd5e1;">│  • Eesti Brändi DDS 2.0 dizaina sistēma (WCAG 2.1 AA)                  │</div>
          <div style="color:#38bdf8;">└───────────────────────────────────▲────────────────────────────────────┘</div>
          <div style="color:#64748b; text-align:center;">                            │ REST / GraphQL API (Directus SDK)</div>
          <div style="color:#a855f7;">┌───────────────────────────────────▼────────────────────────────────────┐</div>
          <div style="color:#a855f7;">│             BACKEND: Directus Headless CMS (Port: 8055)                │</div>
          <div style="color:#cbd5e1;">│  • Universāli satura bloki (Many-to-Any Block Builder)                 │</div>
          <div style="color:#cbd5e1;">│  • Dinamiskie URL un lapu pārvaldība (/page/..., /services/...)        │</div>
          <div style="color:#cbd5e1;">│  • SEO metadati, OpenGraph, daudzvalodība (EE / EN)                   │</div>
          <div style="color:#cbd5e1;">│  • S3 mediju krātuve, RBAC tiesības, Webhook paziņojumi                │</div>
          <div style="color:#a855f7;">└─────────────────▲──────────────────────────────────────▲───────────────┘</div>
          <div style="color:#64748b; text-align:center;">                  │                                      │</div>
          <div style="display:flex; justify-content:space-around;">
            <span style="color:#10b981;">┌─────────────────▼──────────────┐</span>
            <span style="color:#f59e0b;">┌────────────────▼──────────────┐</span>
          </div>
          <div style="display:flex; justify-content:space-around;">
            <span style="color:#10b981;">│      PostgreSQL Datubāze       │</span>
            <span style="color:#f59e0b;">│      MCP AI Rīku Serviss      │</span>
          </div>
          <div style="display:flex; justify-content:space-around;">
            <span style="color:#cbd5e1;">│  (Ar gataviem seed datiem)     │</span>
            <span style="color:#cbd5e1;">│  (Model Context Protocol API) │</span>
          </div>
          <div style="display:flex; justify-content:space-around;">
            <span style="color:#10b981;">└────────────────────────────────┘</span>
            <span style="color:#f59e0b;">└───────────────────────────────┘</span>
          </div>
        </div>

        <!-- 2. UX User Flow -->
        <h3 style="margin: 2rem 0 1rem 0;">2. Klienta ceļvedis (UX Flow): No Sākumlapas līdz Pakalpojumam</h3>
        <p style="margin-bottom:1.25rem;">
          Pielikumā 4 noteikts, ka ceļam jāsākas EIS sākumlapā, jāietver vismaz 1 kategorijas lapa un 3 konkrēti pakalpojumi. Lūk, kā to uzbūvēt, lai gūtu 20/20 punktus UX vērtējumā:
        </p>

        <div class="kpi-grid">
          <div class="kpi-card" style="background:#fff; border-top:4px solid var(--primary);">
            <strong style="color:var(--primary); font-size:1.05rem;">1. Sākumlapa (Avaleht)</strong>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:0.35rem;">
              • <strong>Viedais meklēšanas & filtru bloks:</strong> Klients izvēlas savu profilu (piem., <em>„Esmu eksportētājs“</em>, <em>„Meklēju digitalizācijas grantu“</em>).<br>
              • <strong>Kategoriju kartītes ar ikonām:</strong> Tiešas saites uz galvenajiem virzieniem (Inovācijas, Kredīti, Eksports).<br>
              • <strong>Top pakalpojumu karuselis:</strong> Tūlītēja piekļuve populārākajām programmām ar skaidriem statusa badge (<em>„Atvērts pieteikumiem“</em>).
            </p>
          </div>

          <div class="kpi-card" style="background:#fff; border-top:4px solid var(--accent);">
            <strong style="color:var(--accent); font-size:1.05rem;">2. Kategorija (/innoveeri-ja-kaitse-ari/)</strong>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:0.35rem;">
              • <strong>Daudzkritēriju filtrs:</strong> Atlase pēc uzņēmuma lieluma (Mikro / MVU / Liels) un atbalsta veida (Grants / Garantija / Mentors).<br>
              • <strong>Pārskatāmas pakalpojumu kartītes:</strong> Norādīts maksimālais atbalsta apjoms (€), intensitāte (%) un pieteikšanās termiņš.<br>
              • <strong>Ātrais salīdzināšanas rīks:</strong> Ļauj klientam saprast atšķirību starp diviem līdzīgiem atbalsta pasākumiem.
            </p>
          </div>

          <div class="kpi-card" style="background:#fff; border-top:4px solid var(--purple);">
            <strong style="color:var(--purple); font-size:1.05rem;">3. Pakalpojumu lapas (3 Paraugi)</strong>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:0.35rem;">
              • <strong>Digitalizācijas ceļa karte:</strong> Soļu grafiks (1. Diagnostika ➔ 2. Ceļa karte ➔ 3. Granta pieteikums), budžeta kalkulators.<br>
              • <strong>Aizdevuma garantija:</strong> Interaktīvs procentu likmes kalkulators un sadarbības banku saraksts ar tiešajām saitēm.<br>
              • <strong>Viedais pasūtītājs:</strong> Paziņojums par mentoriem un 1-klikšķa pieteikuma forma konsultācijai.
            </p>
          </div>
        </div>

        <!-- 3. Directus Data Modeling -->
        <h3 style="margin: 2.5rem 0 1rem 0;">3. Directus CMS Datu modeļu shēma (Mērogojamība)</h3>
        <p style="margin-bottom:1rem;">
          Lai pierādītu arhitektūras ilgtspēju, Directus jākonfigurē elastīgs un modulārs datu modelis:
        </p>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width:20%;">Kolekcija</th>
                <th style="width:30%;">Galvenie lauki</th>
                <th style="width:50%;">Nolūks un pielietojums</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong><code>pages</code></strong></td>
                <td><code>id, title, slug, status, seo_title, seo_desc, og_image, blocks (M2A)</code></td>
                <td>Dinamiskās lapas. Katra lapa sastāv no konfigurējamiem satura blokiem, ko satura redaktors var brīvi kārtot un rediģēt.</td>
              </tr>
              <tr>
                <td><strong><code>page_blocks</code></strong></td>
                <td><code>collection, item_id, sort_order</code></td>
                <td>Polimorfiskā saikne (Many-to-Any), kas apvieno: <code>hero_block</code>, <code>services_grid_block</code>, <code>steps_block</code>, <code>faq_accordion</code>, <code>cta_banner</code>.</td>
              </tr>
              <tr>
                <td><strong><code>services</code></strong></td>
                <td><code>title, slug, category_id, summary, max_amount, intensity_percent, eligibility, process_steps (JSON), cta_url</code></td>
                <td>Visi EIS sniegtie pakalpojumi un atbalsta programmas. Nodrošina vienotu datu avotu visām lapām un meklētājam.</td>
              </tr>
              <tr>
                <td><strong><code>categories</code></strong></td>
                <td><code>title, slug, icon, short_desc, color_theme</code></td>
                <td>Pakalpojumu tematiskās kategorijas (Inovācijas, Eksports, Kredīti, Tūrisms).</td>
              </tr>
              <tr>
                <td><strong><code>navigation</code></strong></td>
                <td><code>menu_type (header/footer), label, link_url, sort_order</code></td>
                <td>Globālā un kājenes navigācija, kas tiek pārvaldīta no CMS bez koda izmaiņām.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- 4. MCP AI Protocol Layer -->
        <h3 style="margin: 2.5rem 0 1rem 0;">4. Mākslīgā intelekta (AI) integrācija caur MCP (Model Context Protocol)</h3>
        <div class="callout callout-warning">
          <div class="callout-title">⭐ Nolikuma noslēpums, kas garantēs komisijas atzinību</div>
          <p>
            Nolikuma 4. pielikumā ir skaidri fiksēts: <em>„AI tööriistade tuge läbi MCP kihi“</em>. Lielākā daļa pretendentu to ignorēs vai nesapratīs. Izstrādājiet vienkāršu, bet funkcionējošu <strong>MCP Serveri</strong>, kas savieno AI aģentu ar Directus saturu:
          </p>
        </div>

        <ul style="margin-left:1.5rem; line-height:1.7; margin-bottom:1.5rem;">
          <li><strong>Rīks 1: <code>find_eis_services</code></strong> — Ļauj AI modelim pēc uzņēmuma apgrozījuma, darbinieku skaita un nozares no Directus atlasīt atbilstošās atbalsta programmas.</li>
          <li><strong>Rīks 2: <code>get_service_criteria</code></strong> — Nolasa konkrētas programmas pieteikšanās nosacījumus un sniedz atbildes uz klienta jautājumiem.</li>
          <li><strong>Frontend čatbota logs:</strong> Next.js saskarnē ievietojiet demonstrācijas logu <em>„EIS Viedais Asistents (ar MCP atbalstu)“</em>, kurā klients var pajautāt, piemēram: <em>„Esmu neliels ražotājs, vēlos digitalizēt noliktavu – kādu atbalstu varu saņemt?“</em>, un sistēma atgriež saiti uz <strong>Digitalizācijas ceļa kartes</strong> pakalpojumu!</li>
        </ul>

        <!-- 5. Docker Compose -->
        <h3 style="margin: 2.5rem 0 1rem 0;">5. Viss startējas ar vienu komandu: `docker compose up`</h3>
        <p style="margin-bottom:1rem;">
          Komisijai ir kritiski svarīgi novērtēt risinājumu lokāli bez sarežģītas konfigurācijas. Repozitorija saknē jābūt gatavam <code>docker-compose.yml</code> ar iepriekš sagatavotiem datubāzes datiem:
        </p>

        <div style="background:#1e293b; color:#e2e8f0; padding:1.5rem; border-radius:var(--radius-sm); font-family:'JetBrains Mono', monospace; font-size:0.85rem; line-height:1.5; overflow-x:auto;">
<pre style="margin:0;"><span style="color:#94a3b8;"># Repozitorija saknes docker-compose.yml fails</span>
<span style="color:#38bdf8;">version:</span> <span style="color:#fde047;">'3.8'</span>

<span style="color:#38bdf8;">services:</span>
  <span style="color:#a855f7;">postgres:</span>
    <span style="color:#38bdf8;">image:</span> postgres:15-alpine
    <span style="color:#38bdf8;">environment:</span>
      <span style="color:#cbd5e1;">POSTGRES_DB:</span> directus
      <span style="color:#cbd5e1;">POSTGRES_USER:</span> directus
      <span style="color:#cbd5e1;">POSTGRES_PASSWORD:</span> directus_password
    <span style="color:#38bdf8;">volumes:</span>
      <span style="color:#94a3b8;"># Iepriekš aizpildīti Directus shēmas un EIS satura dati!</span>
      - ./backend/init-db/01-eis-seed.sql:/docker-entrypoint-initdb.d/init.sql
    <span style="color:#38bdf8;">ports:</span>
      - <span style="color:#fde047;">"5432:5432"</span>

  <span style="color:#a855f7;">directus:</span>
    <span style="color:#38bdf8;">image:</span> directus/directus:latest
    <span style="color:#38bdf8;">ports:</span>
      - <span style="color:#fde047;">"8055:8055"</span>
    <span style="color:#38bdf8;">environment:</span>
      <span style="color:#cbd5e1;">KEY:</span> <span style="color:#fde047;">"eis-proovitoo-key"</span>
      <span style="color:#cbd5e1;">SECRET:</span> <span style="color:#fde047;">"eis-proovitoo-secret"</span>
      <span style="color:#cbd5e1;">DB_CLIENT:</span> <span style="color:#fde047;">"pg"</span>
      <span style="color:#cbd5e1;">DB_HOST:</span> <span style="color:#fde047;">"postgres"</span>
      <span style="color:#cbd5e1;">DB_PORT:</span> <span style="color:#fde047;">"5432"</span>
      <span style="color:#cbd5e1;">DB_DATABASE:</span> <span style="color:#fde047;">"directus"</span>
      <span style="color:#cbd5e1;">DB_USER:</span> <span style="color:#fde047;">"directus"</span>
      <span style="color:#cbd5e1;">DB_PASSWORD:</span> <span style="color:#fde047;">"directus_password"</span>
      <span style="color:#cbd5e1;">ADMIN_EMAIL:</span> <span style="color:#fde047;">"admin@eis.ee"</span>
      <span style="color:#cbd5e1;">ADMIN_PASSWORD:</span> <span style="color:#fde047;">"admin123"</span>
    <span style="color:#38bdf8;">depends_on:</span>
      - postgres

  <span style="color:#a855f7;">frontend:</span>
    <span style="color:#38bdf8;">build:</span>
      <span style="color:#cbd5e1;">context:</span> ./frontend
      <span style="color:#cbd5e1;">dockerfile:</span> Dockerfile
    <span style="color:#38bdf8;">ports:</span>
      - <span style="color:#fde047;">"3000:3000"</span>
    <span style="color:#38bdf8;">environment:</span>
      <span style="color:#cbd5e1;">NEXT_PUBLIC_DIRECTUS_URL:</span> <span style="color:#fde047;">"http://localhost:8055"</span>
    <span style="color:#38bdf8;">depends_on:</span>
      - directus</pre>
        </div>

        <!-- 6. Four Deliverables -->
        <h3 style="margin: 2.5rem 0 1rem 0;">6. Četru obligāto nodevumu kontrolsaraksts</h3>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width:22%;">Nodevums</th>
                <th style="width:25%;">Formāts</th>
                <th style="width:53%;">Izstrādes instrukcija maksimālajam vērtējumam</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. Koncepcijas dokuments</strong></td>
                <td>PDF (līdz 10 lpp.)</td>
                <td>
                  • Problēmas analīze un EIS digitālā transformācija (2 lpp.)<br>
                  • Klienta ceļvedis (User Journey) un biznesa loģika (2 lpp.)<br>
                  • Directus datu modeļu un komponentu specifikācija (2 lpp.)<br>
                  • Tehniskā arhitektūra, Next.js, Docker, MCP AI slānis (2 lpp.)<br>
                  • Drošība, WCAG 2.1 AA pieejamība un nākotnes migrācijas plāns (2 lpp.)
                </td>
              </tr>
              <tr>
                <td><strong>2. Figma DDS 2.0 prototips</strong></td>
                <td>Figma publiska / koplietota saite</td>
                <td>
                  • Pielietot oficiālo Igaunijas Zīmola dizaina sistēmu <em>💎 DDS 2.0 - WIP</em>.<br>
                  • Pilnībā klikšķināms ceļš no Avaleht ➔ Kategorija ➔ 3 Pakalpojumi.<br>
                  • Desktop (1440px) un Mobile (375px) adaptīvie ekrāni.<br>
                  • WCAG 2.1 AA kontrasta pārbaudes apliecinājums.
                </td>
              </tr>
              <tr>
                <td><strong>3. GitHub repozitorijs</strong></td>
                <td>GitHub ar komandas pieejām</td>
                <td>
                  • Pilns funkcionējošs Next.js + Directus kods ar <code>docker compose up</code>.<br>
                  • Koda vēsture ar jēgpilniem commit ierakstiem (Clean Git History).<br>
                  • Detalizēts <code>README.md</code> ar ekrānuzņēmumiem un palaišanas soļiem.<br>
                  • <strong>Obligāti piešķirt lasīšanas tiesības:</strong> <code>martinroos-eis</code> un <code>rvaher</code>!
                </td>
              </tr>
              <tr>
                <td><strong>4. Video prezentācija</strong></td>
                <td>YouTube nereģistrēts (unlisted) links</td>
                <td>
                  • Ilgums: <strong>līdz 10 minūtēm</strong> (vislabāk 8-9 minūtes).<br>
                  • Struktūra: 0:00-2:30 (Koncepcija un problēmas risinājums), 2:30-6:30 (Dzīvā demonstrācija pārlūkā un Directus CMS administrācijā), 6:30-8:30 (Tehniskā arhitektūra, MCP AI rīki un koda kvalitāte), 8:30-9:30 (Kopsavilkums).
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- 7. Timeline -->
        <h3 style="margin: 2.5rem 0 1rem 0;">7. Ieteicamais 12 dienu izstrādes plāns komandai</h3>
        <div style="background:#fff; border:1px solid var(--border); border-radius:var(--radius-sm); padding:1.5rem;">
          <ul style="list-style:none; display:flex; flex-direction:column; gap:0.75rem; font-size:0.9rem;">
            <li><strong style="color:var(--primary);">Diena 1-2:</strong> Analīze, satura atlase no eis.ee, Directus datu shēmas konfigurēšana un SQL eksports.</li>
            <li><strong style="color:var(--primary);">Diena 3-5:</strong> Figma prototipa izstrāde (DDS 2.0 komponentes, interaktīvie ceļi, mobilais skats).</li>
            <li><strong style="color:var(--accent);">Diena 6-8:</strong> Next.js frontenda izstrāde, Directus API savienošana, dinamiskie bloki un filtri.</li>
            <li><strong style="color:var(--purple);">Diena 9-10:</strong> MCP AI servisa integrācija, Docker Compose testēšana 'tīrā' vidē, automatizētie vienībtesti.</li>
            <li><strong style="color:var(--success);">Diena 11:</strong> Koncepcijas dokumenta (PDF līdz 10 lpp.) noformēšana un README pulēšana.</li>
            <li><strong style="color:var(--danger);">Diena 12:</strong> 10 minūšu video prezentācijas ierakstīšana, augšupielāde YouTube un saišu pievienošana eRHR reģistrā.</li>
          </ul>
        </div>
      </section>
"""

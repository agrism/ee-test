# EIS Proovitöö – Veebide ja Infosüsteemide Platvorm 2026 – 2029
**Riigihange viitenumbriga 315313 (Hankija siseviide: HNR260046)**  
*Ettevõtluse ja Innovatsiooni Sihtasutus (EIS)*  
*Vastavus: RHAD Lisa 4 (Proovitöö lähteülesanne) ja Lisa 2 (Hindamismetoodika)*

---

## 🚀 Kiirkäivitus (Quick Start)

Vastavalt RHAD Lisa 4 punktile 3.2 peab kogu arendatud lahendus käivituma **üheainsa käsuga**.

```bash
# 1. Liigu projekti kausta
cd home-task

# 2. Käivita kogu süsteem konteinerites (Frontend + Directus + PostgreSQL + MCP)
docker compose up --build
```

Pärast konteinerite käivitumist on teenused kättesaadavad järgmistel aadressidel:

| Teenus | Aadress | Kirjeldus & Ligipääsud |
|---|---|---|
| **Frontend (Next.js)** | [http://localhost:3002](http://localhost:3002) (või `:3000`) | Avalik veebirakendus DDS 2.0 disainisüsteemiga |
| **Directus CMS (Backend)** | [http://localhost:8055](http://localhost:8055) | Sisuhaldus (**E-post:** `admin@eis.ee`, **Parool:** `adminpassword`) |
| **MCP AI Server** | [http://localhost:3001](http://localhost:3001) | Model Context Protocol AI tööriistade kiht (`/healthz`, `/api/mcp/tools`) |
| **PostgreSQL Databaas** | `localhost:5435` (või `:5432`) | Andmebaas eelseadistatud EIS testandmetega |

---

## 🧭 Kliendi teekonna kontrollnimekiri (RHAD Lisa 4 p. 2.2)

Lahendus realiseerib täieliku ja katkematu teekonna **avalehelt teenuseleheni**:

1. **Avaleht (Avaleht / Home):**  
   👉 [http://localhost:3000](http://localhost:3000)  
   * Sisaldab nutikat teenuste otsingut, fookusteemasid ja populaarsemaid toetusmeetmeid.
2. **Kategooria sisuleht (Kategooria leht):**  
   👉 [http://localhost:3000/innoveeri-ja-kaitse-ari](http://localhost:3000/innoveeri-ja-kaitse-ari)  
   * Sisaldab dünaamilist mitmekriteeriumilist filtrit (toetuse liik, ettevõtte suurus, vabas vormis otsing).
3. **Teenuseleht 1: Digitaliseerimise teekaardi toetus:**  
   👉 [http://localhost:3000/teenused/digitaliseerimise-teekaardi-arendustegevused-toetus](http://localhost:3000/teenused/digitaliseerimise-teekaardi-arendustegevused-toetus)  
   * Sisaldab interaktiivset toetussumma kalkulaatorit (kuni 300 000 €), tingimuste kontrolli ja 4-sammulist taotlusprotsessi.
4. **Teenuseleht 2: Ettevõtluslaenu käendus:**  
   👉 [http://localhost:3000/teenused/laenukaendus-2](http://localhost:3000/teenused/laenukaendus-2)  
   * Sisaldab interaktiivset pangalaenu käenduse kalkulaatorit (kuni 80% riiklik tagatis) ja partnerpankade nimekirja.
5. **Teenuseleht 3: Tark tellija programm:**  
   👉 [http://localhost:3000/teenused/tark-tellija](http://localhost:3000/teenused/tark-tellija)  
   * Sisaldab mentorlusprogrammi kirjeldust, osalustingimusi ja registreerimise pilti.
6. **Tehisintellekti MCP demonstratsioon (AI Asistent):**  
   👉 [http://localhost:3000/ai-assistant](http://localhost:3000/ai-assistant)  
   * Reaalajas MCP (Model Context Protocol) tööriistade käivitamine ja meetmete semantiline soovitamine.

---

## 🏛️ Tehnoloogiline arhitektuur

```
 ┌────────────────────────────────────────────────────────┐
 │            FRONTEND (Next.js 14+ App Router)           │
 │   - React, TypeScript, Tailwind CSS, shadcn/ui         │
 │   - Eesti Brändi DDS 2.0 disainisüsteem                │
 │   - Server-Side Rendering (SSR) & Server Components    │
 └──────────────────────────▲─────────────────────────────┘
                            │ REST / GraphQL API
 ┌──────────────────────────▼─────────────────────────────┐
 │            BACKEND (Directus Headless CMS)             │
 │   - Universaalsed sisuplokid (M2A Block Builder)       │
 │   - Dünaamilised lehed ja URL-id (/teenused/[slug])    │
 │   - SEO metaandmete ja meediafailide haldus            │
 └───────────▲───────────────────────────────▲────────────┘
             │                               │
 ┌───────────▼────────────┐     ┌────────────▼────────────┐
 │  PostgreSQL 15         │     │ MCP Server (Node.js)    │
 │  Eelseadistatud seed   │     │ Model Context Protocol  │
 │  skeem ja andmed       │     │ LLM tööriistade kiht    │
 └────────────────────────┘     └─────────────────────────┘
```

### 1. Frontend (Next.js App Router & TypeScript)
* **Server Components & SSR:** Kõik lehed renderdatakse serveripoolselt, tagades kiireima esmase laadimisaja ja täiuslikud SEO näitajad (*Google Core Web Vitals rohelises tsoonis*).
* **DDS 2.0 Vastavus:** Kasutatud on Eesti Brändi digitaalse disainisüsteemi ametlikke värvitoone, tüpograafiat ja disainitokeneid.
* **Juurdepääsetavus:** Järgitud on **WCAG 2.1 AA** kontrasti- ja klaviatuurinavigatsiooni nõudeid.

### 2. Sisuhaldus (Directus Headless CMS)
* Eraldatud esitlus- ja sisuhalduskiht.
* Datu struktuur toetab universaalseid sisuplokke: `hero`, `services_grid`, `process_steps`, `faq`, `cta_banner`.
* **Tõrketaluvus (Graceful Fallback):** Juhul kui Directus CMS konteiner on taaskäivitamisel, kasutab frontend sisseehitatud varukoopiat (`seed-data.ts`), mis tagab, et veebileht ei kuva kunagi tühja lehte ega 500 viga.

### 3. Tehisintellekti tugi läbi MCP (Model Context Protocol)
* Vastavalt RHAD Lisa 4 nõudele sisaldab lahendus toimivat **MCP serverit** (`/mcp-server`), mis pakub standardiseeritud tööriistu:
  * `find_eis_services`: Analüüsib ettevõtja vabas vormis kirjeldust ja soovitab Directusest sobivaid toetusmeetmeid.
  * `get_service_criteria`: Annab detailse ülevaate meetme tingimustest.

---

## 🛠️ Lokaalne arendus ilma Dockerita

Kui soovite rakendust käivitada lokaalselt ilma Dockerita:

```bash
# 1. Frontend
cd home-task/frontend
npm install
npm run dev
# Rakendus avaneb aadressil: http://localhost:3000

# 2. MCP Server
cd ../mcp-server
npm install
npm start
# MCP server kuulab pordil: http://localhost:3001
```

---

## 👥 Ligipääsud ja esitamine

Vastavalt RHAD Lisa 4 punktile 4.3 on GitHubi repositooriumile tagatud ligipääs hankija hindajatele:
* `martinroos-eis`
* `rvaher`

Videotutvustus (kuni 10 minutit) on laaditud YouTube'i registrivälise (unlisted) lingina ning esitatud Riigihangete Registris.

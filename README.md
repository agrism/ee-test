# EIS Iepirkums 2026 – 2029 (Hanke viitenumber: 315313)
**Veebide ja infosüsteemide analüüsi, arendus- ning hooldustööd 2026 - 2029**  
*Ettevõtluse ja Innovatsiooni Sihtasutus (EIS)*

Šis repozitorijs satur EIS iepirkuma pilno dokumentāciju, analīzi, tulkojumus latviešu valodā un **Proovitöö (4. pielikuma pārbaudes uzdevuma)** pilno koda risinājumu.

---

## 📁 Repozitorija struktūra

* **`home-task/`** – **EIS Proovitöö (Pārbaudes uzdevuma)** pilns risinājums:
  * **Next.js 14+ App Router** ar Igaunijas zīmola **DDS 2.0** dizaina sistēmu un **WCAG 2.1 AA** piekļūstamību.
  * **Directus Headless CMS** ar dinamiskām lapām un blokiem.
  * **PostgreSQL** datubāze ar iepriekš aizpildītiem EIS datiem 3 pakalpojumiem.
  * **Model Context Protocol (MCP)** serveris ar AI rīkiem uzņēmumu konsultēšanai.
  * *Skatīt detalizētu instrukciju: [`home-task/README.md`](./home-task/README.md)*
* **`index.html`** – Pilns interaktīvais iepirkuma portāls latviešu valodā:
  * 110 CFR (Cross-Functional Requirements) interaktīva meklēšana un filtrēšana.
  * 20p / 80p finanšu un tehniskā vērtējuma kalkulators.
  * Komandas atbilstības prasību matrica (6 speciālistu lomas).
  * Visi iepirkuma dokumenti ar paralēlu igauņu oriģināltekstu atvēršanu.
* **`Iepirkuma doc orginals/`** – Iepirkuma oriģinālie dokumenti igauņu valodā (RHAD Üldosa, Lisa 1–5, Vastavustingimused, Hindamiskriteeriumid, ESPD).
* **`scripts/`** – Dokumentu parsēšanas, CFR prasību tulkošanas un automatizācijas skripti.

---

## 🚀 Proovitöö palaišana (Quick Start)

Pārbaudes uzdevuma risinājums startējas ar vienu komandu:

```bash
cd home-task
docker compose up --build
```

Pēc startēšanas servisi ir pieejami:
* **Frontend:** [http://localhost:3002](http://localhost:3002) (vai `:3000`)
* **Directus CMS:** [http://localhost:8055](http://localhost:8055) (`admin@eis.ee` / `adminpassword`)
* **MCP AI Server:** [http://localhost:3001](http://localhost:3001)
* **PostgreSQL:** `localhost:5435` (vai `:5432`)

---

## 👥 Vērtētāju piekļuve (RHAD Lisa 4 p. 4.3)

* `martinroos-eis`
* `rvaher`

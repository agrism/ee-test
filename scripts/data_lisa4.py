# -*- coding: utf-8 -*-
"""
Latvian translation and Estonian original text for RHAD LISA 4
(Test Task Specification / Proovitoo lahteulesanne).
"""

LISA4_DATA = {
    "title_lv": "Pielikums 4 – Pārbaudes darba (Proovitöö) darba uzdevums",
    "title_ee": "RHAD Lisa 4 - Proovitöö lähteülesanne",
    "intro_lv": "Pārbaudes darbs ir iepirkuma svarīgākā vērtējamā daļa (dod 80 no 100 punktiem). Tā mērķis ir pārbaudīt pretendenta komandas reālās spējas analizēt, modelēt, dizainēt (Figma DDS 2.0) un tehniski realizēt funkcionējošu Next.js + Directus Headless CMS prototipu, kā arī demonstrēt risinājumu 10 minūšu video prezentācijā.",
    "problem_description_lv": "EIS līdz šim ir darbojies pēc principa, kur gan galvenajam zīmolam, gan apakšzīmoliem ir atsevišķas tīmekļa vietnes, kas darbojušās individuāli atsevišķās vidēs. Tas nozīmē, ka koda bāze ir ļoti atšķirīga, lapas veidotas dažādos laikos un jebkādi papildu uzlabojumi nozīmēja vienas un tās pašas izstrādes atkārtošanu vairākās vietnēs. Jaunais virziens ir apvienot visas dažādās vietnes zem vienas pārvaldības sistēmas – Directus Headless CMS (https://directus.com), lai nākotnē garantētu vienotu koda bāzi, universālus satura blokus un vienkāršāku satura vadību. Tāpat ir atjaunota zīmola dizaina sistēma (DDS 2.0), un nepieciešams saturu padarīt lietotājam loģisku, viegli atrodamu un ērti lietojamu.",
    "goal_lv": "Novērtēt pretendenta spēju analizēt, dizainēt, modelēt un aprakstīt risinājumu, kas nodrošina klienta ceļvedi no eis.ee sākumlapas līdz pakalpojuma lapai. Klienta ceļam jāsākas no EIS sākumlapas un jābeidzas pakalpojuma lapā, ietverot sākumlapu, vismaz vienu kategorijas satura lapu pa vidu un vismaz trīs (3) pakalpojumu lapas.",
    "sample_pages": [
        {"type_lv": "Sākumlapa (Avaleht)", "url": "https://eis.ee"},
        {"type_lv": "Kategorijas lapa (Kategooria leht)", "url": "https://eis.ee/innoveeri-ja-kaitse-ari/"},
        {"type_lv": "Pakalpojuma lapa 1", "url": "https://eis.ee/teenused/digitaliseerimise-teekaardi-arendustegevused-toetus/"},
        {"type_lv": "Pakalpojuma lapa 2", "url": "https://eis.ee/teenused/laenukaendus-2/"},
        {"type_lv": "Pakalpojuma lapa 3", "url": "https://eis.ee/teenused/tark-tellija"}
    ],
    "functional_reqs_lv": [
        "Dinamiskas lapas un URL: Risinājumam jāatbalsta dinamisku lapu un URL veidošana, balstoties uz Directus pārvaldīto saturu.",
        "SEO metadatu pārvaldība: Pilnīga meta tagu, OpenGraph datu un virsrakstu konfigurēšana Directus vidē.",
        "Mākslīgā intelekta (AI) rīku atbalsts caur MCP slāni: Risinājumam jāatbalsta AI rīku integrācija, izmantojot Model Context Protocol (MCP) slāni.",
        "Mediju pārvaldība: Attēlu un citu mediju failu integrācija caur Directus failu krātuvi.",
        "Daudzvalodība: Iespēja pārvaldīt un attēlot daudzvalodu saturu.",
        "Bloku un komponenšu arhitektūra: Lapu salikšana no elastīgiem, universāliem satura blokiem un komponentēm.",
        "Komponenšu atkārtota izmantošana: Viena un tā paša koda komponentu atkalizmantošana dažādiem satura veidiem un dažādām vietnēm."
    ],
    "technical_reqs_lv": [
        "Frontend tehnoloģijas: Jārealizē Next.js App Router arhitektūrā, izmantojot React un TypeScript.",
        "Headless CMS: Satura pārvaldībai jāizmanto Directus Headless CMS. Frontend un Directus jābūt pilnībā atdalītiem un jāsazinās caur API.",
        "API integrācija: Datu ielādei jāizmanto Directus SDK, REST API vai GraphQL API. Risinājumam jānodrošina servera puses datu ielāde un renderēšana (SSR / Server Components) Next.js ietvarā.",
        "Docker konteineri: Visam risinājumam (frontend + Directus backend + datubāze) jādarbojas konteineros.",
        "Palaišana ar 1 komandu: Gatavajam risinājumam obligāti jāstartējas ar vienu vienīgu komandu: `docker compose up`.",
        "Instrukcija: Jāpievieno skaidra un detalizēta palaišanas instrukcija (README)."
    ],
    "deliverables": [
        {
            "num": "1",
            "title_lv": "Problēmas izpratne un risinājuma koncepcijas apraksts",
            "format": "Dokuments līdz 10 lappusēm (PDF)",
            "desc_lv": "Detalizēts apraksts par izvēlēto arhitektūru, datu modeļiem Directus, komponentu struktūru, UX pieeju un risinājuma ilgtspēju."
        },
        {
            "num": "2",
            "title_lv": "Klikšķināms Figma prototips",
            "format": "Figma saite ar publisku vai koplietotu piekļuvi",
            "desc_lv": "Interaktīvs prototips, kas veidots, balstoties uz pasūtītāja digitālo dizaina sistēmu DDS 2.0 (💎 DDS 2.0 - WIP)."
        },
        {
            "num": "3",
            "title_lv": "Gatavs, strādājošs koda risinājums (Frontend + Backend)",
            "format": "GitHub repozitorijs ar pilnu versiju vēsturi",
            "desc_lv": "Pilns funkcionējošs kods Next.js + Directus ar docker compose konfigurāciju. Jādod piekļuve GitHub lietotājiem: 'martinroos-eis' un 'rvaher'."
        },
        {
            "num": "4",
            "title_lv": "Video prezentācija",
            "format": "YouTube nereģistrēta (unlisted) saite",
            "desc_lv": "Maksimums 10 minūšu video, kurā pretendents prezentē risinājumu pēc būtības, skaidro arhitektūras izvēles un demonstrē darbību."
        }
    ],
    "submission_rules_lv": [
        "Komandas sastāvs: Pasūtītājs sagaida, ka pārbaudes darbu sagatavo tie paši speciālisti, kuri tiek pieteikti iepirkuma komandas sastāvā.",
        "Apjoma ierobežojumi eRHR: Tā kā e-iepirkumu sistēmā ir failu apjoma ierobežojumi, koda risinājumu nodod caur GitHub, bet video augšupielādē YouTube, un to saites norāda RHR iesniegtajos materiālos.",
        "Termiņš: Visiem failiem un saitēm jābūt iesniegtām līdz oficiālajam piedāvājumu iesniegšanas termiņam. Vēlākas izmaiņas netiek ņemtas vērā. GitHub repozitorijā jābūt redzamai pilnai commit vēsturei.",
        "Dzēšanas aizliegums: Failus un piekļuves aizliegts dzēst līdz brīdim, kad ir noslēgta vispārīgā vienošanās."
    ]
}

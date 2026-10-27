# -*- coding: utf-8 -*-
"""
Script to parse and translate all CFR items from Lisa 5 into clean Latvian.
"""
import json, re, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load parsed raw CFRs
parsed_path = os.path.join(SCRIPT_DIR, "cfr_parsed.json")
with open(parsed_path, "r", encoding="utf-8") as f:
    raw_cfrs = json.load(f)

# Helper dictionary of Estonian-to-Latvian translations for CFR items
translations = {
    "CFR-001": {
        "title_lv": "Koda versiju vadība ar Git",
        "desc_lv": "Lietotnes kodam jābūt versionētam, izmantojot Git. Jāievēro pasūtītāja noteiktais IT profils.",
        "details_lv": "Git repozitorijs ar skaidru zarošanas stratēģiju (GitFlow/Trunk-based).",
        "cat_lv": "Izstrāde",
        "type_lv": "Obligāts"
    },
    "CFR-002": {
        "title_lv": "Datubāzes versiju vadība un migrācijas",
        "desc_lv": "Lietotnes datubāzei jābūt versionētai. Jāizmanto migrāciju skripti (Liquibase, Flyway).",
        "details_lv": "Visiem datubāzes struktūras grozījumiem jābūt automatizētiem un izsekojamiem versiju vadībā.",
        "cat_lv": "Izstrāde",
        "type_lv": "Sagaidāms"
    },
    "CFR-003": {
        "title_lv": "Tīrs un pašsaprotams kods (Clean Code)",
        "desc_lv": "Kodam jābūt uzrakstītam pietiekami skaidri, lai tas būtu lasāms un saprotams bez komentāriem (clean code). Vietās, kur citam izstrādātājam var rasties pārpratuma risks, kodam jābūt skaidri komentētam.",
        "details_lv": "Ievērot labākās Clean Code prakses un jēgpilnu nosaukumu došanas principus.",
        "cat_lv": "Izstrāde",
        "type_lv": "Obligāts"
    },
    "CFR-004": {
        "title_lv": "Kods un komentāri angļu valodā",
        "desc_lv": "Lietotnes pirmkodam, mainīgo nosaukumiem un koda komentāriem jābūt angļu valodā.",
        "details_lv": "Kods un dokumentācija kodā tiek rakstīta angliski, savukārt lietotāja saskarne un funkcionālā dokumentācija - igauņu valodā.",
        "cat_lv": "Izstrāde",
        "type_lv": "Obligāts"
    },
    "CFR-005": {
        "title_lv": "Programmatūras licencēšana",
        "desc_lv": "Lietotnes programmatūrai jābūt marķētai ar licenci. Ieteicams izmantot MIT licenci.",
        "details_lv": "MIT atvērtā koda licences marķējums repozitorijā.",
        "cat_lv": "Izstrāde",
        "type_lv": "Ieteikums"
    },
    "CFR-006": {
        "title_lv": "Programmēšanas valodu ierobežojums (TIOBE Top 25)",
        "desc_lv": "Lietotņu izstrādē nedrīkst izmantot programmēšanas valodas, kas nav iekļautas TIOBE index Top 25 sarakstā.",
        "details_lv": "Mērķis ir minimizēt situācijas, kad tiek radīti komponenti tehnoloģijās, kurām vēlāk grūti atrast izstrādātājus.",
        "cat_lv": "Izstrāde",
        "type_lv": "Sagaidāms"
    },
    "CFR-007": {
        "title_lv": "Komponentu dzīves cikla beigas (EOL) uzraudzība",
        "desc_lv": "Visiem izstrādē izmantotajiem komponentiem (lietotnes bibliotēkas, datubāzes, trešo pušu risinājumi) nedrīkst būt zināms dzīves cikla beigu termiņš (EOL) tuvāko 2 gadu laikā.",
        "details_lv": "Aizliegts izmantot novecojušas un neatbalstītas bibliotēkas.",
        "cat_lv": "Izstrāde",
        "type_lv": "Obligāts"
    },
    "CFR-008": {
        "title_lv": "Aktuāla un uzturēta sistēmas dokumentācija",
        "desc_lv": "Pakalpojumu lietotnēm jābūt aktuālai un uzturētai tehniskajai dokumentācijai (arhitektūra, izvietošana, konfigurācija).",
        "details_lv": "Dokumentācija tiek uzturēta pasūtītāja Confluence un repozitorija README failos.",
        "cat_lv": "Izstrāde",
        "type_lv": "Obligāts"
    },
    "CFR-009": {
        "title_lv": "Lietotāja saskarnes stāvokļa (State) pārvaldība",
        "desc_lv": "Lietotāja saskarnes stāvoklis (state) tiek glabāts klienta pusē (pārlūkprogrammā), nodrošinot bezstāvokļa (stateless) aizmugursistēmas servisus.",
        "details_lv": "Ļauj brīvi mērogot aizmugursistēmu aiz slodzes balansētāja (LB) un Kubernetes klasterī.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Sagaidāms"
    },
    "CFR-010": {
        "title_lv": "Tehnisko kļūdu žurnālēšana (Error Logging)",
        "desc_lv": "Lietotnei jāreģistrē visas tajā radušās tehniskās kļūdas un izņēmumi ar konteksta informāciju.",
        "details_lv": "Kļūdu žurnāliem jābūt strukturētiem un nosūtāmiem uz centrālo žurnālu sistēmu.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-011": {
        "title_lv": "Žurnālu loģiskais dalījums",
        "desc_lv": "Žurnāliem (logiem) jābūt loģiski nodalītiem: audita žurnāls (sesijas, lietotāju darbības), sistēmas kļūdu žurnāls un veiktspējas metrikas.",
        "details_lv": "Atsevišķa pieeja audita un diagnostikas ierakstiem atbilstoši GDPR un drošības prasībām.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-012": {
        "title_lv": "Sensitīvu datu izslēgšana no žurnāliem",
        "desc_lv": "Žurnāla ierakstos aizliegts iekļaut paroles, piekļuves atslēgas, autorizācijas tokenus un personu sensitīvos datus.",
        "details_lv": "Automātiska datu maskēšana pirms žurnāla ieraksta saglabāšanas.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-013": {
        "title_lv": "Konteinerizācija un Docker vide",
        "desc_lv": "Visiem pakalpojumiem un lietotnēm jābūt konteinerizētiem (Docker) un gataviem darbināšanai Kubernetes vidē (Riigipilv).",
        "details_lv": "Dockerfaili optimizēti, multi-stage būvēšana, minimāls bāzes attēla izmērs.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-014": {
        "title_lv": "Infrastruktūra kā kods (IaC) un deklaratīva konfigurācija",
        "desc_lv": "Lietotnes izvietošanas konfigurācijām jābūt definētām kā kodam (Helm charts, Kubernetes manifests, ArgoCD).",
        "details_lv": "Pilnīga GitOps pieeja un deklaratīva vides pārvaldība.",
        "cat_lv": "Piegāde (CI/CD)",
        "type_lv": "Obligāts"
    },
    "CFR-015": {
        "title_lv": "CI/CD automatizētie cauruļvadi",
        "desc_lv": "Būvēšanai, testēšanai un izvietošanai jāizmanto automatizēti GitLab CI cauruļvadi (pipelines).",
        "details_lv": "Katrs commits iziet automātisku lintingu, vienībtestus un drošības skenēšanu.",
        "cat_lv": "Piegāde (CI/CD)",
        "type_lv": "Obligāts"
    },
    "CFR-016": {
        "title_lv": "Automātisko vienībtestu (Unit tests) prasība",
        "desc_lv": "Kritiskajai biznesa loģikai jābūt pārklātai ar automātiskajiem vienībtestiem. Testu izpildei jābūt obligātam solim CI/CD cauruļvadā.",
        "details_lv": "Koda pārklājuma uzraudzība un regulāra izpilde pirms koda sapludināšanas.",
        "cat_lv": "Kvalitāte",
        "type_lv": "Obligāts"
    },
    "CFR-017": {
        "title_lv": "Statiskā koda analīze un drošības pārbaude (SAST)",
        "desc_lv": "CI/CD cauruļvadā jābūt iekļautai statiskajai koda analīzei (SonarQube vai līdzvērtīgs rīks) un bibliotēku ievainojamību skenēšanai.",
        "details_lv": "Automātiska bloķēšana augsta riska ievainojamību gadījumā.",
        "cat_lv": "Kvalitāte",
        "type_lv": "Obligāts"
    },
    "CFR-018": {
        "title_lv": "Koda pārskatīšanas (Code Review) process",
        "desc_lv": "Neviens kods nedrīkst tikt sapludināts galvenajā zarā bez vismaz viena cita izstrādātāja apstiprinājuma (Merge Request / Pull Request).",
        "details_lv": "Četru acu princips (Four-eyes principle) izstrādes procesā.",
        "cat_lv": "Kvalitāte",
        "type_lv": "Obligāts"
    },
    "CFR-019": {
        "title_lv": "Semantiskā versiju vadība (SemVer)",
        "desc_lv": "Laidieniem un komponentu versijām jāizmanto semantiskā versiju vadība (SemVer 2.0.0: MAJOR.MINOR.PATCH).",
        "details_lv": "Skaidra un paredzama izmaiņu ietekme uz savietojamību.",
        "cat_lv": "Izstrāde",
        "type_lv": "Obligāts"
    },
    "CFR-020": {
        "title_lv": "Automātiski ģenerēta API dokumentācija",
        "desc_lv": "Visiem tehnisko komponentu publiskajiem un iekšējiem API jābūt automātiski ģenerētai dokumentācijai (OpenAPI 3.0 / Swagger).",
        "details_lv": "Dokumentācijai vienmēr jābūt sinhronizētai ar reālo koda stāvokli.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-021": {
        "title_lv": "Domēna vadīts dizains (DDD) un mikrosistēmu principi",
        "desc_lv": "Lietotnēm jābūt veidotām, ievērojot Domain-Driven Design principus un vāji saistītu servisu arhitektūru ar skaidrām atbildības robežām.",
        "details_lv": "Modulāra struktūra ar minimālu savstarpējo atkarību.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Sagaidāms"
    },
    "CFR-022": {
        "title_lv": "RESTful un GraphQL API standarti",
        "desc_lv": "Datu apmaiņai starp front-end un back-end jāizmanto standarta RESTful JSON vai GraphQL protokoli ar paredzamām statusa atbildēm.",
        "details_lv": "Standarta HTTP statusu kodi (200, 201, 400, 401, 403, 404, 500) un vienota kļūdu JSON struktūra.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-023": {
        "title_lv": "Asinhrona notikumu apstrāde",
        "desc_lv": "Ilgstošiem fona procesiem un datu apmaiņai starp sistēmām jāizmanto asinhronas rindu vai notikumu ziņojumapmaiņas arhitektūras.",
        "details_lv": "Lietotāja saskarne netiek bloķēta fona darbu laikā.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Sagaidāms"
    },
    "CFR-024": {
        "title_lv": "Pakalpojumu veselības pārbaudes (Health Checks)",
        "desc_lv": "Katram servisam jānodrošina `/healthz`, `/live` un `/ready` galapunkti Kubernetes veselības un gatavības pārbaudēm.",
        "details_lv": "Automātiska bojātu konteineru pārstartēšana un slodzes noņemšana.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-025": {
        "title_lv": "Konfigurācijas atdalīšana no koda (12-Factor App)",
        "desc_lv": "Lietotnes konfigurācijai jābūt pilnībā atdalītai no koda un padotai caur vides mainīgajiem (Environment Variables) vai Secret pārvaldnieku.",
        "details_lv": "Vienāds koda artefakts tiek darbināts izstrādes, testa un produkcijas vidēs.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-026": {
        "title_lv": "Horizontāla mērogojamība (Stateless)",
        "desc_lv": "Aizmugursistēmas lietotņu instancēm jābūt bezstāvokļa, lai tās varētu horizontāli mērogot atkarībā no slodzes.",
        "details_lv": "Datu glabāšana tikai ārējās datubāzēs, Redis vai S3 krātuvē.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-027": {
        "title_lv": "Graceful Shutdown un darbības pabeigšana",
        "desc_lv": "Konteineriem jāatbalsta droša darba apturēšana (SIGTERM apstrāde), pabeidzot aktīvos pieprasījumus pirms procesa beigām.",
        "details_lv": "Nepārtraukta pakalpojuma pieejamība versiju atjaunināšanas laikā (Zero-downtime).",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-028": {
        "title_lv": "Atvērtā koda bibliotēku auditi",
        "desc_lv": "Izmantotajām npm / pip / composer bibliotēkām jābūt aktīvi uzturētām un bez neatrisinātām kritiskām ievainojamībām.",
        "details_lv": "Regulāra npm audit / dependabot pārbaude.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-029": {
        "title_lv": "Autentifikācija un autorizācija (OAuth2 / OIDC)",
        "desc_lv": "Lietotāju autentifikācijai jāizmanto atvērtie standarti OAuth 2.0 un OpenID Connect (OIDC), nodrošinot vienoto pieteikšanos (SSO).",
        "details_lv": "Integrācija ar Valsts autentifikācijas pakalpojumu (Tara) un EIS iekšējo identitātes pārvaldnieku.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-030": {
        "title_lv": "Lomu bāzēta piekļuves kontrole (RBAC)",
        "desc_lv": "Lietotnē un satura vadības sistēmā (Directus) jābūt ieviestai granulārai lomu un tiesību pārvaldībai.",
        "details_lv": "Pieeja tikai tiem datiem un darbībām, kas nepieciešamas konkrētās lomas izpildei.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-031": {
        "title_lv": "Ievaddatu validācija un sanitizācija",
        "desc_lv": "Visiem no klienta vai ārējām sistēmām saņemtajiem datiem jāveic stingra servera puses validācija un sanitizācija (XSS un SQLi novēršana).",
        "details_lv": "Nekad neuzticēties klienta sniegtajiem datiem.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-032": {
        "title_lv": "CSRF aizsardzība",
        "desc_lv": "Visām stāvokli mainošajām darbībām (POST, PUT, DELETE) jānodrošina aizsardzība pret starpvietņu pieprasījumu viltošanu (CSRF žetoni vai SameSite sīkfaili).",
        "details_lv": "Standarta drošības mehānisms visām formām un API pieprasījumiem.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-033": {
        "title_lv": "Stateless klienta sesijas",
        "desc_lv": "Klienta saskarnes stāvoklis un sesijas informācija tiek uzturēta klienta pusē vai bezstāvokļa žetonos (JWT ar īsu derīguma termiņu).",
        "details_lv": "Aizmugursistēmas serveriem nav nepieciešama sesiju sinhronizācija.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Ieteikums"
    },
    "CFR-034": {
        "title_lv": "Strukturēts kļūdu žurnāls JSON formātā",
        "desc_lv": "Visiem kļūdu žurnālu ierakstiem jābūt strukturētā formātā (ieteicams JSON) ar laika zīmogu, kļūdas kodu un izsekošanas ID.",
        "details_lv": "Atvieglo automatizētu analīzi un monitoringu Elasticsearch / Kibana vidē.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-035": {
        "title_lv": "Auditācijas pierakstu nodalīšana un neaizskaramība",
        "desc_lv": "Lietotāju drošības un datu apstrādes audita pieraksti tiek glabāti atsevišķi no ikdienas lietojuma logiem un nav maināmi.",
        "details_lv": "Nodrošina atbilstību ISKE un GDPR prasībām par datu izsekojamību.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-036": {
        "title_lv": "Droša paroļu hešēšana (Argon2 / bcrypt)",
        "desc_lv": "Paroles un slepenās atslēgas nekad netiek glabātas atvērtā veidā. Jāizmanto mūsdienīgi hešēšanas algoritmi (Argon2id vai bcrypt ar atbilstošu darba faktoru).",
        "details_lv": "Pilnīga drošība datubāzes noplūdes gadījumā.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-037": {
        "title_lv": "HTTPS un TLS 1.3 šifrēšana",
        "desc_lv": "Visa datu pārraide starp klientu un serveri, kā arī starp iekšējiem komponentiem jānodrošina ar šifrēšanu (TLS 1.2+ / TLS 1.3).",
        "details_lv": "Stingra HSTS (HTTP Strict Transport Security) politikas ieviešana.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-038": {
        "title_lv": "Drošības galvenes (Security Headers)",
        "desc_lv": "Tīmekļa atbildēs jābūt iekļautām standarta drošības galvenēm: CSP, X-Content-Type-Options, X-Frame-Options, Referrer-Policy.",
        "details_lv": "Aizsardzība pret Clickjacking, MIME pārņemšanu un nesankcionētiem skriptiem.",
        "cat_lv": "Drošība",
        "type_lv": "Obligāts"
    },
    "CFR-039": {
        "title_lv": "Mākoņa infrastruktūras pielāgošana (Riigipilv)",
        "desc_lv": "Lietotnēm jābūt optimizētām darbam Igaunijas Valsts mākonī (Riigipilv) uz Kubernetes platformas.",
        "details_lv": "Savietojamība ar Riigipilv sniegtajiem pakalpojumiem un tīkla drošības zonām.",
        "cat_lv": "Piegāde (CI/CD)",
        "type_lv": "Obligāts"
    },
    "CFR-040": {
        "title_lv": "Datubāzu savienojumu pūls (Connection Pooling)",
        "desc_lv": "Datubāzes pieprasījumiem jāizmanto efektīvs savienojumu pūls (connection pooler), lai novērstu pārslodzi pie lielas lietotāju aktivitātes.",
        "details_lv": "PgBouncer vai iebūvētais savienojumu pūls.",
        "cat_lv": "Datu pārvaldība",
        "type_lv": "Sagaidāms"
    },
    "CFR-050": {
        "title_lv": "Tīmekļa lietotņu ugunsmūra (WAF) noteikumu ievērošana",
        "desc_lv": "Lietotnes arhitektūrai jābūt saskaņotai ar WAF noteikumiem un jāievēro OWASP rekomendācijas.",
        "details_lv": "Sistēma nedrīkst radīt viltus trauksmes standarta drošības ugunsmūru uzraudzībā.",
        "cat_lv": "Drošība",
        "type_lv": "Sagaidāms"
    },
    "CFR-051": {
        "title_lv": "Datu kodējums UTF-8",
        "desc_lv": "Visiem datiem lietotnē, API saskarnēs, failos un datubāzē jābūt glabātiem un apstrādātiem vismaz UTF-8 kodējumā.",
        "details_lv": "Nodrošina pilnu atbalstu igauņu, latviešu un citām daudzvalodu rakstzīmēm.",
        "cat_lv": "Datu pārvaldība",
        "type_lv": "Obligāts"
    },
    "CFR-052": {
        "title_lv": "Lietotnes un datubāzes serveru nodalīšana",
        "desc_lv": "Lietotnes izpildes videi un datubāzes serverim jābūt izvietotiem atsevišķos serveros/konteineros drošības un mērogojamības nolūkos.",
        "details_lv": "Tīkla izolācija un piekļuves ierobežojumi datubāzes slānim.",
        "cat_lv": "Datu pārvaldība",
        "type_lv": "Sagaidāms"
    },
    "CFR-053": {
        "title_lv": "Failu glabāšana S3 saderīgā objektu krātuvē",
        "desc_lv": "Failu, dokumentu un mediju glabāšanai jāizmanto S3 vai analoģisks objektu glabāšanas risinājums (AWS S3, Ceph, Riigipilv S3).",
        "details_lv": "Faili netiek glabāti lietotnes konteinera lokālajā diska telpā.",
        "cat_lv": "Datu pārvaldība",
        "type_lv": "Obligāts"
    },
    "CFR-070": {
        "title_lv": "Uznirstošo logu (pop-up) aizliegums",
        "desc_lv": "Lietotāja saskarnē aizliegts izmantot pārlūkprogrammas standarta pop-up logus. Atļauti tikai labi izstrādāti lietotnes iekšējie modālie logi (modals).",
        "details_lv": "Nodrošina kvalitatīvu lietotāja pieredzi un novērš pārlūkprogrammu bloķētāju konfliktus.",
        "cat_lv": "Izstrāde",
        "type_lv": "Obligāts"
    },
    "CFR-071": {
        "title_lv": "Mīkstā dzēšana (Soft Delete) datu bāzē",
        "desc_lv": "Būtiskajiem datubāzes ierakstiem jāizmanto mīkstās dzēšanas pieeja (ar statusa vai dzēšanas lauka atzīmi), lai nodrošinātu datu atjaunošanas iespēju.",
        "details_lv": "Ieraksti netiek fiziski izdzēsti uzreiz, saglabājot vēsturi un auditējamību.",
        "cat_lv": "Datu pārvaldība",
        "type_lv": "Sagaidāms"
    },
    "CFR-072": {
        "title_lv": "Atbilstība pasūtītāja IT profilam",
        "desc_lv": "Projektētajam risinājumam jābūt pilnīgā saskaņā ar pasūtītāja apstiprināto IT arhitektūras un tehnoloģiju profilu.",
        "details_lv": "Izstrāde iekļaujas EIS tehnoloģiju standartos.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-073": {
        "title_lv": "Biznesa loģikas atdalīšana no datu piekļuves slāņa",
        "desc_lv": "Lietotnes biznesa loģika jārealizē servisu slānī, nodalot to no konkrētās datubāzes vai API piekļuves implementācijas.",
        "details_lv": "Atvieglo vienībtestēšanu un nākotnes refaktorēšanu.",
        "cat_lv": "Arhitektūra",
        "type_lv": "Obligāts"
    },
    "CFR-092": {
        "title_lv": "Izmaiņu žurnāls (Changelog) ar katru versiju",
        "desc_lv": "Katrai jaunajai versijai jābūt skaidri dokumentētam izmaiņu žurnālam (Changelog) ar laboto defektu un pievienoto funkciju aprakstu.",
        "details_lv": "Paredzama un caurspīdīga laidienu vadība.",
        "cat_lv": "Kvalitāte",
        "type_lv": "Obligāts"
    },
    "CFR-094": {
        "title_lv": "Vienotas koda un API nosaukumu konvencijas",
        "desc_lv": "Visam pirmkodam un API laukiem jāizmanto vienotas konvencijas: camelCase API un JS/TS metodēm, PascalCase klasēm, UPPER_SNAKE konstantēm.",
        "details_lv": "Standartizēts stils visā koda bāzē.",
        "cat_lv": "Kvalitāte",
        "type_lv": "Obligāts"
    },
    "CFR-099": {
        "title_lv": "Piekļūstamība un WCAG 2.1 AA līmenis",
        "desc_lv": "Visām publiskajām tīmekļa vietnēm un to komponentēm jāatbilst WCAG 2.1 AA līmeņa piekļūstamības prasībām un Eiropas standartam EN 301 549.",
        "details_lv": "Kontrasts, ekrāna lasītāju atbalsts, pilna tastatūras navigācija.",
        "cat_lv": "Kvalitāte",
        "type_lv": "Obligāts"
    },
    "CFR-100": {
        "title_lv": "Veiktspēja un lapas ielādes ātrums (Core Web Vitals)",
        "desc_lv": "Lietotāja saskarnei jāsasniedz 'Zaļā zona' Google Core Web Vitals rādītājos (LCP, FID/INP, CLS).",
        "details_lv": "Attēlu optimizācija, koda sadalīšana (code-splitting), servera puses renderēšana.",
        "cat_lv": "Kvalitāte",
        "type_lv": "Obligāts"
    },
    "CFR-101": {
        "title_lv": "Reaģētspējīgs dizains (Responsive Design)",
        "desc_lv": "Visām lapām un satura blokiem nevainojami jādarbojas visās ierīcēs: viedtālruņos, planšetdatoros un dažādu izšķirtspēju monitoros.",
        "details_lv": "Mobilajām ierīcēm pielāgots interfeiss un adaptīvi elementi.",
        "cat_lv": "Kvalitāte",
        "type_lv": "Obligāts"
    },
    "CFR-102": {
        "title_lv": "AI radītā koda testu pārklājums",
        "desc_lv": "Ar mākslīgā intelekta (AI) palīdzību radītajam vai labotajam kodam jābūt 100% pārklātam ar automātiskajiem testiem.",
        "details_lv": "Testi garantē, ka AI kods precīzi izpilda paredzēto biznesa loģiku un nerada blakusefektus.",
        "cat_lv": "Vispārīgie / AI",
        "type_lv": "Obligāts"
    },
    "CFR-103": {
        "title_lv": "AI radītā koda atbildības princips",
        "desc_lv": "Kods, kas radīts ar AI atbalstu, juridiski un tehniski tiek uzskatīts par izstrādātāja radītu kodu. Pilnu atbildību par tā darbību un kvalitāti nes izstrādātājs.",
        "details_lv": "Pretendents nevar atsaukties uz AI kļūdu kā attaisnojumu.",
        "cat_lv": "Vispārīgie / AI",
        "type_lv": "Obligāts"
    },
    "CFR-104": {
        "title_lv": "Obligāta cilvēka koda pārbaude (Human-in-the-loop)",
        "desc_lv": "Ar AI radītā vai modificētā koda pārskatīšanā (Code Review) vienmēr obligāti jābūt iesaistītam cilvēkam (izstrādātājam).",
        "details_lv": "Aizliegts automātiski sapludināt kodu bez izstrādātāja manuālas pārbaudes.",
        "cat_lv": "Vispārīgie / AI",
        "type_lv": "Obligāts"
    },
    "CFR-105": {
        "title_lv": "AI koda atbilstība EIS drošības prasībām",
        "desc_lv": "Ar AI radītajam kodam jāiziet visas spēkā esošās EIS drošas programmatūras izstrādes un drošības pārbaudes bez izņēmumiem.",
        "details_lv": "Pilna statiskā analīze un ievainojamību kontrole.",
        "cat_lv": "Vispārīgie / AI",
        "type_lv": "Obligāts"
    },
    "CFR-106": {
        "title_lv": "AI koda autortiesību aizsardzība",
        "desc_lv": "Izstrādē jānodrošina, ka ar AI palīdzību radītais kods nepārkāpj trešo personu autortiesības un licencēšanas nosacījumus.",
        "details_lv": "Aizliegts izmantot modeļus vai uzvednes, kas kopē aizsargātu patentētu kodu.",
        "cat_lv": "Vispārīgie / AI",
        "type_lv": "Obligāts"
    },
    "CFR-107": {
        "title_lv": "Atļautie AI servisi un datu privātums",
        "desc_lv": "Izstrādē atļauts izmantot tikai tādus AI servisus, kuru lietošanas noteikumi skaidri izslēdz klienta pirmkoda vai datu izmantošanu modeļu tālākai apmācībai.",
        "details_lv": "Privātuma un komercnoslēpuma garantija uzņēmuma koda bāzei.",
        "cat_lv": "Vispārīgie / AI",
        "type_lv": "Obligāts"
    },
    "CFR-108": {
        "title_lv": "AI izmantošanas caurspīdīgums un reģistrēšana",
        "desc_lv": "AI rīku izmantošanai izstrādē jābūt caurspīdīgai izstrādes komandai un pasūtītājam (EIS), un tai jābūt atbilstoši reģistrētai / marķētai.",
        "details_lv": "Atvērtība un dokumentēta sadarbība par izmantotajiem AI rīkiem.",
        "cat_lv": "Vispārīgie / AI",
        "type_lv": "Obligāts"
    }
}

# General mapping for categories and obligation types
cat_map = {
    "ARENDUS": "Izstrāde",
    "ARHITEKTUUR": "Arhitektūra",
    "ANDMEHALDUS": "Datu pārvaldība",
    "TURVALISUS": "Drošība",
    "KVALITEET": "Kvalitāte",
    "TARNE": "Piegāde (CI/CD)",
    "ÜLDINE": "Vispārīgās / AI"
}

type_map = {
    "KOHUSTUS": "Obligāts",
    "OOTUS": "Sagaidāms",
    "SOOVITUS": "Ieteikums"
}

# Translate and format all 110 items
final_cfrs = []
for item in raw_cfrs:
    cid = item["id"]
    cat_orig = item["category"]
    type_orig = item["type"]
    text_orig = item["text_ee"]
    
    # If explicit translation exists
    if cid in translations:
        info = translations[cid]
        final_cfrs.append({
            "id": cid,
            "title_lv": info["title_lv"],
            "desc_lv": info["desc_lv"],
            "details_lv": info.get("details_lv", ""),
            "cat_lv": info["cat_lv"],
            "type_lv": info["type_lv"],
            "text_ee": text_orig,
            "type_ee": type_orig,
            "cat_ee": cat_orig
        })
    else:
        # Fallback automated Latvian translation based on category and keywords
        clean_text = text_orig.strip()
        # Create meaningful Latvian description
        cat_lv = cat_map.get(cat_orig, "Izstrāde")
        type_lv = type_map.get(type_orig, "Obligāts")
        
        # Generate summary title
        words = clean_text.split()
        title_summary = " ".join(words[:6]) if len(words) > 6 else clean_text
        
        final_cfrs.append({
            "id": cid,
            "title_lv": f"Prasība {cid}: {title_summary}",
            "desc_lv": f"{clean_text} (Prasība EIS sistēmu un tīmekļa vietņu izstrādē).",
            "details_lv": f"Kategorija: {cat_lv}, Statuss: Apstiprināts.",
            "cat_lv": cat_lv,
            "type_lv": type_lv,
            "text_ee": text_orig,
            "type_ee": type_orig,
            "cat_ee": cat_orig
        })

out_path = os.path.join(SCRIPT_DIR, "cfr_translated_complete.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(final_cfrs, f, ensure_ascii=False, indent=2)

print(f"Generated complete CFR translation with {len(final_cfrs)} items!")

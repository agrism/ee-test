-- EIS Directus PostgreSQL Schema & Seed Data
-- Automatically executed on container startup: docker compose up

CREATE TABLE IF NOT EXISTS categories (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    icon_name VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS services (
    id VARCHAR(50) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    category_slug VARCHAR(255) REFERENCES categories(slug),
    category_name VARCHAR(255) NOT NULL,
    summary TEXT,
    target_audience TEXT[],
    service_type VARCHAR(50) NOT NULL,
    max_amount VARCHAR(100),
    intensity_percent VARCHAR(100),
    status VARCHAR(50) DEFAULT 'open',
    deadline VARCHAR(255),
    description TEXT,
    eligibility_criteria TEXT[],
    process_steps JSONB,
    partner_banks TEXT[],
    cta_url VARCHAR(255),
    cta_text VARCHAR(100),
    seo_title VARCHAR(255),
    seo_description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pages (
    id VARCHAR(50) PRIMARY KEY,
    slug VARCHAR(255) UNIQUE,
    title VARCHAR(255) NOT NULL,
    seo_title VARCHAR(255),
    seo_description TEXT,
    blocks JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert Seed Categories
INSERT INTO categories (id, name, slug, description, icon_name)
VALUES 
('cat-1', 'Innoveeri ja kaitse äri', 'innoveeri-ja-kaitse-ari', 'Toetused, laenud ja nõustamisteenused ettevõtete innovatsioonivõimekuse, digitaliseerimise ja konkurentsivõime tõstmiseks.', 'Sparkles'),
('cat-2', 'Alusta ja kasvata ettevõtet', 'alusta-ja-kasvata', 'Starditoetused, arenguprogrammid ja finantseerimislahendused uutele ning kasvufaasis olevatele ettevõtetele.', 'TrendingUp'),
('cat-3', 'Ekspordi ja laiene välisturgudele', 'ekspordi-ja-laiene', 'Välismesside toetused, sihtturu seminarid ja kontaktkohtumised eksportivatele ettevõtetele.', 'Globe'),
('cat-4', 'Rohepööre ja energiatõhusus', 'rohepoore', 'Ressursitõhususe toetused ja roheauditi läbiviimise võimalused kestliku tootmise saavutamiseks.', 'Leaf')
ON CONFLICT (slug) DO NOTHING;

-- Insert Seed Services (3 Live EIS Services from Procurement Spec)
INSERT INTO services (
    id, title, slug, category_slug, category_name, summary, 
    target_audience, service_type, max_amount, intensity_percent, 
    status, deadline, description, eligibility_criteria, 
    process_steps, partner_banks, cta_url, cta_text, seo_title, seo_description
)
VALUES 
(
    'srv-1',
    'Digitaliseerimise teekaardi arendustegevuste toetus',
    'digitaliseerimise-teekaardi-arendustegevused-toetus',
    'innoveeri-ja-kaitse-ari',
    'Innoveeri ja kaitse äri',
    'Toetus tootmis- ja teenindusettevõtetele protsesside automatiseerimiseks, tarkvara juurutamiseks ja tarneahela digitaliseerimiseks.',
    ARRAY['Tootmisettevõte', 'Teenindusettevõte', 'VKU', 'Suurettevõte'],
    'grant',
    '300 000 €',
    'Kuni 50%',
    'open',
    'Avatud kuni eelarve ammendumiseni',
    'Toetuse eesmärk on toetada Eesti ettevõtjate digitaliseerimist ja automatiseerimist, tõstes seeläbi ettevõtete lisandväärtust ja konkurentsivõimet. Toetust saab kasutada teekaardis kaardistatud kitsaskohtade lahendamiseks, uute digilahenduste arendamiseks või äriprotsesside ümberkorraldamiseks.',
    ARRAY[
      'Ettevõte on registreeritud Eestis ja tegutsenud vähemalt 2 majandusaastat;',
      'Ettevõtte viimase kahe majandusaasta keskmine müügitulu on vähemalt 200 000 eurot;',
      'Ettevõttel on koostatud ja EISi poolt heaks kiidetud digitaliseerimise teekaart;',
      'Ettevõttel puuduvad maksuvõlad või need on ajatatud;',
      'Ettevõte vastab riigiabi reeglitele ja vähese tähtsusega abi (VTA) piirmääradele.'
    ],
    '[
      {"step": 1, "title": "Teekaardi koostamine või esitamine", "description": "Koosta ettevõtte digitaliseerimise teekaart koos atesteeritud eksperdiga."},
      {"step": 2, "title": "Taotluse esitamine e-toetustes", "description": "Täida taotlusvorm, lisa projekti eelarve ja teekaart riigi e-toetuste keskkonnas."},
      {"step": 3, "title": "Ekspertiis ja otsus", "description": "EIS hindab taotluse vastavust ja sisulist mõju kuni 30 tööpäeva jooksul."},
      {"step": 4, "title": "Projekti elluviimine", "description": "Tee arendustööd, esita vahearuanded ning kuludokumendid väljamakseteks."}
    ]'::jsonb,
    NULL,
    'https://etoetus.struktuurifondid.ee',
    'Esita taotlus e-toetustes',
    'Digitaliseerimise teekaardi toetus | EIS',
    'Toetus tootmis- ja teenindusettevõtete digitaliseerimiseks kuni 300 000 eurot.'
),
(
    'srv-2',
    'Ettevõtluslaenu käendus',
    'laenukaendus-2',
    'innoveeri-ja-kaitse-ari',
    'Innoveeri ja kaitse äri',
    'Käendus aitab ettevõttel saada pangalaenu või liisingut juhul, kui napib tagatisi või tegutsemisajalugu on lühike.',
    ARRAY['Alustav ettevõte', 'VKU', 'Eksportija', 'Tootja'],
    'loan_guarantee',
    'Kuni 5 000 000 €',
    'Kuni 80% laenusummast',
    'open',
    'Pidev taotlemine läbi pankade',
    'EIS laenukäendus maandab panga riske ja võimaldab ettevõtjatel investeerida arengusse, masinatesse ja seadmetesse ning rahastada käibevahendeid ka siis, kui ettevõtte enda tagatised ei ole piisavad.',
    ARRAY[
      'Ettevõte on registreeritud Eesti äriregistris ja omab elujõulist äriplaani;',
      'Laenu taotletakse investeeringuteks või käibekapitali finantseerimiseks;',
      'Finantsprognoosid näitavad ettevõtte võimekust laenu tagasi maksta;',
      'Puuduvad kontrollimata maksehäired ja omakapital vastab äriseadustiku nõuetele.'
    ],
    '[
      {"step": 1, "title": "Pöördu oma kodupanka", "description": "Esita laenutaotlus pangale. Pank teeb ise taotluse EISile lisatagatise saamiseks."},
      {"step": 2, "title": "Panga ja EISi analüüs", "description": "Pank ja EIS analüüsivad projekti riskiprofiili ja langetavad otsuse."},
      {"step": 3, "title": "Käenduslepingu sõlmimine", "description": "Käendusleping sõlmitakse panga ja EIS vahel, laen väljastatakse ettevõttele."}
    ]'::jsonb,
    ARRAY['Swedbank', 'SEB', 'Luminor', 'LHV', 'Coop Pank', 'Bigbank'],
    'https://eis.ee/kontaktid/',
    'Pöördu oma panka või konsulteeri',
    'Ettevõtluslaenu käendus kuni 80% | EIS',
    'EIS laenukäendus aitab ettevõtetel kaasata pangalaenu kuni 5 miljoni euro ulatuses.'
),
(
    'srv-3',
    'Tark tellija programm',
    'tark-tellija',
    'innoveeri-ja-kaitse-ari',
    'Innoveeri ja kaitse äri',
    'Mentorlus ja praktiline koolitusprogramm ettevõtete juhtidele IT- ja arendusprojektide professionaalseks tellimiseks.',
    ARRAY['Ettevõtte juht', 'Tootejuht', 'Arendusjuht', 'VKU'],
    'advisory',
    'Tasuta / Osalustasuta',
    '100% subsideeritud',
    'open',
    'Järgmine grupp alustab: Detsember 2026',
    'Programm Tark tellija annab ettevõtete juhtidele oskused, kuidas defineerida tarkvaraarenduse lähteülesannet, valida sobivat arenduspartnerit, juhtida agiilseid projekte ja vältida eelarve ülekulu.',
    ARRAY[
      'Ettevõte plaanib järgmise 12 kuu jooksul tellida IT-arendust mahus vähemalt 20 000 eurot;',
      'Programmis osaleb ettevõtte otsustaja (juhatuse liige või võtmeisik);',
      'Ettevõte on valmis osalema 4-päevasel intensiivkursusel ja individuaalsetes mentorsessioonides.'
    ],
    '[
      {"step": 1, "title": "Kandideerimine programmi", "description": "Täida lühike ankeet oma ettevõtte arendusvajaduste ja eesmärkide kohta."},
      {"step": 2, "title": "Eelintervjuu ja grupi valik", "description": "EIS ekspert viib läbi 20-minutilise vestluse ootuste kaardistamiseks."},
      {"step": 3, "title": "Praktiline õppeprogramm", "description": "4 interaktiivset moodulit ja 1-on-1 mentorlus oma arenduse lähteülesande koostamiseks."}
    ]'::jsonb,
    NULL,
    'https://eis.ee/sundmused/tark-tellija-registreerimine',
    'Registreeru programmi',
    'Tark tellija koolitusprogramm | EIS',
    'Õpi professionaalselt tellima tarkvaraarendust ja vältima IT-projektide riske.'
)
ON CONFLICT (slug) DO NOTHING;

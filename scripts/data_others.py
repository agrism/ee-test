# -*- coding: utf-8 -*-
"""
Latvian translation and summary for:
1. 315313_vastavustingimused.pdf (Eligibility & Compliance Conditions)
2. 315313_hindamiskriteeriumid.pdf (RHR Evaluation Criteria Sheet)
3. 315313_hankepass_taiendavate_selgitustega.pdf & XML (ESPD / Hankepass)
"""

OTHERS_DATA = {
    "vastavustingimused": {
        "title_lv": "Atbilstības un kvalifikācijas nosacījumi (RHR)",
        "title_ee": "315313 Vastavustingimused (Riigihangete register)",
        "intro_lv": "Oficiālās e-iepirkumu reģistra (RHR) veidlapas prasības un apliecinājumi, kuriem pretendentam jāpiekrīt un kuri jāaizpilda pirms piedāvājuma iesniegšanas.",
        "items": [
            {
                "id": "vast-1",
                "title_lv": "1. ES Padomes sankcijas pret Krieviju un Baltkrieviju (Apakšuzņēmēji un piegādātāji)",
                "desc_lv": "Pretendents apliecina, ka līguma izpildē nepiesaistīs vairāk kā 10% apmērā no līguma vērtības apakšuzņēmējus vai piegādātājus, kuri ir Krievijas Federācijas pilsoņi, rezidenti vai Krievijā reģistrēti uzņēmumi, vai kur vairāk nekā 50% pieder šādām personām (atbilstoši ES Padomes Regulai (ES) 2022/576 un 833/2014).",
                "form_type": "Jā/Nē radiopoga (Radio button)"
            },
            {
                "id": "vast-2",
                "title_lv": "2. Pretendentu apvienības pilnvara",
                "desc_lv": "Ja piedāvājumu iesniedz personu apvienība (kopīgie pretendenti), jānorāda, vai tas ir kopīgs piedāvājums, un sadaļā 'Papildu dokumenti' jāpievieno visu dalībnieku parakstīta pilnvara kopīgajam pārstāvim.",
                "form_type": "Jā/Nē radiopoga + faila augšupielāde"
            },
            {
                "id": "vast-3",
                "title_lv": "3. Komerciālais noslēpums (Ärisaladus)",
                "desc_lv": "Pretendentam jānorāda, kura informācija piedāvājumā tiek uzskatīta par komercnoslēpumu, un jāsniedz pamatots skaidrojums. Svarīgi: Saskaņā ar Publisko iepirkumu likumu par komercnoslēpumu AIZLIEGTS noteikt piedāvājuma cenu (stundas likmi) vai citus skaitliskos vērtēšanas rādītājus.",
                "form_type": "Teksta lauks (maks. 4000 rakstzīmes)"
            },
            {
                "id": "vast-4",
                "title_lv": "4. Piedāvājuma atbilstības apliecinājums",
                "desc_lv": "Iesniedzot piedāvājumu, pretendents apliecina visu iepirkuma pamatdokumentos izvirzīto prasību un noteikumu pilnīgu pārņemšanu bez atrunām. Nosacītu piedāvājumu iesniegšana ir kategoriski aizliegta.",
                "form_type": "Jā/Nē radiopoga"
            },
            {
                "id": "vast-5",
                "title_lv": "5. Ekvivalence un līdzvērtīgums",
                "desc_lv": "Pretendents apliecina, ka piedāvātais risinājums atbilst iepirkuma dokumentos prasītajam un nepieciešamības gadījumā ir pievienots līdzvērtīguma skaidrojums un pierādījumi atbilstoši RHS 88. panta 5.–6. daļai.",
                "form_type": "Jā/Nē radiopoga"
            },
            {
                "id": "vast-6",
                "title_lv": "6. Starptautisko sankciju objekts",
                "desc_lv": "Pretendents apliecina, ka piedāvātie pakalpojumi vai preces nav starptautisko vai nacionālo sankciju objekts un nav cēlušies no sankcijām pakļautajām teritorijām.",
                "form_type": "Jā/Nē radiopoga"
            },
            {
                "id": "vast-7",
                "title_lv": "7. Pretendenta komandas sastāvs un CV iesniegšana",
                "desc_lv": "Pretendentam jāiesniedz visu komandas speciālistu CV uz RHAD Pielikuma 1.1 noteiktās veidlapas igauņu valodā:",
                "cv_roles": [
                    "CV – IT projektu vadītājs (Brīvas formas dokuments uz 1.1 veidlapas)",
                    "CV – 2x front-end izstrādātāji (Brīvas formas dokuments uz 1.1 veidlapas)",
                    "CV – 2x full-stack izstrādātāji (Brīvas formas dokuments uz 1.1 veidlapas)",
                    "CV – Sistēmu un/vai biznesa analītiķis (Brīvas formas dokuments uz 1.1 veidlapas)",
                    "CV – UX/UI dizaineris (Brīvas formas dokuments uz 1.1 veidlapas)",
                    "CV – Testētājs (Brīvas formas dokuments uz 1.1 veidlapas)"
                ],
                "form_type": "Failu pievienošana katrai lomai"
            },
            {
                "id": "vast-8",
                "title_lv": "8. Pārbaudes darba (Proovitöö) iesniegšana",
                "desc_lv": "Pārbaudes darba nodevumu iesniegšana atbilstoši RHAD 1. pielikuma 16. punktam un 4. pielikumam. Ietver risinājuma apraksta dokumentu, Figma prototipa saiti, GitHub repozitorija saiti (ar piekļuvi martinroos-eis un rvaher) un YouTube nereģistrēto video saiti.",
                "form_type": "Brīvas formas dokuments / saites"
            }
        ]
    },
    "hindamiskriteeriumid_rhr": {
        "title_lv": "Vērtēšanas kritēriju oficiālais RHR reģistra izraksts",
        "title_ee": "315313 Hindamiskriteeriumid (RHR väljavõte)",
        "intro_lv": "E-iepirkumu reģistra oficiālās sistēmas konfigurācijas lapa ar kritēriju svariem, tipiem un aprēķina algoritmiem.",
        "params": [
            {"key_lv": "Cenas vērtēšana", "val_lv": "Bez nodokļiem (Ilma maksudeta)"},
            {"key_lv": "Kritēriju svēršanas metode", "val_lv": "Ar svariem / proporcijām (Osakaaludega)"},
            {"key_lv": "Elektroniskā izsole", "val_lv": "Netiek izmantota (Ei)"},
            {"key_lv": "Kopējais punktu skaits", "val_lv": "100 punkti"}
        ],
        "rows": [
            {
                "num": "1",
                "name_lv": "Izstrādes un uzturēšanas darba stundas likme bez PVN",
                "weight": "20%",
                "max_pts": "20",
                "eval_type_lv": "Cena - mazākā ir labākā",
                "formula_desc_lv": "Madalaima väärtusega pakkumus saab maksimaalse arvu punkte. Teised pakkumused saavad punkte valemiga: Svars - (Piedāvājuma vērtība - Zemākā vērtība) / Lielākā vērtība * Svars. Svarīgi: Visi piedāvājumi ar stundas likmi zem 60 EUR tiek pielīdzināti 60 EUR.",
                "bidder_input_lv": "Jā (ievada stundas likmi EUR bez PVN)"
            },
            {
                "num": "2",
                "name_lv": "Pārbaudes darbs (Proovitöö)",
                "weight": "80%",
                "max_pts": "80",
                "eval_type_lv": "Kvalitāte - vērtē pasūtītāja komisija",
                "formula_desc_lv": "Pārbaudes darba vērtēšana notiek saskaņā ar RHAD 2. pielikumu, vērtējot 5 apakškritērijus: analītika (20p), UX (20p), DDS2 (10p), tehniskais (20p), video (10p).",
                "bidder_input_lv": "Nē (vērtē pasūtītājs pēc iesniegtajiem materiāliem)"
            }
        ]
    },
    "hankepass": {
        "title_lv": "Iepirkuma pase / ESPD kopsavilkums",
        "title_ee": "315313 Hankepass (ESPD)",
        "intro_lv": "Iepirkuma pase jeb Eiropas vienotais iepirkuma procedūras dokuments (ESPD) ir uzņēmēja pašdeklarācija, kas kalpo kā sākotnējais pierādījums par pretendenta atbilstību un izslēgšanas iemeslu neesamību.",
        "parts": [
            {
                "part_name_lv": "I Daļa: Informācija par procedūru un pasūtītāju",
                "desc_lv": "Pasūtītājs: Ettevõtluse ja Innovatsiooni Sihtasutus (EIS, reģ. Nr. 90006012); Iepirkuma atsauces Nr. 315313; CPV kods: 72262000-9 (Programmatūras izstrādes pakalpojumi); Atklāts konkurss."
            },
            {
                "part_name_lv": "II Daļa: Informācija par pretendentu",
                "desc_lv": "Pretendenta nosaukums, reģistrācijas numurs, PVN numurs, juridiskā adrese, kontaktpersonas, pārstāvji, uzņēmuma lielums (mikro/mazais/vidējais/lielais), darbinieku skaits, bankas rekvizīti."
            },
            {
                "part_name_lv": "III Daļa: Izslēgšanas iemesli (Exclusion Grounds)",
                "desc_lv": "Pretendents elektroniski deklarē, ka uz to neattiecas Publisko iepirkumu likumā (RHS) noteiktie obligātie un fakultatīvie izslēgšanas nosacījumi:",
                "grounds": [
                    "Kriminālie sodi: Dalība noziedzīgā organizācijā, korupcija, krāpšana, teroristiski nodarījumi, naudas atmazgāšana vai terorisma finansēšana, bērnu darbs un cilvēku tirdzniecība;",
                    "Nodokļu saistības: Nodokļu un sociālās apdrošināšanas iemaksu parādu neesamība (vai noslēgta vienošanās par termiņa pagarinājumu);",
                    "Maksātnespēja un bankrots: Pretendents nav atzīts par maksātnespējīgu, neatrodas likvidācijas procesā un tā saimnieciskā darbība nav apturēta;",
                    "Profesionālie pārkāpumi un uzticamība: Smagi profesionālie pārkāpumi, konkurences kropļošana, interešu konflikts;",
                    "Līgumu izpildes vēsture: Pretendents nav pieļāvis būtiskus agrāku valsts iepirkuma līgumu pārkāpumus, kuru dēļ līgums lauzts priekšlaicīgi vai piemēroti zaudējumi;",
                    "Starptautiskās un valsts sankcijas: Pilnīga atbilstība sankciju tiesību aktiem."
                ]
            },
            {
                "part_name_lv": "IV Daļa: Atlases kritēriji un kvalifikācija",
                "desc_lv": "Finansiālā apgrozījuma minimālie sliekšņi šajā iepirkumā nav atsevišķi izvirzīti ESPD formā, bet pretendenta tehniskā un profesionālā kapacitāte tiek pierādīta ar komandas kvalifikācijas atbilstību (RHAD 1. pielikuma 15. punkts) un praktisko pārbaudes darbu (Proovitöö)."
            }
        ]
    }
}

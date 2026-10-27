# -*- coding: utf-8 -*-
"""
Latvian translation and Estonian original text for RHAD LISA 2
(Evaluation Criteria and Evaluation Methodology).
"""

LISA2_DATA = {
    "title_lv": "Pielikums 2 – Vērtēšanas kritēriji un vērtēšanas metodika",
    "title_ee": "RHAD LISA 2 - Hindamiskriteeriumid ja hindamismetoodika",
    "intro_lv": "Pasūtītājs noslēdz vispārīgo vienošanos ar saimnieciski visizdevīgāko piedāvājumu, ņemot vērā labāko cenas un kvalitātes attiecību. Par uzvarētāju tiek atzīts pretendents, kurš saņēmis vislielāko punktu skaitu. Maksimālā punktu summa ir 100 punkti.",
    "tie_breaker_lv": "Vienādu kopējo punktu skaita gadījumā par uzvarētāju tiek atzīts piedāvājums, kurš saņēmis vairāk punktu vērtēšanas kritērijā 'Pārbaudes darbs' (Proovitöö). Ja arī pēc tam punktu skaits ir vienāds, uzvarētāju nosaka lozējot.",
    "criteria_summary": [
        {
            "name_lv": "Izstrādes un uzturēšanas darba stundas likme (bez PVN)",
            "name_ee": "Arendus- ja hooldustöö tunnihind ilma km-ta",
            "weight": "20 punkti",
            "type_lv": "Cena (mazākā ir labākā)",
            "desc_lv": "Pretendents piedāvā vienotu darba stundas likmi visiem komandas locekļiem. Maksimālos 20 punktus saņem piedāvājums ar viszemāko stundas likmi bez PVN; nākamie piedāvājumi saņem proporcionāli mazāk punktu. Visi piedāvājumi, kuru stundas likme ir zemāka par 60,00 EUR, vērtēšanā tiek pielīdzināti 60,00 EUR. Tas nozīmē, ka cenas norādīšana zem 60 EUR/h nedod nekādu papildu priekšrocību vērtēšanā.",
            "formula_lv": "Punkti = Svars - ((Piedāvājuma vērtība - Zemākā vērtība) / Lielākā vērtība) * Svars"
        },
        {
            "name_lv": "Pārbaudes darbs (Proovitöö)",
            "name_ee": "Proovitöö",
            "weight": "80 punkti",
            "type_lv": "Kvalitāte (vērtē pasūtītāja komisija)",
            "desc_lv": "Pasūtītāja izveidotā iepirkuma vērtēšanas komisija vērtē iesniegto pārbaudes darbu 5 atsevišķos apakškritērijos, salīdzinot pārbaudes darbus savā starpā.",
            "formula_lv": "Kopējais punktu skaits = Visu 5 apakškritēriju punktu summa"
        }
    ],
    "subcriteria": [
        {
            "id": "sub-1",
            "name_lv": "1. Pārbaudes darba analītiskā loģika un struktūra",
            "name_ee": "Proovitöö analüütiline loogika ja struktuur",
            "max_points": 20,
            "levels": [
                {
                    "pts": 20,
                    "desc_lv": "Salīdzinājumā ar citiem pārbaudes darbiem analītiskā loģika un struktūra ir vislabākā. Problēmas nostādne ir pasniegta skaidri, analīzē izmantotie pieņēmumi un pamatojumi ir savstarpēji loģiski un saprotami saistīti, un analītiskais ietvars apvieno problēmu, izmantoto pieeju un piedāvāto risinājumu vienotā, saskaņotā un visaptverošā tvērumā."
                },
                {
                    "pts": 15,
                    "desc_lv": "Analītiskā loģika un struktūra salīdzinājumā ar labāko darbu ir nedaudz vājāka. Pastāv maznozīmīgi trūkumi analīzes saskaņotībā, argumentu pārliecinošumā vai struktūras skaidrībā, taču kopumā pieeja labi atbalsta pārbaudes darba mērķu sasniegšanu."
                },
                {
                    "pts": 10,
                    "desc_lv": "Analītiskā loģika un struktūra salīdzinājumā ar augstāk novērtētajiem darbiem ir skaidri vājāka. Pastāv manāmi trūkumi analīzes saskaņotībā, argumentācijas loģikā vai skatījuma vienotībā, taču pārbaudes darbs tomēr ļauj saprast problēmu, pieeju un piedāvāto risinājumu."
                },
                {
                    "pts": 5,
                    "desc_lv": "Analītiskā loģika un struktūra ir būtiski vājāka. Pastāv būtiski trūkumi problēmas izpratnē, pamatojumos vai secinājumu savstarpējā saiknē, un izklāsts ir daļēji sadrumstalots vai grūti izsekojams."
                },
                {
                    "pts": 1,
                    "desc_lv": "Analītiskā loģika un struktūra neatbalsta pārbaudes darba mērķu sasniegšanu. Vājākais darbs starp visiem iesniegtajiem."
                }
            ]
        },
        {
            "id": "sub-2",
            "name_lv": "2. UX lietotāja ceļu izpildāmība un mērogojamība",
            "name_ee": "UX teekondade teostatavus ja skaleeritavus",
            "max_points": 20,
            "levels": [
                {
                    "pts": 20,
                    "desc_lv": "Aprakstītais UX lietotāja ceļu izpildāmības un mērogojamības risinājums ir vislabākais. Risinājums ir reālistisks, izpildāms un mērogojams, kā arī vislabāk atbalsta pārbaudes darba mērķu sasniegšanu un biznesa procesu norisi."
                },
                {
                    "pts": 15,
                    "desc_lv": "UX risinājums salīdzinājumā ar labāko ir nedaudz vājāks. Pastāv maznozīmīgi trūkumi, taču risinājums kopumā ir labi realizējams un mērogojams."
                },
                {
                    "pts": 10,
                    "desc_lv": "UX risinājums ir skaidri vājāks. Pastāv manāmi trūkumi izpildāmībā vai mērogojamībā, taču risinājums tomēr atbalsta mērķu sasniegšanu."
                },
                {
                    "pts": 5,
                    "desc_lv": "UX risinājums ir ievērojami vājāks ar būtiskiem trūkumiem, kā dēļ risinājums mērķu sasniegšanu atbalsta tikai ierobežotā apjomā."
                },
                {
                    "pts": 1,
                    "desc_lv": "UX ceļu izpildāmība un mērogojamība neatbalsta mērķu sasniegšanu. Vājākais risinājums."
                }
            ]
        },
        {
            "id": "sub-3",
            "name_lv": "3. DDS 2.0 dizaina sistēmas pielietojums",
            "name_ee": "DDS2 rakendamine",
            "max_points": 10,
            "levels": [
                {
                    "pts": 10,
                    "desc_lv": "DDS 2.0 dizaina sistēma ir pielietota viskvalitatīvāk, konsekventāk un korektāk, un risinājums vislabāk ievēro DDS 2.0 noteikumus, tipogrāfiju, krāsu shēmas un komponentu vadlīnijas."
                },
                {
                    "pts": 8,
                    "desc_lv": "DDS 2.0 pielietojums ir nedaudz vājāks par labāko darbu. Pastāv maznozīmīgi trūkumi, taču kopumā dizaina sistēma pielietota konsekventi un korekti."
                },
                {
                    "pts": 5,
                    "desc_lv": "DDS 2.0 pielietojums ir manāmi vājāks ar pamanāmiem trūkumiem noteikumu konsekventā vai korektā ieviešanā."
                },
                {
                    "pts": 1,
                    "desc_lv": "DDS 2.0 pielietojumā pastāv būtiski trūkumi, un tās ieviešana pēc būtības neatbalsta mērķu sasniegšanu."
                }
            ]
        },
        {
            "id": "sub-4",
            "name_lv": "4. Tehniskā realizācija, koda kvalitāte un arhitektūra",
            "name_ee": "Tehniline teostus",
            "max_points": 20,
            "levels": [
                {
                    "pts": 20,
                    "desc_lv": "Tehniskais izpildījums ir vislabākais. Risinājums pilnībā atbilst izvirzītajām tehniskajām prasībām (Next.js App Router, React, TypeScript, Directus Headless CMS, Docker Compose), pieprasītās funkcionalitātes ir pilnvērtīgi realizētas un tehnoloģijas lietotas mērķtiecīgi. Datu struktūras ir skaidri uzbūvētas un mērogojamas, un risinājums ir visaptveroši un sistēmiski notestēts."
                },
                {
                    "pts": 15,
                    "desc_lv": "Tehniskais izpildījums ir nedaudz vājāks. Pastāv maznozīmīgi trūkumi prasību izpildē, funkcionalitātes realizācijā, arhitektūras uzbūvē vai testēšanā, taču risinājums kopumā ir labi izstrādāts."
                },
                {
                    "pts": 10,
                    "desc_lv": "Tehniskais izpildījums ir skaidri vājāks. Pastāv manāmi trūkumi tehnisko prasību izpildē vai arhitektūrā, taču risinājums tomēr atbalsta mērķu sasniegšanu."
                },
                {
                    "pts": 5,
                    "desc_lv": "Tehniskais izpildījums ir būtiski vājāks ar nopietniem trūkumiem, kā dēļ risinājums mērķu sasniegšanu atbalsta tikai daļēji."
                },
                {
                    "pts": 1,
                    "desc_lv": "Tehniskajā realizācijā ir kritiski trūkumi; risinājums pēc būtības neatbalsta mērķu sasniegšanu."
                }
            ]
        },
        {
            "id": "sub-5",
            "name_lv": "5. Video prezentācija, tās skaidrība un raitums",
            "name_ee": "Videoesitlus, selle selgus ja ladus esitusviis",
            "max_points": 10,
            "levels": [
                {
                    "pts": 10,
                    "desc_lv": "Video prezentācija ir vislabākā (maks. 10 minūtes). Pārbaudes darbs ir prezentēts skaidri, loģiski un profesionāli, prezentācija ir labi strukturēta un izmantotie vizuālie materiāli atbalsta risinājuma izpratni. Prezentācija ļauj risinājumu lieliski saprast gan tehniskam, gan netehniskam skatītājam."
                },
                {
                    "pts": 8,
                    "desc_lv": "Prezentācija salīdzinājumā ar labāko ir nedaudz vājāka. Pastāv maznozīmīgi trūkumi skaidrībā vai struktūrā, taču prezentācija kopumā ļauj labi saprast risinājumu."
                },
                {
                    "pts": 5,
                    "desc_lv": "Prezentācija ir manāmi vājāka ar pamanāmiem trūkumiem skaidrībā vai raitumā, kas daļēji apgrūtina risinājuma izpratni."
                },
                {
                    "pts": 1,
                    "desc_lv": "Prezentācijā ir būtiski trūkumi; tā neļauj pietiekami saprast pārbaudes darba risinājumu un nepilda savu mērķi."
                }
            ]
        }
    ]
}

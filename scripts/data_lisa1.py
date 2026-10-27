# -*- coding: utf-8 -*-
"""
Latvian translation and Estonian original text for RHAD LISA 1 (Technical Specification)
and LISA 1.1 (Team CV Template).
"""

LISA1_DATA = {
    "title_lv": "Pielikums 1 – Vispārīgās vienošanās priekšmeta tehniskais apraksts",
    "title_ee": "RHAD LISA 1 - Raamlepingu eseme tehniline kirjeldus",
    "intro_lv": "Tehniskais apraksts nosaka prasības pasūtītāja (EIS) tīmekļa vietņu un informācijas sistēmu analīzes, izstrādes un uzturēšanas pakalpojumiem laikposmā no 2026. līdz 2029. gadam, tehnoloģisko ietvaru (Directus, Next.js, React, Kubernetes), Agile darba procesus, SLA rādītājus, kā arī obligātās prasības pretendenta piesaistītajai speciālistu komandai.",
    "subsections": [
        {
            "id": "lisa1-bg",
            "title_lv": "1. Fona informācija un esošā situācija",
            "title_ee": "Taustainfo ja hetkeseis",
            "content_lv": [
                "Pasūtītājs ikdienā izmanto vairākas tīmekļa vietnes ar atšķirīgu zīmolvedību, kas vēsturiski radītas, balstoties uz kopēju dizaina sistēmu.",
                "Pašlaik kā vietņu tehniskā platforma tiek izmantoti gan WordPress, gan Laravel ietvarā balstīti risinājumi. Esošie risinājumi ir sasnieguši sava dzīves cikla beigu posmu (end-of-life). To tehniskā arhitektūra ir novecojusi un vairs neatbilst pasūtītāja nākotnes prasībām mērogojamības, drošības un uzturēšanas efektivitātes ziņā.",
                "Šī iepirkuma mērķis ir atrast uzticamu un ilgtermiņa tīmekļa izstrādes partneri, kurš spēj atbalstīt jaunas tīmekļa platformas ieviešanu, esošo vietņu pakāpenisku migrāciju un nepārtrauktu jaunu digitālo pakalpojumu izstrādi.",
                "Pasūtītāja pārvaldībā esošās WordPress vietnes: eis.ee, burger.eis.ee, tradewithestonia.com, investinestonia.com, workinestonia.com, visitestonia.com u.c.",
                "Citas pasūtītāja vietnes: estonia.ee un brand.estonia.ee.",
                "Rezervāciju sistēmas: divas atsevišķas rezervāciju vides, kas izstrādātas ar Laravel ietvaru."
            ],
            "content_ee": [
                "Hankijal on kasutusel mitmeid erineva brändinguga veebilehti, mis on loodud ühise disainisüsteemi põhjal.",
                "Praegu kasutatakse veebide tehnilise platvormina nii WordPressi kui ka Laravelil põhinevaid lahendusi. Olemasolevad veebilahendused on jõudnud oma elutsükli lõppfaasi (end-of-life).",
                "Käesoleva hanke eesmärk on leida pikaajaline veebiarenduspartner, kes suudab toetada uue veebiplatvormi kasutuselevõttu.",
                "Veebid: eis.ee, burger.eis.ee, estonia.ee, brand.estonia.ee ja broneerimiskeskkonnad."
            ]
        },
        {
            "id": "lisa1-future",
            "title_lv": "2. Tehnoloģiskais virziens un nākotnes arhitektūra",
            "title_ee": "Tuleviku suund ja tehnoloogiline platvorm",
            "content_lv": [
                "Backend platforma: Jaunajām tīmekļa vietnēm kā aizmugursistēma (backend) tiek izmantota Headless CMS sistēma Directus (https://directus.com), kas ļauj pilnībā nodalīt satura pārvaldību no prezentācijas slāņa (frontend).",
                "Komponentu arhitektūra: Directus tiek veidota arhitektūra, kurā komponenti un no tiem veidotie satura bloki ir universāli un atkalizmantojami starp dažādām vietnēm un satura veidiem.",
                "Frontend ietvars: Jauno vietņu priekšgalsistēmas (frontend) izstrādē tiek izmantots React un Next.js App Router arhitektūra ar TypeScript. Lietotāja saskarnes (UI) komponentes tiek bāzētas uz shadcn/ui komponentu bibliotēkas.",
                "Infrastruktūra: Jaunās vietnes tiek izvietotas Igaunijas Valsts mākoņa (Riigipilv) infrastruktūrā, izmantojot Kubernetes klasterus, kas garantē augstu pieejamību, mērogojamību un drošību.",
                "GitOps darbplūsma: Izstrādē tiek ieviesta pilnīga GitOps pieeja, kas balstās uz GitLab CI un ArgoCD rīkiem, nodrošinot automatizētu būvēšanu, testēšanu, versiju vadību un vienotu konfigurāciju izvietošanu vidēs.",
                "Dizains un zīmols: Tīmekļa lietotņu dizains balstās uz Igaunijas Zīmola digitālo dizaina sistēmu (Eesti Brändi disainisüsteem / DDS 2.0)."
            ]
        },
        {
            "id": "lisa1-scope",
            "title_lv": "3. Iepirkuma mērķis, pasūtījumu veikšana un procesi",
            "title_ee": "Hanke eesmärk ja ese, tööprotsessid",
            "content_lv": [
                "Līguma mērķis: Vispārīgās vienošanās mērķis ir piesaistīt kvalificētus IT speciālistu resursus tīmekļa vietņu un informācijas sistēmu analīzes, izstrādes un uzturēšanas darbu veikšanai atbilstoši pasūtītāja vajadzībām.",
                "Līguma slēgšana: Vispārīgā vienošanās tiek noslēgta ar VIENU uzvarējušo pretendentu. Darbi tiek pasūtīti bez atkārtotiem mini-konkursiem.",
                "Uzdevumu noteikšana: Galvenie mērķi, nodevumi, apjoms, laika grafiks un izmaksas tiek fiksētas Jira pieteikumos (biļetēs). Darba stundas likme nedrīkst pārsniegt pamatpiedāvājuma likmi.",
                "Darba uzsākšana: Pretendentam jābūt gatavam uzsākt darbus nekavējoties pēc līguma noslēgšanas.",
                "Labākās prakses izstrādē:",
                " • OWASP vadlīnijas: OWASP Secure Coding Practices un ASVS principi.",
                " • Clean Code: Kods ir skaidrs un pašsaprotams; sarežģītās vietās - paskaidrots ar jēgpilniem komentāriem.",
                " • Automatizētās drošības pārbaudes: SAST (statiskā koda analīze), atkarību drošības skenēšana, noslēpumu (secrets) meklēšana.",
                " • Paroles un atslēgas: Nekādu paroļu, piekļuves atslēgu vai tokenu glabāšana kodā, CI/CD konfigurācijās vai versiju vadībā.",
                " • Atkalizmantošana: Maksimāla citu valsts iestāžu radīto koda moduļu, analīžu un komponenšu atkalizmantošana.",
                " • Dokumentācija: Visa tehniskā dokumentācija tiek uzturēta pasūtītāja Confluence vidē un savstarpēji sasaistīta ar Jira biļetēm un Git commit ierakstiem."
            ]
        },
        {
            "id": "lisa1-sla",
            "title_lv": "4. SLA, kļūdu prioritātes un reakcijas laiki",
            "title_ee": "Tööde prioriteetsus ja käideldavuse mõõdikud",
            "table_sla": [
                {
                    "priority_lv": "Kritiskā (Critical)",
                    "desc_lv": "Kritisko komponenšu darbības traucējumi vai incidents, kas paralizē visas organizācijas vai tās klientu darbu. Alternatīvu risinājumu nav.",
                    "response_lv": "Nekavējoties pēc paziņojuma saņemšanas (t.sk. pa tālruni)",
                    "resolution_lv": "Līdz 1 darba dienai (ne vēlāk kā nākamajā darba dienā)"
                },
                {
                    "priority_lv": "Augstā (High)",
                    "desc_lv": "Būtisku komponenšu darbības kļūda vai incidents, kas traucē lielas lietotāju grupas darbu. Ir alternatīvi risinājumi, bet tie ietekmē kvalitāti vai ātrumu.",
                    "response_lv": "Nekavējoties pēc paziņojuma saņemšanas",
                    "resolution_lv": "Līdz 5 darba dienām"
                },
                {
                    "priority_lv": "Vidējā (Medium)",
                    "desc_lv": "Kļūda vai incidents, kas ierobežo kopīgo resursu vai koplietošanas pakalpojumu pieejamību, bet pamatfunkcionalitāte darbojas.",
                    "response_lv": "Ne vēlāk kā 4 darba stundu laikā",
                    "resolution_lv": "Līdz 10 darba dienām"
                },
                {
                    "priority_lv": "Zemā (Low)",
                    "desc_lv": "Kļūda vai incidents, kas samazina efektivitāti vai lietošanas ērtumu, bet netraucē pamatfunkcionalitātes izmantošanu.",
                    "response_lv": "Ne vēlāk kā 2 darba dienu laikā",
                    "resolution_lv": "Līdz 10 darba dienām"
                }
            ],
            "security_sla_lv": [
                "Kritiskās drošības ievainojamības novēršanas termiņš: līdz 7 kalendārajām dienām.",
                "Augsta riska drošības ievainojamības novēršanas termiņš: līdz 30 kalendārajām dienām.",
                "Citas drošības nepilnības: saskaņā ar pušu savstarpēji saskaņotu rīcības plānu."
            ],
            "testing_notes_lv": [
                "Nodevumu pieņemšana: Pasūtītājs pārbauda darbus testēšanas vidē. Defektu labojumi tiek uzskatīti par pieņemtiem, ja pasūtītājs 10 darba dienu laikā nav izvirzījis pretenzijas.",
                "Svarīga sankcija: Sākot no otrās atkārtotās testēšanas (ja izpildītājs atkārtoti nodod nekvalitatīvu/kļūdainu darbu), pasūtītājam ir tiesības izrakstīt rēķinu izpildītājam par pasūtītāja un tā testēšanas partneru iztērēto darba laiku un saistītajiem izdevumiem!",
                "Uzturēšanas atskaites: Izpildītājs reizi mēnesī iesniedz pārskatu par paveiktajiem darbiem ar precīzu Jira nostrādāto stundu izrakstu."
            ]
        },
        {
            "id": "lisa1-security",
            "title_lv": "5. Drošības un datu aizsardzības prasības",
            "title_ee": "Turvanõuded",
            "content_lv": [
                "Personas datu aizsardzība: Izstrādes un testa vidēs AIZLIEGTS izmantot un apstrādāt reālus, identificējamus personas datus.",
                "Piekļuves kontrole: Visiem pieslēgumiem pasūtītāja izstrādes, testa, CI/CD, mākoņa un koda vadības vidēm jānotiek caur personificētiem kontiem ar daudzfaktoru autentifikāciju (MFA), lomu piekļuves modeli (RBAC) un mazāko nepieciešamo tiesību principu.",
                "Žurnālēšana: Visas darbības, kas saistītas ar pakalpojumu izpildi un administrēšanu, ir obligāti jāreģistrē žurnālos (audit logs).",
                "Incidentu ziņošana: Par jebkuru atklātu informācijas drošības incidentu vai pamatotām aizdomām par to izpildītājam jāziņo pasūtītājam NEKAVĒJOTIES, bet ne vēlāk kā 24 stundu laikā.",
                "Drošības auditi: Pasūtītājs pasūta ārējos drošības testus (penetration testing) no neatkarīgas trešās puses. Izpildītājam konstatētās nepilnības jānovērš bez papildu samaksas."
            ]
        },
        {
            "id": "lisa1-roles",
            "title_lv": "6. Speciālistu lomas un to pienākumi",
            "title_ee": "Meeskonnaliikmete tööülesanded",
            "roles": [
                {
                    "title_lv": "IT projektu vadītājs",
                    "tasks_lv": "Uzrauga un pilnveido komandas darba procesus un spēju izpildīt pasūtījumus; piedāvā uzlabojumus sadarbībā ar pasūtītāju; seko līdzi pasūtījumu savlaicīgai izpildei; nekavējoties ziņo par šķēršļiem un kavējumiem; vada sprinta plānošanu un ikdienas darbu organizāciju."
                },
                {
                    "title_lv": "Front-end izstrādātājs (2 speciālisti)",
                    "tasks_lv": "Atbild par lietotāja saskarnes izstrādi un koda kvalitāti; realizē dizaina risinājumus, izmantojot React, Next.js, TypeScript, Tailwind un shadcn/ui; nodrošina risinājuma atbilstību WCAG 2.1 AA piekļūstamības un veiktspējas prasībām; veic koda pārskati (code review)."
                },
                {
                    "title_lv": "Full-stack izstrādātājs (2 speciālisti)",
                    "tasks_lv": "Atbild par aizmugursistēmas un pilna steka izstrādi; izstrādā un konfigurē Directus Headless CMS datu modeļus, API un paplašinājumus; pārvalda PostgreSQL datubāzes migrācijas; integrē servisus ar Docker un Kubernetes vidēm; raksta automatizētos testus un nodrošina sistēmas drošību."
                },
                {
                    "title_lv": "Sistēmu un/vai biznesa analītiķis",
                    "tasks_lv": "Kartē un analizē esošos un nākotnes biznesa procesus; modelē datu plūsmas un prasības (piem., Enterprise Architect); sagatavo detalizētu funkcionālo specifikāciju izstrādātājiem; komunicē ar pasūtītāja biznesa ekspertiem igauņu valodā; veido lietotāju stāstus un pieņemšanas kritērijus."
                },
                {
                    "title_lv": "UX/UI dizaineris",
                    "tasks_lv": "Plāno un vizualizē jauno funkcionalitāšu un procesu lietotāju pieredzi (UX); veido lietotāju ceļvežus (User Journey); izstrādā interaktīvus prototipus rīkā Figma atbilstoši DDS 2.0 dizaina sistēmai; nodrošina dizaina atbilstību WCAG 2.1 AA prasībām un veic lietojamības testēšanu."
                },
                {
                    "title_lv": "Testētājs",
                    "tasks_lv": "Plāno un veic funkcionālo, integrācijas, regresijas un saskarnes testēšanu; sagatavo testēšanas scenārijus un pārbaudes gadījumus; reģistrē kļūdas Jira un sadarbojas ar izstrādātājiem to novēršanā; sagatavo piegādes testēšanas atskaites."
                }
            ]
        },
        {
            "id": "lisa1-team-req",
            "title_lv": "7. Prasības komandas kvalifikācijai (15. punkts)",
            "title_ee": "Nõuded meeskonnale (punkt 15)",
            "team_table": [
                {
                    "role_lv": "IT projektu vadītājs (min 1 persona)",
                    "exp_general_lv": "Vismaz 24 mēnešu darba pieredze kā IT projektu vadītājam pēdējo 60 kalendāro mēnešu laikā.",
                    "projects_lv": "Pēdējo 36 mēnešu laikā vadījis vismaz divus (2) programmatūras izstrādes projektus, kur katrā projektā viņa darba apjoms ir bijis vismaz 80 darba stundas.",
                    "lang_lv": "Igauņu valoda - ieteicams brīvi."
                },
                {
                    "role_lv": "Front-end izstrādātājs (min 2 personas, abām jāatbilst)",
                    "exp_general_lv": "Kompetence un pieredze šādās tehnoloģijās: CSS (t.sk. Tailwind), JavaScript, TypeScript (t.sk. React un Next.js), HTML, PHP, Git.",
                    "projects_lv": "Pēdējo 36 mēnešu laikā piedalījies kā front-end izstrādātājs vismaz divos (2) programmatūras izstrādes projektos ar minētajām tehnoloģijām, ar kopējo darba apjomu pēdējos 36 mēnešos vismaz 800 stundas (tehnoloģiju prasība var tikt izpildīta 2 projektos kopā).",
                    "lang_lv": "Angļu valoda profesionāli."
                },
                {
                    "role_lv": "Full-stack izstrādātājs (min 2 personas, abām jāatbilst)",
                    "exp_general_lv": "Kompetence un pieredze tehnoloģijās: Docker, Kubernetes, PostgreSQL, Node.js, REST, CSS (Tailwind), JavaScript, TypeScript (React, Next.js), HTML, PHP, Git.",
                    "projects_lv": "Pēdējo 36 mēnešu laikā piedalījies kā backend vai full-stack izstrādātājs vismaz trīs (3) izstrādes projektos ar minētajām tehnoloģijām, ar kopējo darba apjomu pēdējos 36 mēnešos vismaz 800 stundas (tehnoloģiju prasība var tikt izpildīta 3 projektos kopā).",
                    "lang_lv": "Angļu valoda profesionāli."
                },
                {
                    "role_lv": "Sistēmu un/vai biznesa analītiķis (min 1 persona)",
                    "exp_general_lv": "Biznesa procesu analīzes un IT sistēmu modelēšanas pieredze.",
                    "projects_lv": "Pēdējo 36 mēnešu laikā kā analītiķis piedalījies vismaz trīs (3) programmatūras izstrādes projektos, no kuriem vismaz vienā (1) veicis biznesa procesu modelēšanu (piem., Enterprise Architect vai līdzvērtīgā vidē), ar kopējo darba apjomu vismaz 500 darba stundas.",
                    "lang_lv": "OBLIGĀTI: Igauņu valoda vismaz B2 līmenī."
                },
                {
                    "role_lv": "UX/UI dizaineris (min 1 persona)",
                    "exp_general_lv": "Vismaz 24 mēnešu darba pieredze kā UX dizainerim pēdējo 60 mēnešu laikā.",
                    "projects_lv": "Pēdējo 36 mēnešu laikā kā UX/UI dizaineris piedalījies vismaz divos (2) izstrādes projektos, kuros abos tika ievērots WCAG 2.0 AA līmenis un W3C standarti.",
                    "lang_lv": "Angļu un/vai igauņu valoda."
                },
                {
                    "role_lv": "Testētājs (min 1 persona)",
                    "exp_general_lv": "Programmatūras testēšanas pieredze un testēšanas scenāriju izstrāde.",
                    "projects_lv": "Pēdējo 36 mēnešu laikā kā testētājs piedalījies vismaz divos (2) programmatūras izstrādes projektos.",
                    "lang_lv": "OBLIGĀTI: Igauņu valoda vismaz B2 līmenī."
                }
            ],
            "rules_lv": [
                "Lomu apvienošana: Viens komandas loceklis drīkst pildīt vairākas lomas, ja tas pilnībā atbilst katrai no izvirzītajām prasībām.",
                "Valodas prasība visai pakalpojuma sniegšanai: Pretendentam jānodrošina pakalpojumu sniegšana igauņu valodā vismaz B2 līmenī.",
                "CV forma: Visu komandas locekļu CV obligāti jāiesniedz uz RHAD Pielikuma 1.1 veidlapas igauņu valodā.",
                "Komandas nemainīgums: Komandai jābūt nokomplektētai vismaz uz 12 secīgiem mēnešiem. Komandas locekļu maiņa pieļaujama tikai ar pasūtītāja iepriekšēju rakstisku piekrišanu, paziņojot vismaz 1 mēnesi iepriekš, un jaunajam speciālistam jābūt ar vismaz līdzvērtīgu kvalifikāciju.",
                "Papildu speciālisti: Ja pretendents iesniedz vairāk personu, arī papildu personām jāatbilst prasībām."
            ]
        },
        {
            "id": "lisa1-cv-form",
            "title_lv": "8. Pielikums 1.1 – Komandas locekļa CV veidne",
            "title_ee": "RHAD LISA 1 LISA 1.1. CV VORM",
            "cv_intro_lv": "Veidne, kurā obligāti jāiesniedz visu komandas locekļu dzīvesgājumi igauņu valodā:",
            "cv_sections": [
                {
                    "sec_title": "1. Pamatinformācija par personu",
                    "fields": [
                        {"label_lv": "Lomas nosaukums (Rolli nimetus)", "desc": "IT projektu vadītājs / Front-end / Full-stack / Analītiķis / UX/UI / Testētājs"},
                        {"label_lv": "Vārds un uzvārds (Ees- ja perekonnanimi)", "desc": "Speciālista pilns vārds"}
                    ]
                },
                {
                    "sec_title": "2. Valodu prasmes (Keeleoskus)",
                    "fields": [
                        {"label_lv": "Valoda (Keele nimetus)", "desc": "Igauņu valoda (Eesti keel)"},
                        {"label_lv": "Runāšanas prasme (Kõneoskus)", "desc": "Līmenis atbilstoši CEFR (B2, C1, C2 vai dzimtā)"},
                        {"label_lv": "Rakstīšanas prasme (Kirjaoskus)", "desc": "Līmenis atbilstoši CEFR (B2, C1, C2 vai dzimtā)"}
                    ]
                },
                {
                    "sec_title": "3. Darba pieredze (Töökogemus - ja rollil nõutud)",
                    "fields": [
                        {"label_lv": "Darba devējs (Tööandja)", "desc": "Uzņēmuma nosaukums"},
                        {"label_lv": "Periods (Töötamise periood)", "desc": "Formāts: mm.gggg - mm.gggg"},
                        {"label_lv": "Amats un pienākumi (Ametinimetus ja ülesanded)", "desc": "Īss galveno pienākumu apraksts"}
                    ]
                },
                {
                    "sec_title": "4. Dalība programmatūras izstrādes projektos (Osalemine tarkvaraarenduse projektides)",
                    "fields": [
                        {"label_lv": "Projekta nosaukums un iepirkuma Nr. (Projekti nimetus ja riigihanke number)", "desc": "Projekta vai iepirkuma identifikators"},
                        {"label_lv": "Pretendenta loma projektā (Pakkuja roll projektis)", "desc": "Piem., vadošais izstrādātājs, front-end izstrādātājs utt."},
                        {"label_lv": "Projekta un veikto darbu apraksts (Projekti ja tööde kirjeldus)", "desc": "Detalizēts apraksts par izstrādāto risinājumu"},
                        {"label_lv": "Izmantotās tehnoloģijas (Kasutatud tehnoloogiad)", "desc": "Piem., React, Next.js, TypeScript, Tailwind, Docker, PostgreSQL utt."},
                        {"label_lv": "Nostrādātais darba apjoms (Töömaht viimase 36 kuu jooksul)", "desc": "Nostrādātās darba stundas pēdējo 36 mēnešu laikā"},
                        {"label_lv": "Pasūtītāja kontaktpersona atsauksmēm (Hankija kontaktisik)", "desc": "Vārds, uzvārds, tālrunis, e-pasts datu pārbaudei"}
                    ]
                }
            ]
        }
    ]
}

import { Service, ServiceCategory, DirectusPage } from './types';

export const SEED_CATEGORIES: ServiceCategory[] = [
  {
    id: 'cat-1',
    name: 'Innoveeri ja kaitse äri',
    slug: 'innoveeri-ja-kaitse-ari',
    description: 'Toetused, laenud ja nõustamisteenused ettevõtete innovatsioonivõimekuse, digitaliseerimise ja konkurentsivõime tõstmiseks.',
    iconName: 'Sparkles',
  },
  {
    id: 'cat-2',
    name: 'Alusta ja kasvata ettevõtet',
    slug: 'alusta-ja-kasvata',
    description: 'Starditoetused, arenguprogrammid ja finantseerimislahendused uutele ning kasvufaasis olevatele ettevõtetele.',
    iconName: 'TrendingUp',
  },
  {
    id: 'cat-3',
    name: 'Ekspordi ja laiene välisturgudele',
    slug: 'ekspordi-ja-laiene',
    description: 'Välismesside toetused, sihtturu seminarid ja kontaktkohtumised eksportivatele ettevõtetele.',
    iconName: 'Globe',
  },
  {
    id: 'cat-4',
    name: 'Rohepööre ja energiatõhusus',
    slug: 'rohepoore',
    description: 'Ressursitõhususe toetused ja roheauditi läbiviimise võimalused kestliku tootmise saavutamiseks.',
    iconName: 'Leaf',
  }
];

export const SEED_SERVICES: Service[] = [
  {
    id: 'srv-1',
    title: 'Digitaliseerimise teekaardi arendustegevuste toetus',
    slug: 'digitaliseerimise-teekaardi-arendustegevused-toetus',
    categorySlug: 'innoveeri-ja-kaitse-ari',
    categoryName: 'Innoveeri ja kaitse äri',
    summary: 'Toetus tootmis- ja teenindusettevõtetele protsesside automatiseerimiseks, tarkvara juurutamiseks ja tarneahela digitaliseerimiseks.',
    targetAudience: ['Tootmisettevõte', 'Teenindusettevõte', 'VKU', 'Suurettevõte'],
    serviceType: 'grant',
    maxAmount: '300 000 €',
    intensityPercent: 'Kuni 50%',
    status: 'open',
    deadline: 'Avatud kuni eelarve ammendumiseni',
    description: 'Toetuse eesmärk on toetada Eesti ettevõtjate digitaliseerimist ja automatiseerimist, tõstes seeläbi ettevõtete lisandväärtust ja konkurentsivõimet. Toetust saab kasutada teekaardis kaardistatud kitsaskohtade lahendamiseks, uute digilahenduste arendamiseks või äriprotsesside ümberkorraldamiseks.',
    eligibilityCriteria: [
      'Ettevõte on registreeritud Eestis ja tegutsenud vähemalt 2 majandusaastat;',
      'Ettevõtte viimase kahe majandusaasta keskmine müügitulu on vähemalt 200 000 eurot;',
      'Ettevõttel on koostatud ja EISi poolt heaks kiidetud digitaliseerimise teekaart;',
      'Ettevõttel puuduvad maksuvõlad või need on ajatatud;',
      'Ettevõte vastab riigiabi reeglitele ja vähese tähtsusega abi (VTA) piirmääradele.'
    ],
    processSteps: [
      {
        step: 1,
        title: 'Teekaardi koostamine või esitamine',
        description: 'Koosta ettevõtte digitaliseerimise teekaart koos atesteeritud eksperdiga või esita varasem kehtiv teekaart.'
      },
      {
        step: 2,
        title: 'Taotluse esitamine e-toetuste keskkonnas',
        description: 'Täida taotlusvorm, lisa projekti eelarve, tegevuskava ja teekaart riigi e-toetuste keskkonnas.'
      },
      {
        step: 3,
        title: 'Ekspertiis ja otsus',
        description: 'EIS hindab taotluse vastavust ja sisulist mõju kuni 30 tööpäeva jooksul.'
      },
      {
        step: 4,
        title: 'Projekti elluviimine ja väljamaksed',
        description: 'Tee arendustööd, esita vahearuanded ning kuludokumendid toetuse väljamaksmiseks.'
      }
    ],
    ctaUrl: 'https://etoetus.struktuurifondid.ee',
    ctaText: 'Esita taotlus e-toetustes',
    seoTitle: 'Digitaliseerimise teekaardi toetus | EIS',
    seoDescription: 'Toetus tootmis- ja teenindusettevõtete digitaliseerimiseks ja automatiseerimiseks kuni 300 000 eurot.'
  },
  {
    id: 'srv-2',
    title: 'Ettevõtluslaenu käendus',
    slug: 'laenukaendus-2',
    categorySlug: 'innoveeri-ja-kaitse-ari',
    categoryName: 'Innoveeri ja kaitse äri',
    summary: 'Käendus aitab ettevõttel saada pangalaenu või liisingut juhul, kui napib tagatisi või tegutsemisajalugu on lühike.',
    targetAudience: ['Alustav ettevõte', 'VKU', 'Eksportija', 'Tootja'],
    serviceType: 'loan_guarantee',
    maxAmount: 'Kuni 5 000 000 €',
    intensityPercent: 'Kuni 80% laenusummast',
    status: 'open',
    deadline: 'Pidev taotlemine läbi pankade',
    description: 'EIS laenukäendus maandab panga riske ja võimaldab ettevõtjatel investeerida arengusse, masinatesse ja seadmetesse ning rahastada käibevahendeid ka siis, kui ettevõtte enda tagatised ei ole panga nõuete täitmiseks piisavad.',
    eligibilityCriteria: [
      'Ettevõte on registreeritud Eesti äriregistris ja omab elujõulist äriplaani;',
      'Laenu taotletakse investeeringuteks (nt seadmed, kinnisvara) või käibekapitali finantseerimiseks;',
      'Finantsprognoosid näitavad ettevõtte võimekust laenu tagasi maksta;',
      'Puuduvad kontrollimata maksehäired ja omakapital vastab äriseadustiku nõuetele.'
    ],
    processSteps: [
      {
        step: 1,
        title: 'Pöördu oma kodupanka',
        description: 'Esita laenutaotlus pangale. Kui pank nõuab lisatagatist, teeb pank ise taotluse EISile käenduse saamiseks.'
      },
      {
        step: 2,
        title: 'Panga ja EISi koostöö',
        description: 'Ettevõtja ei pea eraldi EISi poole pöörduma – pank saadab projekti andmed EISile analüüsiks.'
      },
      {
        step: 3,
        title: 'Käenduslepingu sõlmimine',
        description: 'EISi positiivse otsuse järel sõlmivad pank ja EIS käenduslepingu ning laen väljastatakse ettevõttele.'
      }
    ],
    partnerBanks: ['Swedbank', 'SEB', 'Luminor', 'LHV', 'Coop Pank', 'Bigbank'],
    ctaUrl: 'https://eis.ee/kontaktid/',
    ctaText: 'Pöördu oma panka või konsulteeri',
    seoTitle: 'Ettevõtluslaenu käendus kuni 80% | EIS',
    seoDescription: 'EIS laenukäendus aitab ettevõtetel kaasata pangalaenu kuni 5 miljoni euro ulatuses.'
  },
  {
    id: 'srv-3',
    title: 'Tark tellija programm',
    slug: 'tark-tellija',
    categorySlug: 'innoveeri-ja-kaitse-ari',
    categoryName: 'Innoveeri ja kaitse äri',
    summary: 'Mentorlus ja praktiline koolitusprogramm ettevõtete juhtidele IT- ja arendusprojektide professionaalseks tellimiseks.',
    targetAudience: ['Ettevõtte juht', 'Tootejuht', 'Arendusjuht', 'VKU'],
    serviceType: 'advisory',
    maxAmount: 'Tasuta / Osalustasuta',
    intensityPercent: '100% subsideeritud',
    status: 'open',
    deadline: 'Järgmine grupp alustab: Detsember 2026',
    description: 'Programm "Tark tellija" annab mitte-tehnoloogiliste ettevõtete juhtidele oskused, kuidas defineerida tarkvaraarenduse lähteülesannet, valida sobivat arenduspartnerit, juhtida agiilseid projekte ja vältida eelarve ülekulu.',
    eligibilityCriteria: [
      'Ettevõte plaanib järgmise 12 kuu jooksul tellida IT-arendust mahus vähemalt 20 000 eurot;',
      'Programmis osaleb ettevõtte otsustaja (juhatuse liige või võtmeisik);',
      'Ettevõte on valmis osalema 4-päevasel intensiivkursusel ja individuaalsetes mentorsessioonides.'
    ],
    processSteps: [
      {
        step: 1,
        title: 'Kandideerimine programmi',
        description: 'Täida lühike ankeet oma ettevõtte arendusvajaduste ja eesmärkide kohta.'
      },
      {
        step: 2,
        title: 'Eelintervjuu ja grupi valik',
        description: 'EIS ekspert viib läbi 20-minutilise vestluse ootuste kaardistamiseks.'
      },
      {
        step: 3,
        title: 'Praktiline õppeprogramm',
        description: '4 interaktiivset moodulit ja 1-on-1 mentorlus oma arenduse lähteülesande koostamiseks.'
      }
    ],
    ctaUrl: 'https://eis.ee/sundmused/tark-tellija-registreerimine',
    ctaText: 'Registreeru programmi',
    seoTitle: 'Tark tellija koolitusprogramm | EIS',
    seoDescription: 'Õpi professionaalselt tellima tarkvaraarendust ja vältima IT-projektide riske.'
  }
];

export const SEED_HOMEPAGE: DirectusPage = {
  id: 'page-home',
  slug: '',
  title: 'Ettevõtluse ja Innovatsiooni Sihtasutus',
  seoTitle: 'EIS - Ettevõtluse ja Innovatsiooni Sihtasutus | Avalikud teenused',
  seoDescription: 'EIS toetab Eesti ettevõtete arengut, innovatsiooni, eksporti ja digitaliseerimist.',
  blocks: [
    {
      id: 'blk-hero',
      type: 'hero',
      title: 'Aitame Sinu ettevõttel kasvada ja uueneda',
      subtitle: 'Toetused, käendused, mentorlus ja sihtturu ekspertiis ühest kohast.',
      data: {}
    },
    {
      id: 'blk-categories',
      type: 'categories_grid',
      title: 'Vali oma ettevõtte eesmärk',
      subtitle: 'Leia sobivad teenused vastavalt oma äri arenguetapile',
      data: { categories: SEED_CATEGORIES }
    },
    {
      id: 'blk-services',
      type: 'services_grid',
      title: 'Populaarsemad toetused ja teenused',
      subtitle: 'Hetkel avatud ja enim taotletud EISi võimalused',
      data: { services: SEED_SERVICES }
    }
  ]
};

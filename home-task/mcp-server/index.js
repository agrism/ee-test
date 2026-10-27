const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3001;

// MCP Tool Manifest
const MCP_TOOLS = [
  {
    name: 'find_eis_services',
    description: 'Otsib ja soovitab EIS toetusmeetmeid vastavalt ettevõtte profiilile, märksõnadele ja vajadustele.',
    parameters: {
      type: 'object',
      properties: {
        query: { type: 'string', description: 'Ettevõtte vabas vormis vajadus' },
        company_type: { type: 'string', description: 'Tootmisettevõte / Teenindus / VKU' }
      },
      required: ['query']
    }
  },
  {
    name: 'get_service_criteria',
    description: 'Annab konkreetse meetme tingimused ja toetuse piirmäärad.',
    parameters: {
      type: 'object',
      properties: {
        slug: { type: 'string', description: 'Meetme URL slug' }
      },
      required: ['slug']
    }
  }
];

// Health check endpoint
app.get('/healthz', (req, res) => {
  res.json({ status: 'ok', mcp: 'active' });
});

// List MCP tools
app.get('/api/mcp/tools', (req, res) => {
  res.json({ tools: MCP_TOOLS });
});

// Execute find_services tool
app.post('/api/mcp/tool/find_services', (req, res) => {
  const { query } = req.body || {};
  const q = (query || '').toLowerCase();

  let matched = [];
  let explanation = '';

  if (q.includes('digi') || q.includes('tarkvara') || q.includes('tootmis') || q.includes('automat')) {
    matched.push({
      id: 'srv-1',
      title: 'Digitaliseerimise teekaardi arendustegevuste toetus',
      slug: 'digitaliseerimise-teekaardi-arendustegevused-toetus',
      categorySlug: 'innoveeri-ja-kaitse-ari',
      maxAmount: '300 000 €',
      intensityPercent: 'Kuni 50%'
    });
    explanation = 'MCP Mudeli analüüs: Tuvastatud tegevused seonduvad digitaliseerimise ja protsesside automatiseerimisega. Sobivaim meede on Digitaliseerimise teekaardi arendustoetus.';
  } else if (q.includes('laen') || q.includes('käendus') || q.includes('pank') || q.includes('tagatis')) {
    matched.push({
      id: 'srv-2',
      title: 'Ettevõtluslaenu käendus',
      slug: 'laenukaendus-2',
      categorySlug: 'innoveeri-ja-kaitse-ari',
      maxAmount: 'Kuni 5 000 000 €',
      intensityPercent: 'Kuni 80%'
    });
    explanation = 'MCP Mudeli analüüs: Ettevõte vajab laenuriskide maandamist ja riiklikku garantiid. Sobiv meede on EIS ettevõtluslaenu käendus.';
  } else if (q.includes('koolitus') || q.includes('tellija') || q.includes('it')) {
    matched.push({
      id: 'srv-3',
      title: 'Tark tellija programm',
      slug: 'tark-tellija',
      categorySlug: 'innoveeri-ja-kaitse-ari',
      maxAmount: 'Tasuta / Subsideeritud',
      intensityPercent: '100%'
    });
    explanation = 'MCP Mudeli analüüs: Enne suuremahulise tarkvara tellimist soovitab mudel läbida programmi "Tark tellija", et vältida eelarve ülekulu.';
  } else {
    matched.push({
      id: 'srv-1',
      title: 'Digitaliseerimise teekaardi arendustegevuste toetus',
      slug: 'digitaliseerimise-teekaardi-arendustegevused-toetus',
      maxAmount: '300 000 €'
    });
    matched.push({
      id: 'srv-2',
      title: 'Ettevõtluslaenu käendus',
      slug: 'laenukaendus-2',
      maxAmount: '5 000 000 €'
    });
    explanation = `MCP Tööriist leidis üldised aktiivsed meetmed päringule "${query}".`;
  }

  res.json({
    tool: 'find_eis_services',
    query,
    matchedServices: matched,
    explanation
  });
});

// Execute get_service_criteria tool
app.post('/api/mcp/tool/get_service_criteria', (req, res) => {
  const { slug } = req.body || {};
  const criteriaMap = {
    'digitaliseerimise-teekaardi-arendustegevused-toetus': {
      title: 'Digitaliseerimise teekaardi arendustegevuste toetus',
      targetAudience: 'Töötleva tööstuse ja mäetööstuse ning teenindussektori VKU-d ja suurettevõtted',
      maxGrant: '300 000 €',
      ownContribution: 'Vähemalt 50%',
      eligibleCosts: ['Tarkvara litsentsid ja arendus', 'Robotite ja seadmete sidustamine', 'Pilvetehnoloogiad', 'Töötajate digikoolitused']
    },
    'laenukaendus-2': {
      title: 'Ettevõtluslaenu käendus',
      targetAudience: 'Eestis registreeritud jätkusuutlikud ettevõtted',
      maxGuarantee: 'Kuni 5 000 000 € (kuni 80% laenusummast)',
      partnerBanks: ['Swedbank', 'SEB', 'Luminor', 'LHV', 'Coop Pank']
    },
    'tark-tellija': {
      title: 'Tark tellija programm',
      targetAudience: 'Ettevõtted, kes plaanivad suuremahulisi IT/tarkvara hankeid',
      cost: 'Tasuta / Riigi toetatud',
      format: 'Praktilised töötoad ja mentorlus'
    }
  };

  const details = criteriaMap[slug] || { error: 'Meedet ei leitud', slug };
  res.json({
    tool: 'get_service_criteria',
    slug,
    criteria: details
  });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`EIS MCP Server running on port ${PORT}`);
});

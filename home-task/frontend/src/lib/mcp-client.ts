import { Service, McpToolResponse } from './types';
import { getServices } from './directus';

const MCP_SERVER_URL = process.env.NEXT_PUBLIC_MCP_SERVER_URL || 'http://localhost:3001';

export async function queryMcpAssistant(userQuery: string): Promise<McpToolResponse> {
  const normalized = userQuery.toLowerCase();
  const allServices = await getServices();

  // Try querying MCP server if running
  try {
    const res = await fetch(`${MCP_SERVER_URL}/api/mcp/tool/find_services`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: userQuery }),
      cache: 'no-store'
    });
    if (res.ok) {
      const data = await res.json();
      return data;
    }
  } catch (err) {
    // If standalone MCP container is booting or in dev, run local MCP tool logic
  }

  // Local MCP tool matching implementation:
  let matched: Service[] = [];
  let explanation = '';

  if (normalized.includes('digi') || normalized.includes('tarkvara') || normalized.includes('it') || normalized.includes('tootmis')) {
    matched = allServices.filter(s => s.slug === 'digitaliseerimise-teekaardi-arendustegevused-toetus');
    explanation = 'Tuvastatud märksõnad: digitaliseerimine, IT, tarkvara. Soovitatud meede toetab tootmis- ja teenindusprotsesside automatiseerimist kuni 300 000 euroga.';
  } else if (normalized.includes('laen') || normalized.includes('raha') || normalized.includes('käendus') || normalized.includes('tagatis') || normalized.includes('pank')) {
    matched = allServices.filter(s => s.slug === 'laenukaendus-2');
    explanation = 'Tuvastatud märksõnad: laen, finantseerimine, tagatised. EIS laenukäendus võimaldab pangast laenu saada kuni 80% ulatuses riigi käendusega.';
  } else if (normalized.includes('koolitus') || normalized.includes('tellij') || normalized.includes('mentor') || normalized.includes('õpi')) {
    matched = allServices.filter(s => s.slug === 'tark-tellija');
    explanation = 'Tuvastatud märksõnad: teadmised, arenduse juhtimine. Programm "Tark tellija" aitab juhtidel vältida IT-projektide ebaõnnestumist.';
  } else {
    matched = allServices.slice(0, 2);
    explanation = `Vastavalt päringule "${userQuery}" soovitab EIS MCP mudel tutvuda järgmiste aktiivsete toetusmeetmetega:`;
  }

  return {
    tool: 'find_eis_services',
    query: userQuery,
    matchedServices: matched,
    explanation
  };
}

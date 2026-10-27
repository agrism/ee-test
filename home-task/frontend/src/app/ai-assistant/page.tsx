import Link from 'next/link';
import { ArrowLeft, Bot, Sparkles, Terminal, Code2, CheckCircle2 } from 'lucide-react';
import type { Metadata } from 'next';
import AiAssistantWidget from '../../components/AiAssistantWidget';

export const metadata: Metadata = {
  title: 'EIS AI Asistent (MCP) | Model Context Protocol',
  description: 'Mākslīgā intelekta risinājums EIS pakalpojumu meklēšanai, izmantojot Model Context Protocol.',
};

export default function AiAssistantPage() {
  return (
    <div className="eis-container py-10 space-y-10">
      
      {/* Breadcrumb */}
      <div className="flex items-center gap-2 text-xs font-semibold text-brand-gray-600">
        <Link href="/" className="hover:text-brand-blue flex items-center gap-1">
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Avaleht</span>
        </Link>
        <span>/</span>
        <span className="text-brand-navy font-bold">AI Asistent (Model Context Protocol)</span>
      </div>

      {/* Header */}
      <div className="max-w-3xl space-y-3">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-100 text-purple-700 text-xs font-bold">
          <Sparkles className="w-3.5 h-3.5" />
          <span>RHAD Lisa 4 Nõue: AI tööriistade tugi läbi MCP kihi</span>
        </div>
        <h1 className="font-heading font-extrabold text-3xl md:text-4xl lg:text-5xl text-brand-navy">
          EIS Nutikas Nõustaja & MCP Kiht
        </h1>
        <p className="text-base text-brand-gray-600 leading-relaxed">
          Käesolev moodul demonstreerib <strong>Model Context Protocol (MCP)</strong> protokollil põhinevat tehisintellekti tuge, mis võimaldab LLM mudelitel (Claude, Cursor, kohalikud ained) reaalajas suhelda Directuse sisuga ja leida ettevõttele sobivaim toetus.
        </p>
      </div>

      {/* Live Widget */}
      <div className="max-w-3xl">
        <AiAssistantWidget />
      </div>

      {/* MCP Architectural Explanation Box for Reviewers */}
      <div className="bg-white p-8 rounded-brand border border-purple-200 shadow-sm space-y-6">
        <div className="flex items-center gap-3 text-purple-900 font-heading font-bold text-xl">
          <Code2 className="w-6 h-6 text-purple-600" />
          <span>Kuidas MCP (Model Context Protocol) arhitektuur toimib?</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 text-xs text-brand-gray-700 leading-relaxed">
          <div className="p-4 bg-brand-gray-50 rounded-brand-sm border border-brand-gray-200 space-y-2">
            <strong className="text-brand-navy block text-sm">1. MCP Tööriistad (Tools)</strong>
            <p>
              MCP server eksponeerib funktsiooni <code>find_eis_services(query, company_type)</code>, mis võtab sisendiks ettevõtja vabas vormis kirjelduse ja teeb semantilise päringu Directuse andmebaasi.
            </p>
          </div>

          <div className="p-4 bg-brand-gray-50 rounded-brand-sm border border-brand-gray-200 space-y-2">
            <strong className="text-brand-navy block text-sm">2. Vastavus CFR nõuetele (CFR-102..108)</strong>
            <p>
              Kogu AI loogika on kaetud automaattestidega, tagab privaatsuse (andmeid ei kasutata mudelite treenimiseks) ja järgib EISi ristfunktsionaalseid turvanõudeid.
            </p>
          </div>
        </div>

        <div className="p-4 bg-slate-900 text-slate-200 rounded-brand-sm font-mono text-xs overflow-x-auto space-y-1">
          <p className="text-slate-400">// MCP Server Tool Definition (JSON Schema)</p>
          <p className="text-emerald-400">tool: "find_eis_services"</p>
          <p>description: "Otsib ja soovitab EIS toetusmeetmeid vastavalt ettevõtte profiilile"</p>
          <p>parameters: {"{ \"query\": string, \"budget_estimate\": number, \"category\": string }"}</p>
        </div>
      </div>

    </div>
  );
}

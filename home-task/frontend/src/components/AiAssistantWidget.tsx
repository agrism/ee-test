'use client';

import { useState } from 'react';
import { Bot, Send, Sparkles, ArrowRight, CheckCircle2 } from 'lucide-react';
import Link from 'next/link';
import { queryMcpAssistant } from '../lib/mcp-client';
import { McpToolResponse } from '../lib/types';

export default function AiAssistantWidget() {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<McpToolResponse | null>(null);

  const sampleQueries = [
    'Soovin automatiseerida ja digitaliseerida tootmist',
    'Vajan pangalaenu saamiseks riiklikku käendust',
    'Kuidas vältida IT-arenduse tellimisel vigade tegemist?'
  ];

  const handleAsk = async (userText: string) => {
    if (!userText.trim()) return;
    setLoading(true);
    setQuery(userText);
    try {
      const resp = await queryMcpAssistant(userText);
      setResult(resp);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-brand border-2 border-brand-lightBlue p-7 shadow-sm">
      <div className="flex items-center gap-3 mb-3">
        <div className="w-10 h-10 rounded-full bg-brand-lightBlue flex items-center justify-center text-brand-blue">
          <Bot className="w-5 h-5" />
        </div>
        <div>
          <h3 className="font-heading font-bold text-lg text-brand-navy flex items-center gap-2">
            <span>EIS Viedais Asistent</span>
            <span className="badge-tag bg-purple-100 text-purple-700 text-[10px]">MCP PROTOKOLS</span>
          </h3>
          <p className="text-xs text-brand-gray-600">
            Mākslīgā intelekta serviss, kas analizē Jūsu vajadzību un piemeklē atbilstošās EIS programmas.
          </p>
        </div>
      </div>

      {/* Input area */}
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleAsk(query);
        }}
        className="relative mb-4"
      >
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Kirjelda oma ettevõtte vajadust (nt. plaanime osta uue tarkvara)..."
          className="w-full pl-4 pr-24 py-3 rounded-brand-sm border border-brand-gray-300 text-sm focus:border-brand-blue focus:ring-1 focus:ring-brand-blue outline-none"
        />
        <button
          type="submit"
          disabled={loading || !query.trim()}
          className="absolute right-1.5 top-1.5 bottom-1.5 px-4 bg-brand-blue text-white rounded-brand-sm text-xs font-bold hover:bg-brand-darkBlue transition-colors flex items-center gap-1.5 disabled:opacity-50"
        >
          {loading ? (
            <span className="animate-spin text-sm">⏳</span>
          ) : (
            <>
              <span>Leia meede</span>
              <Send className="w-3.5 h-3.5" />
            </>
          )}
        </button>
      </form>

      {/* Quick Prompts */}
      <div className="flex flex-wrap items-center gap-2 text-xs text-brand-gray-600 mb-6">
        <span className="text-[11px] font-semibold text-brand-gray-400">Näidisküsimused:</span>
        {sampleQueries.map((q, idx) => (
          <button
            key={idx}
            type="button"
            onClick={() => handleAsk(q)}
            className="px-2.5 py-1 bg-brand-gray-100 hover:bg-brand-lightBlue hover:text-brand-blue rounded-full text-brand-gray-700 transition-colors"
          >
            {q}
          </button>
        ))}
      </div>

      {/* Results Box */}
      {result && (
        <div className="p-5 bg-brand-gray-50 rounded-brand-sm border border-brand-gray-200 animate-fadeIn space-y-4">
          <div className="flex items-center justify-between text-xs border-b border-brand-gray-200 pb-2">
            <span className="font-mono text-purple-700 font-semibold">
              🛠️ Rīks: {result.tool}()
            </span>
            <span className="text-emerald-600 font-semibold flex items-center gap-1">
              <CheckCircle2 className="w-3.5 h-3.5" />
              Tuvastatud {result.matchedServices.length} meede(t)
            </span>
          </div>

          <p className="text-xs text-brand-gray-800 leading-relaxed font-medium">
            {result.explanation}
          </p>

          <div className="space-y-2">
            {result.matchedServices.map((srv) => (
              <div
                key={srv.id}
                className="flex items-center justify-between p-3 bg-white rounded-brand-sm border border-brand-gray-200 hover:border-brand-blue transition-colors text-xs"
              >
                <div>
                  <strong className="text-brand-navy block text-sm">{srv.title}</strong>
                  <span className="text-brand-gray-600">
                    {srv.maxAmount ? `Maksimum: ${srv.maxAmount}` : srv.categoryName}
                  </span>
                </div>
                <Link
                  href={`/teenused/${srv.slug}`}
                  className="inline-flex items-center gap-1 font-bold text-brand-blue hover:underline"
                >
                  <span>Ava teenus</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </Link>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

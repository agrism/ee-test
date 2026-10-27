'use client';

import { useState } from 'react';
import { Coins, CheckCircle } from 'lucide-react';

export default function GrantCalculator() {
  const [projectBudget, setProjectBudget] = useState<number>(150000);
  const [grantRate, setGrantRate] = useState<number>(50);

  // Maximum grant is 300,000 €
  const calculatedGrant = Math.min(300000, (projectBudget * grantRate) / 100);
  const selfContribution = projectBudget - calculatedGrant;

  return (
    <div className="bg-gradient-to-br from-emerald-50/60 to-teal-50/30 p-7 rounded-brand border border-emerald-200 shadow-sm">
      <div className="flex items-center gap-2.5 text-emerald-800 font-heading font-bold text-lg mb-2">
        <Coins className="w-5 h-5 text-emerald-600" />
        <span>Digitaliseerimise toetussumma kalkulaator</span>
      </div>
      <p className="text-xs text-brand-gray-600 mb-6">
        Arvuta prognoositav toetuse suurus vastavalt oma digitaliseerimise projekti eelarvele.
      </p>

      <div className="space-y-6">
        {/* Project Budget Slider */}
        <div>
          <div className="flex justify-between items-center mb-2">
            <label className="text-xs font-bold text-brand-gray-800 uppercase tracking-wide">
              Projekti kogumaksumus (ilma km-ta):
            </label>
            <span className="font-heading font-bold text-lg text-emerald-700">
              {projectBudget.toLocaleString('et-EE')} €
            </span>
          </div>
          <input
            type="range"
            min="20000"
            max="700000"
            step="10000"
            value={projectBudget}
            onChange={(e) => setProjectBudget(Number(e.target.value))}
            className="w-full h-2 bg-emerald-200 rounded-lg appearance-none cursor-pointer accent-emerald-600"
          />
          <div className="flex justify-between text-[11px] text-brand-gray-400 mt-1">
            <span>20 000 €</span>
            <span>350 000 €</span>
            <span>700 000 €</span>
          </div>
        </div>

        {/* Grant Rate Selection */}
        <div>
          <div className="flex justify-between items-center mb-2">
            <label className="text-xs font-bold text-brand-gray-800 uppercase tracking-wide">
              Toetusmäär (ettevõtte suurusest sõltuvalt):
            </label>
            <span className="font-heading font-bold text-base text-emerald-700">
              {grantRate} %
            </span>
          </div>
          <div className="grid grid-cols-2 gap-2">
            <button
              type="button"
              onClick={() => setGrantRate(50)}
              className={`py-2 px-3 text-xs font-bold rounded-brand-sm border transition-all ${
                grantRate === 50 
                  ? 'bg-emerald-600 text-white border-emerald-600 shadow-xs' 
                  : 'bg-white text-brand-gray-700 border-emerald-200 hover:bg-emerald-50'
              }`}
            >
              50% (Väike- ja keskmine ettevõte)
            </button>
            <button
              type="button"
              onClick={() => setGrantRate(35)}
              className={`py-2 px-3 text-xs font-bold rounded-brand-sm border transition-all ${
                grantRate === 35 
                  ? 'bg-emerald-600 text-white border-emerald-600 shadow-xs' 
                  : 'bg-white text-brand-gray-700 border-emerald-200 hover:bg-emerald-50'
              }`}
            >
              35% (Suurettevõte)
            </button>
          </div>
        </div>

        {/* Calculation Summary */}
        <div className="grid grid-cols-2 gap-4 p-4 bg-white rounded-brand-sm border border-emerald-200 text-center">
          <div>
            <span className="text-[11px] text-brand-gray-600 uppercase font-semibold block mb-0.5">
              EIS toetus (mitte-tagastatav)
            </span>
            <span className="font-heading font-extrabold text-xl text-emerald-600">
              {calculatedGrant.toLocaleString('et-EE')} €
            </span>
            {calculatedGrant === 300000 && (
              <span className="text-[10px] text-amber-600 font-bold block mt-0.5">
                (Saavutatud meetme limiit 300 000 €)
              </span>
            )}
          </div>
          <div>
            <span className="text-[11px] text-brand-gray-600 uppercase font-semibold block mb-0.5">
              Ettevõtte omafinantseering
            </span>
            <span className="font-heading font-extrabold text-xl text-brand-navy">
              {selfContribution.toLocaleString('et-EE')} €
            </span>
          </div>
        </div>

        <div className="flex items-center gap-2 text-xs text-brand-gray-600 bg-white/70 p-2.5 rounded-brand-sm border border-emerald-100">
          <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0" />
          <span>Taotlemiseks on eelduseks eelnevalt koostatud digitaliseerimise teekaart.</span>
        </div>
      </div>
    </div>
  );
}

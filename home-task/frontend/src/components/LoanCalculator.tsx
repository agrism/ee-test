'use client';

import { useState } from 'react';
import { Calculator, ShieldCheck } from 'lucide-react';

export default function LoanCalculator() {
  const [loanAmount, setLoanAmount] = useState<number>(250000);
  const [guaranteeRate, setGuaranteeRate] = useState<number>(80);

  const guaranteeAmount = (loanAmount * guaranteeRate) / 100;
  const selfFinancing = loanAmount - guaranteeAmount;

  return (
    <div className="bg-gradient-to-br from-blue-50/70 to-indigo-50/40 p-7 rounded-brand border border-blue-200 shadow-sm">
      <div className="flex items-center gap-2.5 text-brand-blue font-heading font-bold text-lg mb-2">
        <Calculator className="w-5 h-5" />
        <span>Ettevõtluslaenu käenduse kalkulaator</span>
      </div>
      <p className="text-xs text-brand-gray-600 mb-6">
        Hinda, kui suures ulatuses saab EIS maandada panga riske Sinu investeeringu või käibekapitali kaasamisel.
      </p>

      <div className="space-y-6">
        {/* Loan Amount Slider */}
        <div>
          <div className="flex justify-between items-center mb-2">
            <label className="text-xs font-bold text-brand-gray-800 uppercase tracking-wide">
              Vajatav laenusumma:
            </label>
            <span className="font-heading font-bold text-lg text-brand-blue">
              {loanAmount.toLocaleString('et-EE')} €
            </span>
          </div>
          <input
            type="range"
            min="10000"
            max="2000000"
            step="10000"
            value={loanAmount}
            onChange={(e) => setLoanAmount(Number(e.target.value))}
            className="w-full h-2 bg-blue-200 rounded-lg appearance-none cursor-pointer accent-brand-blue"
          />
          <div className="flex justify-between text-[11px] text-brand-gray-400 mt-1">
            <span>10 000 €</span>
            <span>1 000 000 €</span>
            <span>2 000 000 €</span>
          </div>
        </div>

        {/* Guarantee Rate Slider */}
        <div>
          <div className="flex justify-between items-center mb-2">
            <label className="text-xs font-bold text-brand-gray-800 uppercase tracking-wide">
              EIS Käenduse määr:
            </label>
            <span className="font-heading font-bold text-base text-brand-blue">
              {guaranteeRate} %
            </span>
          </div>
          <input
            type="range"
            min="20"
            max="80"
            step="5"
            value={guaranteeRate}
            onChange={(e) => setGuaranteeRate(Number(e.target.value))}
            className="w-full h-2 bg-blue-200 rounded-lg appearance-none cursor-pointer accent-brand-blue"
          />
          <div className="flex justify-between text-[11px] text-brand-gray-400 mt-1">
            <span>Min 20%</span>
            <span>Tavaline 50%</span>
            <span>Maksimum 80%</span>
          </div>
        </div>

        {/* Calculation Result */}
        <div className="grid grid-cols-2 gap-4 p-4 bg-white rounded-brand-sm border border-blue-200 text-center">
          <div>
            <span className="text-[11px] text-brand-gray-600 uppercase font-semibold block mb-0.5">
              EISi riiklik tagatis
            </span>
            <span className="font-heading font-extrabold text-xl text-emerald-600">
              {guaranteeAmount.toLocaleString('et-EE')} €
            </span>
          </div>
          <div>
            <span className="text-[11px] text-brand-gray-600 uppercase font-semibold block mb-0.5">
              Ettevõtte omaosalus/tagatis
            </span>
            <span className="font-heading font-extrabold text-xl text-brand-navy">
              {selfFinancing.toLocaleString('et-EE')} €
            </span>
          </div>
        </div>

        <div className="flex items-center gap-2 text-xs text-brand-gray-600 bg-white/70 p-2.5 rounded-brand-sm border border-blue-100">
          <ShieldCheck className="w-4 h-4 text-emerald-600 flex-shrink-0" />
          <span>Käenduse saamiseks esita taotlus oma kodupangale (Swedbank, SEB, LHV jt).</span>
        </div>
      </div>
    </div>
  );
}

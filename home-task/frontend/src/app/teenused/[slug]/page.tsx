import { notFound } from 'next/navigation';
import Link from 'next/link';
import { ArrowLeft, CheckCircle2, Calendar, Coins, Building, ArrowUpRight, ShieldCheck, Check } from 'lucide-react';
import type { Metadata } from 'next';
import { getServiceBySlug, getServices } from '../../../lib/directus';
import LoanCalculator from '../../../components/LoanCalculator';
import GrantCalculator from '../../../components/GrantCalculator';

interface ServicePageProps {
  params: {
    slug: string;
  };
}

export async function generateMetadata({ params }: ServicePageProps): Promise<Metadata> {
  const service = await getServiceBySlug(params.slug);
  if (!service) {
    return { title: 'Teenust ei leitud | EIS' };
  }

  return {
    title: `${service.title} | EIS Teenused`,
    description: service.summary,
    openGraph: {
      title: service.seoTitle || service.title,
      description: service.seoDescription || service.summary,
    }
  };
}

export default async function ServiceDetailPage({ params }: ServicePageProps) {
  const service = await getServiceBySlug(params.slug);
  if (!service) {
    notFound();
  }

  const isDigitaliseerimine = service.slug === 'digitaliseerimise-teekaardi-arendustegevused-toetus';
  const isLaenukaendus = service.slug === 'laenukaendus-2';
  const isTarkTellija = service.slug === 'tark-tellija';

  return (
    <div className="eis-container py-10 space-y-12">
      
      {/* Breadcrumb Navigation */}
      <div className="flex flex-wrap items-center gap-2 text-xs font-semibold text-brand-gray-600">
        <Link href="/" className="hover:text-brand-blue flex items-center gap-1">
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Avaleht</span>
        </Link>
        <span>/</span>
        <Link href={`/${service.categorySlug}`} className="hover:text-brand-blue">
          {service.categoryName}
        </Link>
        <span>/</span>
        <span className="text-brand-navy font-bold truncate max-w-xs">{service.title}</span>
      </div>

      {/* Hero Header */}
      <div className="max-w-4xl space-y-4">
        <div className="flex flex-wrap items-center gap-2">
          <span className="badge-tag bg-brand-lightBlue text-brand-blue border border-blue-200">
            {service.serviceType === 'grant' ? 'Toetus' : service.serviceType === 'loan_guarantee' ? 'Laenukäendus' : 'Nõustamine'}
          </span>
          <span className="inline-flex items-center gap-1 text-xs font-semibold text-emerald-600 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
            {service.status === 'open' ? 'Avatud taotlemiseks' : 'Pidev'}
          </span>
          {service.deadline && (
            <span className="text-xs text-brand-gray-600 flex items-center gap-1">
              <Calendar className="w-3.5 h-3.5 text-brand-gray-400" />
              {service.deadline}
            </span>
          )}
        </div>

        <h1 className="font-heading font-extrabold text-3xl md:text-4xl lg:text-5xl text-brand-navy leading-tight">
          {service.title}
        </h1>

        <p className="text-lg text-brand-gray-600 leading-relaxed">
          {service.summary}
        </p>
      </div>

      {/* Main Content Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-10">
        
        {/* Left 2 Columns: Details, Process & Calculators */}
        <div className="lg:col-span-2 space-y-10">
          
          {/* Detailed Description */}
          <div className="bg-white p-7 rounded-brand border border-brand-gray-200 shadow-sm space-y-4">
            <h2 className="font-heading font-bold text-xl text-brand-navy">
              Teenuse eesmärk ja võimalused
            </h2>
            <p className="text-sm text-brand-gray-700 leading-relaxed whitespace-pre-line">
              {service.description}
            </p>
          </div>

          {/* Interactive Calculator Section */}
          {isDigitaliseerimine && (
            <div>
              <GrantCalculator />
            </div>
          )}

          {isLaenukaendus && (
            <div>
              <LoanCalculator />
            </div>
          )}

          {/* Eligibility Criteria */}
          <div className="bg-white p-7 rounded-brand border border-brand-gray-200 shadow-sm space-y-5">
            <h2 className="font-heading font-bold text-xl text-brand-navy">
              Nõuded taotlejale ja tingimused
            </h2>
            <div className="space-y-3">
              {service.eligibilityCriteria.map((criterion, idx) => (
                <div key={idx} className="flex items-start gap-3 text-sm text-brand-gray-700">
                  <div className="w-5 h-5 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <Check className="w-3.5 h-3.5" />
                  </div>
                  <span>{criterion}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Process Steps */}
          <div className="bg-white p-7 rounded-brand border border-brand-gray-200 shadow-sm space-y-6">
            <h2 className="font-heading font-bold text-xl text-brand-navy">
              Kuidas taotlemise protsess toimub?
            </h2>
            <div className="space-y-6">
              {service.processSteps.map((step) => (
                <div key={step.step} className="flex items-start gap-4 relative">
                  <div className="w-9 h-9 rounded-full bg-brand-blue text-white font-heading font-bold flex items-center justify-center flex-shrink-0 text-sm shadow-xs">
                    {step.step}
                  </div>
                  <div>
                    <h3 className="font-heading font-bold text-base text-brand-navy mb-1">
                      {step.title}
                    </h3>
                    <p className="text-sm text-brand-gray-600 leading-relaxed">
                      {step.description}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Partner Banks (For Laenukäendus) */}
          {service.partnerBanks && (
            <div className="bg-white p-7 rounded-brand border border-brand-gray-200 shadow-sm space-y-4">
              <h2 className="font-heading font-bold text-lg text-brand-navy flex items-center gap-2">
                <Building className="w-5 h-5 text-brand-blue" />
                <span>Koostööpartneritest pangad</span>
              </h2>
              <p className="text-xs text-brand-gray-600">
                Laenukäendust saab taotleda otse läbi järgmiste finantsasutuste:
              </p>
              <div className="flex flex-wrap gap-2.5">
                {service.partnerBanks.map((bank, idx) => (
                  <span key={idx} className="px-3.5 py-1.5 bg-brand-gray-100 text-brand-navy font-bold text-xs rounded-brand-sm border border-brand-gray-200">
                    {bank}
                  </span>
                ))}
              </div>
            </div>
          )}

        </div>

        {/* Right Sticky Sidebar: Call to action & Summary */}
        <div className="space-y-6">
          <div className="sticky top-28 bg-white p-6 rounded-brand border border-brand-gray-200 shadow-md space-y-6">
            
            <div className="space-y-2 border-b border-brand-gray-100 pb-5">
              <span className="text-xs font-bold uppercase tracking-wide text-brand-gray-600 block">
                Finantseerimise info
              </span>
              {service.maxAmount && (
                <div>
                  <span className="text-xs text-brand-gray-600 block">Maksimaalne summa:</span>
                  <span className="font-heading font-extrabold text-2xl text-brand-blue">{service.maxAmount}</span>
                </div>
              )}
              {service.intensityPercent && (
                <div className="pt-2">
                  <span className="text-xs text-brand-gray-600 block">Toetuse määr:</span>
                  <span className="font-heading font-bold text-lg text-emerald-600">{service.intensityPercent}</span>
                </div>
              )}
            </div>

            {/* Target Audience */}
            <div className="space-y-2 border-b border-brand-gray-100 pb-5">
              <span className="text-xs font-bold uppercase tracking-wide text-brand-gray-600 block">
                Sobib sihtrühmale
              </span>
              <div className="flex flex-wrap gap-1.5">
                {service.targetAudience.map((aud, idx) => (
                  <span key={idx} className="badge-tag bg-brand-gray-100 text-brand-gray-700 text-[11px]">
                    {aud}
                  </span>
                ))}
              </div>
            </div>

            {/* Main Action Button */}
            <div>
              <a
                href={service.ctaUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full inline-flex items-center justify-center gap-2 py-3.5 px-4 rounded-brand-sm bg-brand-blue hover:bg-brand-darkBlue text-white font-bold text-sm shadow-md transition-all text-center"
              >
                <span>{service.ctaText}</span>
                <ArrowUpRight className="w-4 h-4" />
              </a>
              <p className="text-[11px] text-center text-brand-gray-600 mt-2">
                Autentimine ID-kaardi, Mobiil-ID või Smart-ID abil.
              </p>
            </div>

            {/* Support info */}
            <div className="pt-4 border-t border-brand-gray-100 text-xs text-brand-gray-600 space-y-1">
              <p className="font-bold text-brand-navy">Vajad enne taotlemist nõustamist?</p>
              <p>Helista: +372 6279 700 või kirjuta: info@eis.ee</p>
            </div>

          </div>
        </div>

      </div>

    </div>
  );
}

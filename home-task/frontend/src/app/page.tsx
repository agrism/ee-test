import Link from 'next/link';
import { ArrowRight, Sparkles, TrendingUp, Globe, Leaf, CheckCircle2, Shield, Bot } from 'lucide-react';
import { getHomepageData, getCategories, getServices } from '../lib/directus';
import ServiceCard from '../components/ServiceCard';
import AiAssistantWidget from '../components/AiAssistantWidget';

export default async function HomePage() {
  const pageData = await getHomepageData();
  const categories = await getCategories();
  const services = await getServices();

  const iconMap: Record<string, React.ReactNode> = {
    'Sparkles': <Sparkles className="w-6 h-6 text-brand-blue" />,
    'TrendingUp': <TrendingUp className="w-6 h-6 text-emerald-600" />,
    'Globe': <Globe className="w-6 h-6 text-blue-500" />,
    'Leaf': <Leaf className="w-6 h-6 text-teal-600" />
  };

  return (
    <div className="space-y-20 pb-16">
      
      {/* HERO SECTION */}
      <section className="bg-gradient-to-b from-blue-50/80 via-white to-transparent pt-16 pb-14 border-b border-brand-gray-200">
        <div className="eis-container">
          <div className="max-w-3xl mx-auto text-center space-y-6">
            
            <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-brand-lightBlue border border-blue-200 text-brand-blue text-xs font-bold shadow-xs">
              <span className="w-2 h-2 rounded-full bg-brand-blue animate-ping"></span>
              <span>Uus Directus Headless platvorm & DDS 2.0 disain</span>
            </div>

            <h1 className="font-heading font-extrabold text-4xl md:text-5xl lg:text-6xl text-brand-navy tracking-tight leading-tight">
              Aitame Sinu ettevõttel <span className="text-brand-blue">kasvada ja uueneda</span>
            </h1>

            <p className="text-base md:text-lg text-brand-gray-600 leading-relaxed">
              Ettevõtluse ja Innovatsiooni Sihtasutus pakub toetusi, laenukäendusi ja nõustamist Eesti ettevõtete igas arenguetapis.
            </p>

            {/* Quick Actions */}
            <div className="flex flex-wrap items-center justify-center gap-4 pt-2">
              <Link
                href="/innoveeri-ja-kaitse-ari"
                className="px-6 py-3.5 bg-brand-blue hover:bg-brand-darkBlue text-white font-bold rounded-brand-sm text-sm shadow-md transition-all flex items-center gap-2"
              >
                <span>Vaata kõiki toetusi ja teenuseid</span>
                <ArrowRight className="w-4 h-4" />
              </Link>

              <Link
                href="/ai-assistant"
                className="px-6 py-3.5 bg-white hover:bg-brand-gray-50 text-brand-navy border border-brand-gray-300 font-bold rounded-brand-sm text-sm transition-all flex items-center gap-2"
              >
                <Bot className="w-4 h-4 text-purple-600" />
                <span>Leia meede AI abil (MCP)</span>
              </Link>
            </div>

          </div>
        </div>
      </section>

      {/* CATEGORIES GRID */}
      <section className="eis-container">
        <div className="text-center max-w-2xl mx-auto mb-10 space-y-2">
          <h2 className="font-heading font-bold text-2xl md:text-3xl text-brand-navy">
            Vali oma ettevõtte eesmärk
          </h2>
          <p className="text-sm text-brand-gray-600">
            Kogu info on grupeeritud vastavalt sellele, millist väljakutset Sinu ettevõte lahendab.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {categories.map((cat) => (
            <Link
              key={cat.id}
              href={`/${cat.slug}`}
              className="eis-card p-6 flex flex-col justify-between group hover:border-brand-blue transition-all"
            >
              <div>
                <div className="w-12 h-12 rounded-brand-sm bg-brand-gray-100 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                  {iconMap[cat.iconName] || <Sparkles className="w-6 h-6 text-brand-blue" />}
                </div>
                <h3 className="font-heading font-bold text-lg text-brand-navy group-hover:text-brand-blue transition-colors mb-2">
                  {cat.name}
                </h3>
                <p className="text-xs text-brand-gray-600 leading-relaxed mb-6">
                  {cat.description}
                </p>
              </div>

              <div className="flex items-center text-xs font-bold text-brand-blue group-hover:underline">
                <span>Vaata teenuseid</span>
                <ArrowRight className="w-3.5 h-3.5 ml-1 transform group-hover:translate-x-1 transition-transform" />
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* FEATURED SERVICES SECTION */}
      <section className="eis-container">
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-4">
          <div>
            <div className="text-xs font-bold uppercase tracking-wider text-brand-blue mb-1">
              Aktuaalsed võimalused
            </div>
            <h2 className="font-heading font-bold text-2xl md:text-3xl text-brand-navy">
              Populaarsemad toetused ja programmid
            </h2>
          </div>
          <Link
            href="/innoveeri-ja-kaitse-ari"
            className="text-sm font-bold text-brand-blue hover:underline flex items-center gap-1"
          >
            <span>Kõik teenused</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {services.map((service) => (
            <ServiceCard key={service.id} service={service} />
          ))}
        </div>
      </section>

      {/* AI ASSISTANT EMBEDDED WIDGET SECTION */}
      <section className="eis-container">
        <div className="max-w-3xl mx-auto">
          <AiAssistantWidget />
        </div>
      </section>

      {/* WHY CHOOSE EIS BANNER */}
      <section className="eis-container">
        <div className="bg-gradient-to-r from-brand-navy to-brand-darkBlue text-white rounded-brand-lg p-10 md:p-14 shadow-lg">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center md:text-left">
            <div>
              <div className="font-heading font-extrabold text-3xl md:text-4xl text-brand-teal mb-2">
                750 000+
              </div>
              <p className="text-sm text-brand-gray-300">
                Aastas toetatud ettevõtete ja projektide finantseerimise kogumaht.
              </p>
            </div>
            <div>
              <div className="font-heading font-extrabold text-3xl md:text-4xl text-amber-400 mb-2">
                Kuni 80%
              </div>
              <p className="text-sm text-brand-gray-300">
                Riiklik pangalaenu tagatis ja käendus riskide maandamiseks.
              </p>
            </div>
            <div>
              <div className="font-heading font-extrabold text-3xl md:text-4xl text-emerald-400 mb-2">
                100%
              </div>
              <p className="text-sm text-brand-gray-300">
                Digitaalne taotlemine ja nõustamine e-toetuste keskkonnas.
              </p>
            </div>
          </div>
        </div>
      </section>

    </div>
  );
}

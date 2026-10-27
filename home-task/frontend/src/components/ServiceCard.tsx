import Link from 'next/link';
import { ArrowRight, CheckCircle2, Coins, Calendar, Sparkles } from 'lucide-react';
import { Service } from '../lib/types';

interface ServiceCardProps {
  service: Service;
}

export default function ServiceCard({ service }: ServiceCardProps) {
  const isGrant = service.serviceType === 'grant';
  const isLoan = service.serviceType === 'loan_guarantee';

  return (
    <div className="eis-card p-6 flex flex-col justify-between h-full bg-white group">
      <div>
        {/* Top Badges */}
        <div className="flex flex-wrap items-center justify-between gap-2 mb-4">
          <span className={`badge-tag ${
            isGrant 
              ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' 
              : isLoan 
              ? 'bg-blue-50 text-blue-700 border border-blue-200' 
              : 'bg-purple-50 text-purple-700 border border-purple-200'
          }`}>
            {isGrant ? 'Toetus' : isLoan ? 'Laenukäendus' : 'Nõustamine'}
          </span>

          <span className="inline-flex items-center gap-1 text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
            {service.status === 'open' ? 'Avatud taotlemiseks' : 'Pidev'}
          </span>
        </div>

        {/* Title */}
        <h3 className="font-heading font-bold text-xl text-brand-navy group-hover:text-brand-blue transition-colors mb-3 leading-snug">
          <Link href={`/teenused/${service.slug}`} className="focus-visible:outline-none focus-visible:underline">
            {service.title}
          </Link>
        </h3>

        {/* Summary */}
        <p className="text-sm text-brand-gray-600 line-clamp-3 mb-6 leading-relaxed">
          {service.summary}
        </p>
      </div>

      <div>
        {/* Key Metrics Box */}
        {(service.maxAmount || service.intensityPercent) && (
          <div className="grid grid-cols-2 gap-3 p-3.5 bg-brand-gray-50 rounded-brand-sm border border-brand-gray-200 mb-5 text-xs">
            {service.maxAmount && (
              <div>
                <span className="text-brand-gray-600 block mb-0.5">Maksimumsumma</span>
                <span className="font-heading font-bold text-sm text-brand-navy">{service.maxAmount}</span>
              </div>
            )}
            {service.intensityPercent && (
              <div>
                <span className="text-brand-gray-600 block mb-0.5">Toetuse määr</span>
                <span className="font-heading font-bold text-sm text-brand-navy">{service.intensityPercent}</span>
              </div>
            )}
          </div>
        )}

        {/* Action Button */}
        <Link
          href={`/teenused/${service.slug}`}
          className="w-full inline-flex items-center justify-between px-4 py-2.5 rounded-brand-sm bg-brand-lightBlue text-brand-blue font-bold text-sm group-hover:bg-brand-blue group-hover:text-white transition-all"
        >
          <span>Vaata lähemalt ja taotle</span>
          <ArrowRight className="w-4 h-4 transform group-hover:translate-x-1 transition-transform" />
        </Link>
      </div>
    </div>
  );
}

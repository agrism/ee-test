import Link from 'next/link';

export default function Footer() {
  return (
    <footer className="bg-brand-navy text-white pt-16 pb-12 border-t border-brand-gray-800 mt-24">
      <div className="eis-container">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-10 pb-12 border-b border-white/10">
          
          <div className="space-y-4">
            <div className="flex items-center gap-2">
              <span className="w-8 h-8 bg-brand-blue rounded flex items-center justify-center font-heading font-extrabold text-sm">
                EIS
              </span>
              <span className="font-heading font-bold text-lg">eis.ee</span>
            </div>
            <p className="text-sm text-brand-gray-300 leading-relaxed">
              Ettevõtluse ja Innovatsiooni Sihtasutus aitab kasvatada Eesti ettevõtete konkurentsivõimet ja luua tulevikukindlat majandust.
            </p>
          </div>

          <div>
            <h4 className="font-heading font-bold text-sm tracking-wider uppercase text-brand-gray-300 mb-4">
              Peamised valdkonnad
            </h4>
            <ul className="space-y-2.5 text-sm text-brand-gray-200">
              <li>
                <Link href="/innoveeri-ja-kaitse-ari" className="hover:text-white transition-colors">
                  Innovatsioon & Teadusarendus
                </Link>
              </li>
              <li>
                <Link href="/teenused/digitaliseerimise-teekaardi-arendustegevused-toetus" className="hover:text-white transition-colors">
                  Digitaliseerimise toetus
                </Link>
              </li>
              <li>
                <Link href="/teenused/laenukaendus-2" className="hover:text-white transition-colors">
                  Ettevõtluslaenu käendus
                </Link>
              </li>
              <li>
                <Link href="/teenused/tark-tellija" className="hover:text-white transition-colors">
                  Tark tellija programm
                </Link>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="font-heading font-bold text-sm tracking-wider uppercase text-brand-gray-300 mb-4">
              Kontakt & Info
            </h4>
            <ul className="space-y-2 text-sm text-brand-gray-200">
              <li>Sepise 7, 11415 Tallinn</li>
              <li>E-post: info@eis.ee</li>
              <li>Telefon: +372 6279 700</li>
              <li>E-R 9.00 - 17.00</li>
            </ul>
          </div>

          <div>
            <h4 className="font-heading font-bold text-sm tracking-wider uppercase text-brand-gray-300 mb-4">
              Digitaalsed standardid
            </h4>
            <div className="space-y-2 text-xs text-brand-gray-300">
              <p>• Eesti Brändi DDS 2.0 disainisüsteem</p>
              <p>• WCAG 2.1 AA ligipääsetavus</p>
              <p>• Next.js App Router & Directus Headless CMS</p>
              <p>• Riigipilv Kubernetes & GitOps valmidus</p>
              <a href="/dokumentacija" className="hover:text-white underline font-medium text-blue-300 block pt-1">
                ➔ Iepirkuma dokumentācija (LV) & CFR
              </a>
            </div>
          </div>

        </div>

        <div className="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-brand-gray-300">
          <div>
            © 2026 Ettevõtluse ja Innovatsiooni Sihtasutus. Kõik õigused kaitstud.
          </div>
          <div className="flex gap-6">
            <span className="hover:text-white cursor-pointer">Privaatsuspoliitika</span>
            <span className="hover:text-white cursor-pointer">Küpsiste seaded</span>
            <span className="hover:text-white cursor-pointer">Ligipääsetavus</span>
          </div>
        </div>

      </div>
    </footer>
  );
}

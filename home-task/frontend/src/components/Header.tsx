'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Sparkles, Bot, Search } from 'lucide-react';

export default function Header() {
  const pathname = usePathname();

  return (
    <header className="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-brand-gray-200 shadow-sm">
      <div className="eis-container flex items-center justify-between h-20">
        
        {/* Brand Logo & Title */}
        <Link href="/" className="flex items-center gap-3 group focus-visible:ring-2 focus-visible:ring-brand-blue rounded-md p-1">
          <div className="w-11 h-11 bg-brand-blue text-white rounded-brand-sm flex items-center justify-center font-heading font-extrabold text-xl shadow-md group-hover:bg-brand-darkBlue transition-colors">
            EIS
          </div>
          <div>
            <div className="font-heading font-bold text-brand-navy text-lg leading-tight group-hover:text-brand-blue transition-colors">
              Ettevõtluse ja Innovatsiooni Sihtasutus
            </div>
            <div className="text-xs text-brand-gray-600 font-medium">
              Eesti ettevõtete arengupartner
            </div>
          </div>
        </Link>

        {/* Navigation Links */}
        <nav className="hidden md:flex items-center gap-7">
          <Link 
            href="/innoveeri-ja-kaitse-ari" 
            className={`text-sm font-semibold transition-colors py-2 border-b-2 ${
              pathname === '/innoveeri-ja-kaitse-ari' 
                ? 'text-brand-blue border-brand-blue' 
                : 'text-brand-gray-800 border-transparent hover:text-brand-blue'
            }`}
          >
            Teenused & Toetused
          </Link>
          
          <Link 
            href="/ai-assistant" 
            className="flex items-center gap-1.5 px-3 py-1.5 bg-brand-lightBlue text-brand-blue text-sm font-bold rounded-full hover:bg-blue-100 transition-colors"
          >
            <Bot className="w-4 h-4 text-brand-blue" />
            <span>AI Asistent (MCP)</span>
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse ml-0.5"></span>
          </Link>

          <div className="flex items-center gap-1 bg-brand-gray-100 p-1 rounded-brand-sm text-xs font-bold text-brand-gray-600">
            <span className="px-2 py-0.5 bg-white text-brand-blue rounded shadow-xs">ET</span>
            <span className="px-2 py-0.5 hover:text-brand-navy cursor-pointer">EN</span>
          </div>
        </nav>

      </div>
    </header>
  );
}

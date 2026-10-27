import type { Metadata } from 'next';
import './globals.css';
import Header from '../components/Header';
import Footer from '../components/Footer';

export const metadata: Metadata = {
  title: 'Ettevõtluse ja Innovatsiooni Sihtasutus | EIS',
  description: 'EIS toetab Eesti ettevõtete arengut, innovatsiooni, eksporti ja digitaliseerimist.',
  openGraph: {
    title: 'EIS - Ettevõtluse ja Innovatsiooni Sihtasutus',
    description: 'Avalikud toetused, laenukäendused ja nõustamisteenused ettevõtetele.',
    url: 'https://eis.ee',
    siteName: 'EIS',
    locale: 'et_EE',
    type: 'website',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="et">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="min-h-screen flex flex-col bg-brand-gray-50 text-brand-navy antialiased">
        <Header />
        <main className="flex-1">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}

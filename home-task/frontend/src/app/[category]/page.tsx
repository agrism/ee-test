import { notFound } from 'next/navigation';
import Link from 'next/link';
import { ArrowLeft, Sparkles } from 'lucide-react';
import type { Metadata } from 'next';
import { getCategoryBySlug, getServicesByCategory, getCategories } from '../../lib/directus';
import ServiceFilter from '../../components/ServiceFilter';

interface CategoryPageProps {
  params: {
    category: string;
  };
}

export async function generateMetadata({ params }: CategoryPageProps): Promise<Metadata> {
  const category = await getCategoryBySlug(params.category);
  if (!category) {
    return { title: 'Kategooriat ei leitud | EIS' };
  }

  return {
    title: `${category.name} | EIS Teenused`,
    description: category.description,
    openGraph: {
      title: `${category.name} | EIS Teenused`,
      description: category.description,
    }
  };
}

export default async function CategoryPage({ params }: CategoryPageProps) {
  const category = await getCategoryBySlug(params.category);
  if (!category) {
    notFound();
  }

  const services = await getServicesByCategory(params.category);

  return (
    <div className="eis-container py-10 space-y-10">
      
      {/* Breadcrumb & Navigation */}
      <div className="flex items-center gap-2 text-xs font-semibold text-brand-gray-600">
        <Link href="/" className="hover:text-brand-blue flex items-center gap-1">
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Avaleht</span>
        </Link>
        <span>/</span>
        <span className="text-brand-navy font-bold">{category.name}</span>
      </div>

      {/* Category Header */}
      <div className="max-w-3xl space-y-3">
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-100 text-brand-blue text-xs font-bold">
          <Sparkles className="w-3.5 h-3.5" />
          <span>EIS Valdkond</span>
        </div>
        <h1 className="font-heading font-extrabold text-3xl md:text-4xl lg:text-5xl text-brand-navy">
          {category.name}
        </h1>
        <p className="text-base text-brand-gray-600 leading-relaxed">
          {category.description}
        </p>
      </div>

      {/* Interactive Service Filter and List */}
      <ServiceFilter initialServices={services} />

    </div>
  );
}

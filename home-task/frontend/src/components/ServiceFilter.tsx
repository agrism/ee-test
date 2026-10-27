'use client';

import { useState } from 'react';
import { Search, Filter, X } from 'lucide-react';
import { Service } from '../lib/types';
import ServiceCard from './ServiceCard';

interface ServiceFilterProps {
  initialServices: Service[];
}

export default function ServiceFilter({ initialServices }: ServiceFilterProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedType, setSelectedType] = useState<string>('all');
  const [selectedAudience, setSelectedAudience] = useState<string>('all');

  const filteredServices = initialServices.filter(service => {
    // Type match
    if (selectedType !== 'all' && service.serviceType !== selectedType) {
      return false;
    }

    // Audience match
    if (selectedAudience !== 'all' && !service.targetAudience.includes(selectedAudience)) {
      return false;
    }

    // Search query match
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      const matchTitle = service.title.toLowerCase().includes(q);
      const matchSummary = service.summary.toLowerCase().includes(q);
      const matchCategory = service.categoryName.toLowerCase().includes(q);
      return matchTitle || matchSummary || matchCategory;
    }

    return true;
  });

  return (
    <div className="space-y-8">
      
      {/* Filter Toolbar */}
      <div className="bg-white p-5 rounded-brand border border-brand-gray-200 shadow-sm space-y-4">
        <div className="flex flex-col md:flex-row gap-4">
          
          {/* Search Input */}
          <div className="relative flex-1">
            <Search className="w-5 h-5 absolute left-3.5 top-1/2 -translate-y-1/2 text-brand-gray-400" />
            <input
              type="text"
              placeholder="Otsi teenust nime, märksõna või sisu järgi..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-11 pr-4 py-2.5 rounded-brand-sm border border-brand-gray-300 text-sm focus:border-brand-blue focus:ring-1 focus:ring-brand-blue outline-none"
            />
            {searchQuery && (
              <button 
                onClick={() => setSearchQuery('')}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-brand-gray-400 hover:text-brand-gray-600"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>

          {/* Type Select */}
          <div className="w-full md:w-56">
            <select
              value={selectedType}
              onChange={(e) => setSelectedType(e.target.value)}
              className="w-full px-3.5 py-2.5 rounded-brand-sm border border-brand-gray-300 text-sm font-medium text-brand-gray-800 bg-white focus:border-brand-blue focus:ring-1 focus:ring-brand-blue outline-none"
            >
              <option value="all">Kõik toetusliigid</option>
              <option value="grant">Toetused (Grandid)</option>
              <option value="loan_guarantee">Laenukäendused</option>
              <option value="advisory">Nõustamine & Koolitus</option>
            </select>
          </div>

          {/* Audience Select */}
          <div className="w-full md:w-56">
            <select
              value={selectedAudience}
              onChange={(e) => setSelectedAudience(e.target.value)}
              className="w-full px-3.5 py-2.5 rounded-brand-sm border border-brand-gray-300 text-sm font-medium text-brand-gray-800 bg-white focus:border-brand-blue focus:ring-1 focus:ring-brand-blue outline-none"
            >
              <option value="all">Kõik sihtrühmad</option>
              <option value="Tootmisettevõte">Tootmisettevõte</option>
              <option value="Teenindusettevõte">Teenindusettevõte</option>
              <option value="VKU">Väike- ja keskmine (VKU)</option>
              <option value="Alustav ettevõte">Alustav ettevõte</option>
            </select>
          </div>

        </div>

        {/* Active Filters Row */}
        <div className="flex items-center justify-between text-xs text-brand-gray-600 pt-2 border-t border-brand-gray-100">
          <span>Leitud <strong>{filteredServices.length}</strong> teenust</span>
          {(selectedType !== 'all' || selectedAudience !== 'all' || searchQuery) && (
            <button
              onClick={() => {
                setSelectedType('all');
                setSelectedAudience('all');
                setSearchQuery('');
              }}
              className="text-brand-blue hover:underline font-semibold"
            >
              Tühjenda filtrid
            </button>
          )}
        </div>
      </div>

      {/* Services Grid */}
      {filteredServices.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {filteredServices.map(service => (
            <ServiceCard key={service.id} service={service} />
          ))}
        </div>
      ) : (
        <div className="text-center py-16 bg-white rounded-brand border border-dashed border-brand-gray-300 p-8">
          <p className="text-base text-brand-gray-600 mb-2">Ühtegi teenust antud filtritega ei leitud.</p>
          <button
            onClick={() => {
              setSelectedType('all');
              setSelectedAudience('all');
              setSearchQuery('');
            }}
            className="text-sm font-bold text-brand-blue hover:underline"
          >
            Näita kõiki teenuseid
          </button>
        </div>
      )}

    </div>
  );
}

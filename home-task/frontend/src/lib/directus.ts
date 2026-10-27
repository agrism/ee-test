import { Service, ServiceCategory, DirectusPage } from './types';
import { SEED_SERVICES, SEED_CATEGORIES, SEED_HOMEPAGE } from './seed-data';

const DIRECTUS_URL = process.env.NEXT_PUBLIC_DIRECTUS_URL || 'http://localhost:8055';

export async function getHomepageData(): Promise<DirectusPage> {
  try {
    const res = await fetch(`${DIRECTUS_URL}/items/pages?filter[slug][_empty]=true`, {
      next: { revalidate: 60 }
    });
    if (res.ok) {
      const json = await res.json();
      if (json.data && json.data.length > 0) {
        return json.data[0];
      }
    }
  } catch (err) {
    // Graceful fallback to embedded seed data
  }
  return SEED_HOMEPAGE;
}

export async function getCategories(): Promise<ServiceCategory[]> {
  try {
    const res = await fetch(`${DIRECTUS_URL}/items/categories`, {
      next: { revalidate: 60 }
    });
    if (res.ok) {
      const json = await res.json();
      if (json.data && json.data.length > 0) {
        return json.data;
      }
    }
  } catch (err) {
    // Fallback
  }
  return SEED_CATEGORIES;
}

export async function getCategoryBySlug(slug: string): Promise<ServiceCategory | null> {
  const cats = await getCategories();
  return cats.find(c => c.slug === slug) || null;
}

export async function getServices(): Promise<Service[]> {
  try {
    const res = await fetch(`${DIRECTUS_URL}/items/services`, {
      next: { revalidate: 60 }
    });
    if (res.ok) {
      const json = await res.json();
      if (json.data && json.data.length > 0) {
        return json.data;
      }
    }
  } catch (err) {
    // Fallback
  }
  return SEED_SERVICES;
}

export async function getServicesByCategory(categorySlug: string): Promise<Service[]> {
  const allServices = await getServices();
  return allServices.filter(s => s.categorySlug === categorySlug);
}

export async function getServiceBySlug(slug: string): Promise<Service | null> {
  const allServices = await getServices();
  return allServices.find(s => s.slug === slug) || null;
}

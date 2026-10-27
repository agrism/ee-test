export type ServiceCategory = {
  id: string;
  name: string;
  slug: string;
  description: string;
  iconName: string;
};

export type Service = {
  id: string;
  title: string;
  slug: string;
  categorySlug: string;
  categoryName: string;
  summary: string;
  targetAudience: string[];
  serviceType: 'grant' | 'loan_guarantee' | 'advisory';
  maxAmount?: string;
  intensityPercent?: string;
  status: 'open' | 'ongoing' | 'upcoming';
  deadline?: string;
  description: string;
  eligibilityCriteria: string[];
  processSteps: {
    step: number;
    title: string;
    description: string;
  }[];
  partnerBanks?: string[];
  ctaUrl: string;
  ctaText: string;
  seoTitle: string;
  seoDescription: string;
};

export type PageBlock = {
  id: string;
  type: 'hero' | 'categories_grid' | 'services_grid' | 'steps' | 'cta' | 'faq';
  title?: string;
  subtitle?: string;
  data: any;
};

export type DirectusPage = {
  id: string;
  slug: string;
  title: string;
  seoTitle: string;
  seoDescription: string;
  blocks: PageBlock[];
};

export type McpToolResponse = {
  tool: string;
  query: string;
  matchedServices: Service[];
  explanation: string;
};

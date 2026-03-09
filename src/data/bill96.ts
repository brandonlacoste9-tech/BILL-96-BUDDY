export interface KeyArea {
  id: string;
  title: string;
  icon: string;
  summary: string;
  details: string[];
}

export interface AngleInfo {
  id: string;
  label: string;
  icon: string;
  description: string;
  obligations: string[];
  risks: string[];
  keyDates?: string[];
}

export const bill96Overview = {
  title: "Bill 96 — An Act respecting French, the official and common language of Québec",
  adopted: "May 2022",
  officialName: "Law 14",
  legislativeName: "Bill 96",
  amendedLaw: "Charter of the French Language (Bill 101)",
  purpose:
    "To affirm that French is the sole official language of Quebec and the common language of the Quebec nation, and to significantly expand French-language requirements across government, business, education, and the workplace.",
  summary:
    "Bill 96 is Quebec's major reform of its language laws. Adopted by the National Assembly in May 2022 and brought into force in stages, it strengthens the status of French as the province's only official and 'common' language, expanding requirements across government, business, education, and the workplace.",
};

export const keyAreas: KeyArea[] = [
  {
    id: "government",
    title: "Government and Courts",
    icon: "🏛️",
    summary:
      "Stronger obligation for civil administration to use French, with tighter limits on using English or bilingual documents.",
    details: [
      "Stronger obligation for the civil administration to use French in all internal and external communications.",
      "Tighter limits on using English or bilingual documents in dealings with the state.",
      "Exceptions apply for: Indigenous peoples, services outside Quebec, tourism, and recent immigrants (for a short adaptation period).",
      "Government bodies must communicate in French by default; requests for services in another language must meet stricter criteria.",
      "Court proceedings and legal documents must be in French, with exceptions for anglophone parties.",
    ],
  },
  {
    id: "workplace",
    title: "Language of Work",
    icon: "💼",
    summary:
      "Expands employees' right to work in French and requires employers to avoid unnecessary language demands.",
    details: [
      "Expands employees' right to work in French in all aspects of their employment.",
      "Employers must avoid imposing unnecessary requirements for knowledge of a language other than French.",
      "The French Charter's application extends to smaller businesses: now applies to businesses with 25+ employees (previously 50+).",
      "Employers must take concrete measures to generalize the use of French in the workplace.",
      "Written communications to employees must be in French; bilingual communications are only permitted in specific circumstances.",
      "Job postings must be in French; requiring knowledge of another language must be justified with documented necessity.",
    ],
  },
  {
    id: "business",
    title: "Business and Commerce",
    icon: "🏪",
    summary:
      "More stringent rules on French in commercial signage, advertising, contracts, and product labelling.",
    details: [
      "French must be clearly predominant on commercial signage and advertising materials.",
      "Contracts, purchase orders, and other commercial documents must be in French.",
      "Product labelling and packaging must include French descriptions; French must be at least as prominent as any other language.",
      "For trademarks and product packaging: new regulations tied to Bill 96 took effect June 1, 2025.",
      "Grace period until June 1, 2027 for non-compliant products manufactured before June 1, 2025.",
      "No grace period for public signage — compliance was required immediately upon the regulation's coming into force.",
      "Websites and digital platforms serving Quebec consumers must offer a French-language option.",
      "Software and computer interfaces used in Quebec workplaces must be available in French.",
    ],
  },
  {
    id: "education",
    title: "Education",
    icon: "🎓",
    summary:
      "Imposes caps on English-language CEGEP enrollment and adds French-language course requirements.",
    details: [
      "Imposes caps and quotas on English-language CEGEP (college) enrollment.",
      "Adds mandatory French-language course requirements even for students at English-language institutions.",
      "Restricts access to English-language CEGEPs for francophone and allophone students.",
      "Students who attended English-language primary and secondary schools may have continued access to English CEGEPs.",
      "Universities must increase French-language programming and services.",
      "Strengthens French-language requirements in professional integration programs for newcomers.",
    ],
  },
  {
    id: "enforcement",
    title: "Enforcement and Sanctions",
    icon: "⚖️",
    summary:
      "Strengthens OQLF powers and substantially increases fines for non-compliance.",
    details: [
      "Strengthens the powers of the Office québécois de la langue française (OQLF) to investigate, issue orders, and enforce compliance.",
      "The OQLF can now conduct inspections and issue orders without prior complaint.",
      "Increased fines for companies: recurring non-compliance can reach up to tens of thousands of dollars per day.",
      "Individual fines also scale up substantially for repeat violations.",
      "Companies found in violation can have their permits or licenses suspended or revoked.",
      "Directors and officers of corporations can be held personally liable for violations.",
      "A new right of private action allows individuals to sue for damages related to language rights violations.",
    ],
  },
];

export const angles: AngleInfo[] = [
  {
    id: "employer",
    label: "Employer",
    icon: "🏢",
    description:
      "You own or manage a business operating in Quebec with employees.",
    obligations: [
      "If you have 25 or more employees, you must implement a francization program.",
      "Job postings must be in French; requiring another language must be documented and justified.",
      "All internal written communications to employees must be in French.",
      "Software and computer systems used in the workplace must be available in French.",
      "Contracts with suppliers, clients, and partners based in Quebec must be in French.",
      "Commercial signage must clearly display French as the predominant language.",
      "Product labels on goods sold in Quebec must prominently feature French.",
    ],
    risks: [
      "Fines of up to tens of thousands of dollars per day for recurring non-compliance.",
      "OQLF inspections can occur without a prior complaint from an employee or customer.",
      "Directors and officers can be personally liable for corporate violations.",
      "Operating permits or licenses may be suspended or revoked for serious infractions.",
      "Employees have the right to file complaints if they feel pressured to work in a language other than French.",
    ],
    keyDates: [
      "June 1, 2025: New regulations on trademarks and product packaging took effect.",
      "June 1, 2027: Grace period ends for products manufactured before June 1, 2025.",
      "Signage compliance: No grace period — immediate compliance required.",
    ],
  },
  {
    id: "employee",
    label: "Employee",
    icon: "👤",
    description:
      "You work for an employer in Quebec and want to know your language rights.",
    obligations: [
      "You are not personally subject to fines under Bill 96; your employer bears compliance obligations.",
      "You have the right to request communications and documents from your employer in French.",
    ],
    risks: [
      "If your employer requires you to work in a language other than French without documented justification, this may be a violation you can report.",
      "Changes in workplace language policies may affect your day-to-day work environment.",
    ],
    keyDates: [
      "Your employer must comply with francization requirements — check whether your company has 25+ employees.",
    ],
  },
  {
    id: "student",
    label: "Student",
    icon: "📚",
    description:
      "You are a student in Quebec considering post-secondary education options.",
    obligations: [
      "Francophone and allophone students face restricted access to English-language CEGEPs.",
      "If attending an English-language CEGEP, you must complete mandatory French-language courses.",
      "Access to English CEGEPs is determined by your educational background (English primary/secondary schooling may qualify you).",
    ],
    risks: [
      "Enrollment caps at English CEGEPs may limit your ability to attend your preferred institution.",
      "Failure to complete mandatory French-language courses may affect your academic standing.",
      "University programs may have increased French-language requirements even at English-language institutions.",
    ],
    keyDates: [
      "Enrollment caps and course requirements are enforced each academic year.",
    ],
  },
  {
    id: "citizen",
    label: "Citizen",
    icon: "🧑",
    description:
      "You are a Quebec resident and want to understand how Bill 96 affects your daily life.",
    obligations: [
      "As an individual citizen, Bill 96 does not impose direct obligations on you.",
      "You have the right to receive services in French from government bodies, businesses, and professionals.",
    ],
    risks: [
      "Businesses, landlords, and service providers may change how they communicate with you to comply with French-language requirements.",
      "Access to English-language government services may become more restricted over time.",
      "New immigrants have a short adaptation period before being required to interact with the state primarily in French.",
    ],
    keyDates: [
      "New immigrants: transitional period for French-language interactions with the state.",
    ],
  },
  {
    id: "developer",
    label: "Software Developer / Tech Company",
    icon: "💻",
    description:
      "You develop software, apps, or digital products used in Quebec.",
    obligations: [
      "Software and computer interfaces used in Quebec workplaces must be available in French.",
      "Consumer-facing digital products and websites serving Quebec users must offer a French-language option.",
      "Digital contracts, terms of service, and user agreements for Quebec customers must be available in French.",
      "Product documentation and user manuals distributed in Quebec must include French versions.",
      "If your company has 25+ employees in Quebec, workplace language francization obligations apply to your team.",
    ],
    risks: [
      "Non-compliant software deployed in Quebec workplaces can expose employers to OQLF fines — and may affect your contracts.",
      "Failure to provide French-language interfaces for consumer-facing products can attract complaints to the OQLF.",
      "Contracts or terms of service that are only in English may be unenforceable against Quebec consumers.",
      "Employers in Quebec who use English-only software may face enforcement action, creating pressure to switch vendors.",
    ],
    keyDates: [
      "June 1, 2025: Full enforcement of digital product labelling and packaging regulations.",
      "Ongoing: OQLF can inspect any business at any time for language compliance.",
    ],
  },
];

/**
 * Bill 96 Buddy — Interactive Role-Based Guidance
 *
 * Provides role-specific Bill 96 compliance information when a user
 * selects their role (employer, employee, business owner, student, citizen).
 */

'use strict';

/**
 * Guidance content keyed by role.
 * Each role has a title, intro, and an array of obligation sections.
 */
const ROLE_GUIDANCE = {
  employer: {
    title: '👔 Employer Obligations under Bill 96',
    intro:
      'As an employer in Quebec, Bill 96 significantly expands your obligations regarding ' +
      'the language of work. Here is what you need to know:',
    sections: [
      {
        heading: 'Threshold Lowered to 25+ Employees',
        riskLevel: 'high',
        items: [
          'The Charter of the French Language now applies to businesses with <strong>25 or more employees</strong> (previously 50+).',
          'If your headcount is between 25 and 49, you must comply with the "francization" obligations.',
          'You must implement a francization program or obtain a francization certificate from the OQLF.',
        ],
      },
      {
        heading: 'Language of Work',
        riskLevel: 'high',
        items: [
          'Employees have the legal right to work in French — you must not require them to use another language as a condition of employment unless clearly necessary.',
          'Job postings must be in French. English-only postings are prohibited.',
          'You cannot require knowledge of a language other than French unless the nature of the job genuinely requires it, and you must document why.',
          'Internal communications, training materials, and employee evaluations must be available in French.',
        ],
      },
      {
        heading: 'Contracts and Documents',
        items: [
          'Employment contracts must be drafted in French. A bilingual contract may be offered only if the employee explicitly requests it.',
          'Internal HR documents, policies, and handbooks must be in French.',
          'Contracts with Quebec government entities must be in French.',
        ],
      },
      {
        heading: 'OQLF Oversight',
        items: [
          'The Office québécois de la langue française (OQLF) can conduct audits and inspections.',
          'Non-compliance can result in orders to correct practices and substantial fines — up to tens of thousands of dollars per day for recurring violations.',
        ],
      },
    ],
  },

  employee: {
    title: '🧑‍💼 Employee Rights under Bill 96',
    intro:
      'Bill 96 strengthens your right to work in French in Quebec. Here are the key protections ' +
      'and rights you now have:',
    sections: [
      {
        heading: 'Right to Work in French',
        riskLevel: null,
        items: [
          'You have the legal right to communicate with your employer and colleagues in French.',
          'Your employer cannot require you to use another language unless it is clearly necessary for your specific role.',
          'Employers must provide training, manuals, and performance reviews in French.',
        ],
      },
      {
        heading: 'Protection Against Language-Based Requirements',
        items: [
          'Employers must not require knowledge of English or another language in job postings unless they can demonstrate it is genuinely required.',
          'You cannot be dismissed, demoted, or disciplined solely because you choose to work in French.',
        ],
      },
      {
        heading: 'Filing a Complaint',
        items: [
          'If your language rights are violated, you can file a complaint with the <strong>Office québécois de la langue française (OQLF)</strong>.',
          'The OQLF has strengthened powers to investigate and enforce compliance.',
          'You may also consult the <strong>Commission des droits de la personne et des droits de la jeunesse (CDPDJ)</strong> for discrimination related to language rights.',
        ],
      },
      {
        heading: 'Contracts and Documents',
        items: [
          'Your employment contract must be provided in French.',
          'If offered a bilingual contract, you can request a French-only version.',
        ],
      },
    ],
  },

  business: {
    title: '🏪 Business Owner Obligations under Bill 96',
    intro:
      'Bill 96 imposes strict new requirements on how businesses display French in public and ' +
      'conduct their commercial activities. Non-compliance can be costly:',
    sections: [
      {
        heading: 'Commercial Signage — Immediate Compliance Required',
        riskLevel: 'high',
        items: [
          'French must be <strong>clearly predominant</strong> on all public-facing signs, posters, and commercial advertising.',
          'The French text must be at least twice the size of any other language text on signs.',
          '<strong>There is no grace period for public signage</strong> — you must comply immediately.',
          'This applies to storefronts, window displays, menus, digital screens, and outdoor advertising.',
        ],
      },
      {
        heading: 'Product Labelling and Packaging',
        riskLevel: 'high',
        items: [
          'New regulations for trademarks and product packaging took effect <strong>June 1, 2025</strong>.',
          'Products manufactured before June 1, 2025 have a grace period until <strong>June 1, 2027</strong> to comply.',
          'Products manufactured on or after June 1, 2025 must comply immediately.',
          'All product descriptions, instructions, warranties, and safety information must be in French (at a minimum).',
        ],
      },
      {
        heading: 'Contracts and Advertising',
        items: [
          'Consumer contracts must be in French. An English version may be provided if the consumer explicitly requests it.',
          'All commercial advertising must be in French. Advertising in another language is only permissible if the French version is equally prominent.',
          'Contracts with Quebec government bodies must be exclusively in French.',
        ],
      },
      {
        heading: 'Employer Obligations (if you have 25+ employees)',
        items: [
          'If you have 25 or more employees, you are also subject to the language-of-work obligations. See the Employer role for details.',
        ],
      },
      {
        heading: 'Enforcement and Fines',
        riskLevel: 'high',
        items: [
          'The OQLF can issue compliance orders and conduct inspections without prior notice.',
          'Fines for companies: first offence up to $20,000; repeat violations can reach <strong>tens of thousands of dollars per day</strong>.',
          'Fines for individuals: up to $7,000 for repeat violations.',
        ],
      },
    ],
  },

  student: {
    title: '🎓 Student Obligations under Bill 96',
    intro:
      'Bill 96 affects access to English-language post-secondary education and imposes new French-language ' +
      'course requirements. Here is what students need to know:',
    sections: [
      {
        heading: 'English-Language CEGEP Enrollment Caps',
        riskLevel: 'high',
        items: [
          'Bill 96 imposes <strong>enrollment caps</strong> on English-language CEGEPs, limiting the proportion of anglophone, allophone, and francophone students who can attend.',
          'Students who attended English primary and secondary school (i.e., those with historical rights) are generally exempt from the caps.',
          'Students from outside Quebec attending English CEGEPs may face tighter restrictions.',
        ],
      },
      {
        heading: 'French Language Course Requirements',
        items: [
          'Even if you attend an English-language CEGEP, you may be required to complete French-language courses as part of your program.',
          'Additional French-language proficiency requirements may apply depending on your background and program.',
        ],
      },
      {
        heading: 'Workplace Rights After Graduation',
        items: [
          'Once you enter the Quebec workforce, you have the right to work in French regardless of where you studied.',
          'Employers cannot require bilingualism unless genuinely necessary for the position.',
        ],
      },
      {
        heading: 'Exemptions',
        items: [
          'Indigenous students and certain other groups have specific exemptions — consult the OQLF or your institution for details.',
          'Recent immigrants may also benefit from a short transitional period for certain language requirements.',
        ],
      },
    ],
  },

  citizen: {
    title: '🏠 Citizen Rights and Impacts under Bill 96',
    intro:
      'For everyday citizens in Quebec, Bill 96 strengthens your right to receive services in French and ' +
      'impacts many areas of daily life:',
    sections: [
      {
        heading: 'Government Services in French',
        riskLevel: null,
        items: [
          'You have the right to receive all provincial government services in French.',
          'The government has a stronger obligation to communicate in French in all official documents, notices, and interactions.',
          'Limited exceptions apply for communications in English for those with historical English-language rights, Indigenous peoples, and recent immigrants during a transitional period.',
        ],
      },
      {
        heading: 'Commercial and Consumer Rights',
        items: [
          'Consumer contracts (e.g., leases, cellphone plans, insurance policies) must be provided in French.',
          'Product labels, instructions, warranties, and safety information must be in French.',
          'Commercial signage you encounter must display French prominently.',
        ],
      },
      {
        heading: 'Courts and Legal Proceedings',
        items: [
          'You have the right to use French in all Quebec courts and legal proceedings.',
          'The obligation for courts to use French is strengthened, with tighter limits on English-language proceedings.',
        ],
      },
      {
        heading: 'Filing a Complaint',
        items: [
          'If you believe your language rights have been violated, you can file a complaint with the <strong>Office québécois de la langue française (OQLF)</strong>.',
          'The OQLF has stronger powers to investigate and issue compliance orders.',
        ],
      },
      {
        heading: 'Exemptions and Special Cases',
        items: [
          'Indigenous peoples in Quebec have specific exemptions from certain provisions.',
          'Recent immigrants benefit from a short transitional period for some language requirements.',
          'Tourism-related communications may be in other languages in certain contexts.',
        ],
      },
    ],
  },
};

/**
 * Renders the guidance HTML for a given role.
 * @param {string} role - One of: employer, employee, business, student, citizen
 * @returns {string} HTML string
 */
function renderGuidance(role) {
  const data = ROLE_GUIDANCE[role];
  if (!data) return '';

  let html = `<h2>${data.title}</h2><p>${data.intro}</p>`;

  for (const section of data.sections) {
    const riskBadge =
      section.riskLevel === 'high'
        ? '<span class="risk-badge high">High Risk</span>'
        : '';

    html += `<h3>${section.heading}${riskBadge}</h3><ul>`;
    for (const item of section.items) {
      html += `<li>${item}</li>`;
    }
    html += '</ul>';
  }

  return html;
}

/**
 * Initialise role-selection buttons and guidance panel.
 */
function init() {
  const buttons = document.querySelectorAll('.role-btn');
  const guidanceSection = document.getElementById('guidance');
  const guidanceContent = document.getElementById('guidance-content');

  if (!buttons.length || !guidanceSection || !guidanceContent) return;

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      const selectedRole = btn.getAttribute('data-role');

      // Update button states
      buttons.forEach(function (b) {
        b.classList.remove('active');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');

      // Render and show guidance
      guidanceContent.innerHTML = renderGuidance(selectedRole);
      guidanceSection.hidden = false;

      // Scroll guidance into view smoothly
      guidanceSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
}

// Initialise when DOM is ready (browser only)
if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}

// Export for testing (CommonJS)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ROLE_GUIDANCE, renderGuidance };
}

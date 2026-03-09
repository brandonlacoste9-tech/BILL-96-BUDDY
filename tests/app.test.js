/**
 * Tests for Bill 96 Buddy — app.js
 *
 * Validates the core guidance data and rendering logic
 * without requiring a browser environment.
 */

'use strict';

const { ROLE_GUIDANCE, renderGuidance } = require('../app.js');

const KNOWN_ROLES = ['employer', 'employee', 'business', 'student', 'citizen'];

describe('ROLE_GUIDANCE data', () => {
  test('contains all required roles', () => {
    KNOWN_ROLES.forEach((role) => {
      expect(ROLE_GUIDANCE).toHaveProperty(role);
    });
  });

  KNOWN_ROLES.forEach((role) => {
    describe(`role: ${role}`, () => {
      test('has a title string', () => {
        expect(typeof ROLE_GUIDANCE[role].title).toBe('string');
        expect(ROLE_GUIDANCE[role].title.length).toBeGreaterThan(0);
      });

      test('has an intro string', () => {
        expect(typeof ROLE_GUIDANCE[role].intro).toBe('string');
        expect(ROLE_GUIDANCE[role].intro.length).toBeGreaterThan(0);
      });

      test('has at least one section', () => {
        expect(Array.isArray(ROLE_GUIDANCE[role].sections)).toBe(true);
        expect(ROLE_GUIDANCE[role].sections.length).toBeGreaterThan(0);
      });

      test('every section has a heading and items', () => {
        ROLE_GUIDANCE[role].sections.forEach((section) => {
          expect(typeof section.heading).toBe('string');
          expect(section.heading.length).toBeGreaterThan(0);
          expect(Array.isArray(section.items)).toBe(true);
          expect(section.items.length).toBeGreaterThan(0);
        });
      });

      test('riskLevel is null or a valid string when present', () => {
        ROLE_GUIDANCE[role].sections.forEach((section) => {
          if (section.riskLevel !== undefined) {
            expect(
              section.riskLevel === null || typeof section.riskLevel === 'string'
            ).toBe(true);
          }
        });
      });
    });
  });
});

describe('renderGuidance()', () => {
  test('returns an empty string for unknown roles', () => {
    expect(renderGuidance('unknown')).toBe('');
    expect(renderGuidance('')).toBe('');
    expect(renderGuidance(null)).toBe('');
  });

  KNOWN_ROLES.forEach((role) => {
    test(`renders non-empty HTML for role: ${role}`, () => {
      const html = renderGuidance(role);
      expect(typeof html).toBe('string');
      expect(html.length).toBeGreaterThan(0);
    });

    test(`rendered HTML for role ${role} contains a heading`, () => {
      const html = renderGuidance(role);
      expect(html).toContain('<h2>');
    });

    test(`rendered HTML for role ${role} contains list items`, () => {
      const html = renderGuidance(role);
      expect(html).toContain('<li>');
    });
  });

  test('employer guidance mentions 25 employee threshold', () => {
    const html = renderGuidance('employer');
    expect(html).toContain('25');
  });

  test('business guidance mentions June 1, 2025', () => {
    const html = renderGuidance('business');
    expect(html).toContain('2025');
  });

  test('business guidance mentions June 1, 2027 grace period', () => {
    const html = renderGuidance('business');
    expect(html).toContain('2027');
  });

  test('business guidance mentions no grace period for signage', () => {
    const html = renderGuidance('business');
    expect(html.toLowerCase()).toContain('no grace period');
  });

  test('employer guidance mentions high risk badge for employee threshold', () => {
    const html = renderGuidance('employer');
    expect(html).toContain('High Risk');
  });

  test('student guidance mentions enrollment caps', () => {
    const html = renderGuidance('student');
    expect(html.toLowerCase()).toContain('cap');
  });

  test('citizen guidance mentions OQLF', () => {
    const html = renderGuidance('citizen');
    expect(html).toContain('OQLF');
  });
});

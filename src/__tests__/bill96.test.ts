import { bill96Overview, keyAreas, angles } from "@/data/bill96";

describe("Bill 96 data", () => {
  describe("bill96Overview", () => {
    it("has a title", () => {
      expect(bill96Overview.title).toBeTruthy();
    });

    it("was adopted in May 2022", () => {
      expect(bill96Overview.adopted).toBe("May 2022");
    });

    it("has official name Law 14", () => {
      expect(bill96Overview.officialName).toBe("Law 14");
    });

    it("has legislative name Bill 96", () => {
      expect(bill96Overview.legislativeName).toBe("Bill 96");
    });

    it("amends the Charter of the French Language", () => {
      expect(bill96Overview.amendedLaw).toContain("Charter of the French Language");
    });

    it("has a summary describing French as official language", () => {
      expect(bill96Overview.summary.toLowerCase()).toContain("french");
    });
  });

  describe("keyAreas", () => {
    it("has 5 key areas", () => {
      expect(keyAreas).toHaveLength(5);
    });

    it("includes government area", () => {
      const gov = keyAreas.find((a) => a.id === "government");
      expect(gov).toBeDefined();
      expect(gov?.title).toBe("Government and Courts");
    });

    it("includes workplace area", () => {
      const wp = keyAreas.find((a) => a.id === "workplace");
      expect(wp).toBeDefined();
      expect(wp?.title).toBe("Language of Work");
    });

    it("includes business area", () => {
      const biz = keyAreas.find((a) => a.id === "business");
      expect(biz).toBeDefined();
      expect(biz?.title).toBe("Business and Commerce");
    });

    it("includes education area", () => {
      const edu = keyAreas.find((a) => a.id === "education");
      expect(edu).toBeDefined();
      expect(edu?.title).toBe("Education");
    });

    it("includes enforcement area", () => {
      const enf = keyAreas.find((a) => a.id === "enforcement");
      expect(enf).toBeDefined();
      expect(enf?.title).toBe("Enforcement and Sanctions");
    });

    it("each area has an icon, summary, and details", () => {
      keyAreas.forEach((area) => {
        expect(area.icon).toBeTruthy();
        expect(area.summary).toBeTruthy();
        expect(area.details.length).toBeGreaterThan(0);
      });
    });

    it("workplace area mentions 25 employees threshold", () => {
      const wp = keyAreas.find((a) => a.id === "workplace");
      const text = wp?.details.join(" ") ?? "";
      expect(text).toContain("25");
    });

    it("business area mentions June 1, 2025 key date", () => {
      const biz = keyAreas.find((a) => a.id === "business");
      const text = biz?.details.join(" ") ?? "";
      expect(text).toContain("June 1, 2025");
    });

    it("enforcement area mentions OQLF", () => {
      const enf = keyAreas.find((a) => a.id === "enforcement");
      const text = enf?.details.join(" ") ?? "";
      expect(text).toContain("OQLF");
    });
  });

  describe("angles", () => {
    it("has 5 angles", () => {
      expect(angles).toHaveLength(5);
    });

    it("includes employer, employee, student, citizen, and developer angles", () => {
      const ids = angles.map((a) => a.id);
      expect(ids).toContain("employer");
      expect(ids).toContain("employee");
      expect(ids).toContain("student");
      expect(ids).toContain("citizen");
      expect(ids).toContain("developer");
    });

    it("each angle has obligations and risks", () => {
      angles.forEach((angle) => {
        expect(angle.obligations.length).toBeGreaterThan(0);
        expect(angle.risks.length).toBeGreaterThan(0);
      });
    });

    it("employer angle mentions francization program", () => {
      const employer = angles.find((a) => a.id === "employer");
      const text = employer?.obligations.join(" ") ?? "";
      expect(text.toLowerCase()).toContain("francization");
    });

    it("employer angle mentions 25 employees threshold", () => {
      const employer = angles.find((a) => a.id === "employer");
      const text = employer?.obligations.join(" ") ?? "";
      expect(text).toContain("25");
    });

    it("student angle mentions CEGEP", () => {
      const student = angles.find((a) => a.id === "student");
      const text = [
        ...(student?.obligations ?? []),
        ...(student?.risks ?? []),
      ].join(" ");
      expect(text.toUpperCase()).toContain("CEGEP");
    });

    it("developer angle mentions software interfaces in French", () => {
      const dev = angles.find((a) => a.id === "developer");
      const text = dev?.obligations.join(" ") ?? "";
      expect(text.toLowerCase()).toContain("french");
    });

    it("each angle has an icon and label", () => {
      angles.forEach((angle) => {
        expect(angle.icon).toBeTruthy();
        expect(angle.label).toBeTruthy();
      });
    });
  });
});

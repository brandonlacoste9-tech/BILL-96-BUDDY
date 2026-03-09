import { render, screen } from "@testing-library/react";
import PersonalizedAdvice from "@/components/PersonalizedAdvice";
import { angles } from "@/data/bill96";

const employerAngle = angles.find((a) => a.id === "employer")!;
const citizenAngle = angles.find((a) => a.id === "citizen")!;

describe("PersonalizedAdvice", () => {
  it("renders the angle label", () => {
    render(<PersonalizedAdvice angle={employerAngle} />);
    expect(screen.getByText("Employer")).toBeInTheDocument();
  });

  it("renders the angle description", () => {
    render(<PersonalizedAdvice angle={employerAngle} />);
    expect(screen.getByText(employerAngle.description)).toBeInTheDocument();
  });

  it("renders the obligations section heading", () => {
    render(<PersonalizedAdvice angle={employerAngle} />);
    expect(screen.getByText("Your Obligations")).toBeInTheDocument();
  });

  it("renders obligations for the selected angle", () => {
    render(<PersonalizedAdvice angle={employerAngle} />);
    employerAngle.obligations.forEach((obligation) => {
      expect(screen.getByText(obligation)).toBeInTheDocument();
    });
  });

  it("renders the risks section heading", () => {
    render(<PersonalizedAdvice angle={employerAngle} />);
    expect(screen.getByText("Risks of Non-Compliance")).toBeInTheDocument();
  });

  it("renders risks for the selected angle", () => {
    render(<PersonalizedAdvice angle={employerAngle} />);
    employerAngle.risks.forEach((risk) => {
      expect(screen.getByText(risk)).toBeInTheDocument();
    });
  });

  it("renders key dates when present", () => {
    render(<PersonalizedAdvice angle={employerAngle} />);
    expect(screen.getByText("Key Dates")).toBeInTheDocument();
    employerAngle.keyDates?.forEach((date) => {
      expect(screen.getByText(date)).toBeInTheDocument();
    });
  });

  it("does not render key dates section when keyDates is absent", () => {
    const angleWithoutDates = { ...citizenAngle, keyDates: undefined };
    render(<PersonalizedAdvice angle={angleWithoutDates} />);
    expect(screen.queryByText("Key Dates")).not.toBeInTheDocument();
  });
});

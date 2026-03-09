import { render, screen, fireEvent } from "@testing-library/react";
import AngleSelector from "@/components/AngleSelector";
import { angles } from "@/data/bill96";

const mockOnSelect = jest.fn();

describe("AngleSelector", () => {
  beforeEach(() => {
    mockOnSelect.mockClear();
  });

  it("renders all angle buttons", () => {
    render(
      <AngleSelector
        angles={angles}
        selectedAngle={null}
        onSelect={mockOnSelect}
      />
    );
    angles.forEach((angle) => {
      expect(screen.getByText(angle.label)).toBeInTheDocument();
    });
  });

  it("calls onSelect with the angle id when clicked", () => {
    render(
      <AngleSelector
        angles={angles}
        selectedAngle={null}
        onSelect={mockOnSelect}
      />
    );
    fireEvent.click(screen.getByText("Employer"));
    expect(mockOnSelect).toHaveBeenCalledWith("employer");
  });

  it("marks selected angle button as pressed", () => {
    render(
      <AngleSelector
        angles={angles}
        selectedAngle="employer"
        onSelect={mockOnSelect}
      />
    );
    const employerBtn = screen.getByText("Employer").closest("button");
    expect(employerBtn).toHaveAttribute("aria-pressed", "true");
  });

  it("marks non-selected angle buttons as not pressed", () => {
    render(
      <AngleSelector
        angles={angles}
        selectedAngle="employer"
        onSelect={mockOnSelect}
      />
    );
    const studentBtn = screen.getByText("Student").closest("button");
    expect(studentBtn).toHaveAttribute("aria-pressed", "false");
  });

  it("passes angle id when same angle is clicked to deselect", () => {
    render(
      <AngleSelector
        angles={angles}
        selectedAngle="employer"
        onSelect={mockOnSelect}
      />
    );
    fireEvent.click(screen.getByText("Employer"));
    expect(mockOnSelect).toHaveBeenCalledWith("");
  });
});

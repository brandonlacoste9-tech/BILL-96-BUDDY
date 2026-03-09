import { render, screen, fireEvent } from "@testing-library/react";
import KeyAreaCard from "@/components/KeyAreaCard";
import { keyAreas } from "@/data/bill96";

const governmentArea = keyAreas.find((a) => a.id === "government")!;

describe("KeyAreaCard", () => {
  it("renders the area title", () => {
    render(<KeyAreaCard area={governmentArea} />);
    expect(
      screen.getByText("Government and Courts")
    ).toBeInTheDocument();
  });

  it("renders the area summary", () => {
    render(<KeyAreaCard area={governmentArea} />);
    expect(screen.getByText(governmentArea.summary)).toBeInTheDocument();
  });

  it("renders the icon", () => {
    render(<KeyAreaCard area={governmentArea} />);
    expect(screen.getByText(governmentArea.icon)).toBeInTheDocument();
  });

  it("does not show details by default", () => {
    render(<KeyAreaCard area={governmentArea} />);
    // Details list items should not be visible initially
    expect(
      screen.queryByText(governmentArea.details[0])
    ).not.toBeInTheDocument();
  });

  it("expands to show details on click", () => {
    render(<KeyAreaCard area={governmentArea} />);
    const button = screen.getByRole("button");
    fireEvent.click(button);
    expect(
      screen.getByText(governmentArea.details[0])
    ).toBeInTheDocument();
  });

  it("collapses details on second click", () => {
    render(<KeyAreaCard area={governmentArea} />);
    const button = screen.getByRole("button");
    fireEvent.click(button);
    expect(screen.getByText(governmentArea.details[0])).toBeInTheDocument();
    fireEvent.click(button);
    expect(
      screen.queryByText(governmentArea.details[0])
    ).not.toBeInTheDocument();
  });

  it("sets aria-expanded correctly", () => {
    render(<KeyAreaCard area={governmentArea} />);
    const button = screen.getByRole("button");
    expect(button).toHaveAttribute("aria-expanded", "false");
    fireEvent.click(button);
    expect(button).toHaveAttribute("aria-expanded", "true");
  });
});

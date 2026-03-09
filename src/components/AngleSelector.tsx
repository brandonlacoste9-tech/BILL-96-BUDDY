"use client";

import { AngleInfo } from "@/data/bill96";

interface AngleSelectorProps {
  angles: AngleInfo[];
  selectedAngle: string | null;
  onSelect: (id: string) => void;
}

export default function AngleSelector({
  angles,
  selectedAngle,
  onSelect,
}: AngleSelectorProps) {
  return (
    <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
      {angles.map((angle) => (
        <button
          key={angle.id}
          onClick={() => onSelect(angle.id === selectedAngle ? "" : angle.id)}
          className={`flex flex-col items-center gap-2 p-4 rounded-xl border-2 transition-all duration-200 ${
            selectedAngle === angle.id
              ? "border-blue-600 bg-blue-50 shadow-md"
              : "border-gray-200 bg-white hover:border-blue-300 hover:bg-blue-50"
          }`}
          aria-pressed={selectedAngle === angle.id}
        >
          <span className="text-3xl" aria-hidden="true">
            {angle.icon}
          </span>
          <span
            className={`text-sm font-medium text-center leading-tight ${
              selectedAngle === angle.id ? "text-blue-700" : "text-gray-700"
            }`}
          >
            {angle.label}
          </span>
        </button>
      ))}
    </div>
  );
}

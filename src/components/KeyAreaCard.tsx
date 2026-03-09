"use client";

import { useState } from "react";
import { KeyArea } from "@/data/bill96";

interface KeyAreaCardProps {
  area: KeyArea;
}

export default function KeyAreaCard({ area }: KeyAreaCardProps) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden transition-all duration-200">
      <button
        onClick={() => setExpanded(!expanded)}
        className="w-full text-left p-6 flex items-start gap-4 hover:bg-gray-50 transition-colors"
        aria-expanded={expanded}
        aria-controls={`area-details-${area.id}`}
      >
        <span className="text-3xl flex-shrink-0" aria-hidden="true">
          {area.icon}
        </span>
        <div className="flex-1 min-w-0">
          <h3 className="text-lg font-semibold text-gray-900">{area.title}</h3>
          <p className="text-gray-600 mt-1 text-sm">{area.summary}</p>
        </div>
        <span
          className={`flex-shrink-0 text-gray-400 transition-transform duration-200 mt-1 ${
            expanded ? "rotate-180" : ""
          }`}
          aria-hidden="true"
        >
          ▼
        </span>
      </button>

      {expanded && (
        <div
          id={`area-details-${area.id}`}
          className="px-6 pb-6 border-t border-gray-100"
        >
          <ul className="mt-4 space-y-3">
            {area.details.map((detail, index) => (
              <li key={index} className="flex items-start gap-3 text-sm text-gray-700">
                <span
                  className="flex-shrink-0 w-5 h-5 bg-blue-100 text-blue-700 rounded-full flex items-center justify-center text-xs font-bold mt-0.5"
                  aria-hidden="true"
                >
                  {index + 1}
                </span>
                {detail}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

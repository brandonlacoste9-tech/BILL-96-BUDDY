"use client";

import { AngleInfo } from "@/data/bill96";

interface PersonalizedAdviceProps {
  angle: AngleInfo;
}

export default function PersonalizedAdvice({ angle }: PersonalizedAdviceProps) {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-blue-100 overflow-hidden">
      <div className="bg-blue-600 px-6 py-4 flex items-center gap-3">
        <span className="text-3xl" aria-hidden="true">
          {angle.icon}
        </span>
        <div>
          <h3 className="text-xl font-bold text-white">{angle.label}</h3>
          <p className="text-blue-100 text-sm mt-0.5">{angle.description}</p>
        </div>
      </div>

      <div className="p-6 space-y-6">
        <section>
          <h4 className="text-base font-semibold text-gray-900 mb-3 flex items-center gap-2">
            <span className="text-green-600" aria-hidden="true">✅</span>
            Your Obligations
          </h4>
          <ul className="space-y-2">
            {angle.obligations.map((obligation, index) => (
              <li
                key={index}
                className="flex items-start gap-3 text-sm text-gray-700"
              >
                <span
                  className="flex-shrink-0 w-1.5 h-1.5 bg-green-500 rounded-full mt-1.5"
                  aria-hidden="true"
                />
                {obligation}
              </li>
            ))}
          </ul>
        </section>

        <section>
          <h4 className="text-base font-semibold text-gray-900 mb-3 flex items-center gap-2">
            <span className="text-red-600" aria-hidden="true">⚠️</span>
            Risks of Non-Compliance
          </h4>
          <ul className="space-y-2">
            {angle.risks.map((risk, index) => (
              <li
                key={index}
                className="flex items-start gap-3 text-sm text-gray-700"
              >
                <span
                  className="flex-shrink-0 w-1.5 h-1.5 bg-red-500 rounded-full mt-1.5"
                  aria-hidden="true"
                />
                {risk}
              </li>
            ))}
          </ul>
        </section>

        {angle.keyDates && angle.keyDates.length > 0 && (
          <section>
            <h4 className="text-base font-semibold text-gray-900 mb-3 flex items-center gap-2">
              <span aria-hidden="true">📅</span>
              Key Dates
            </h4>
            <ul className="space-y-2">
              {angle.keyDates.map((date, index) => (
                <li
                  key={index}
                  className="flex items-start gap-3 text-sm text-gray-700"
                >
                  <span
                    className="flex-shrink-0 w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5"
                    aria-hidden="true"
                  />
                  {date}
                </li>
              ))}
            </ul>
          </section>
        )}
      </div>
    </div>
  );
}

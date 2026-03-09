"use client";

import { useState } from "react";
import { angles, bill96Overview, keyAreas } from "@/data/bill96";
import AngleSelector from "@/components/AngleSelector";
import KeyAreaCard from "@/components/KeyAreaCard";
import PersonalizedAdvice from "@/components/PersonalizedAdvice";

export default function Home() {
  const [selectedAngle, setSelectedAngle] = useState<string | null>(null);

  const activeAngle = angles.find((a) => a.id === selectedAngle) ?? null;

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-blue-700 text-white">
        <div className="max-w-5xl mx-auto px-4 py-10 text-center">
          <div className="flex items-center justify-center gap-3 mb-3">
            <span className="text-4xl" aria-hidden="true">🇶🇨</span>
            <h1 className="text-4xl font-bold tracking-tight">Bill 96 Buddy</h1>
          </div>
          <p className="text-blue-100 text-lg max-w-2xl mx-auto">
            Your plain-language guide to Quebec&apos;s French language law reform
          </p>
          <div className="mt-4 inline-flex items-center gap-2 bg-blue-600 rounded-full px-4 py-2 text-sm text-blue-100">
            <span aria-hidden="true">📋</span>
            <span>
              <strong className="text-white">{bill96Overview.officialName}</strong> (
              {bill96Overview.legislativeName}) · Adopted {bill96Overview.adopted}
            </span>
          </div>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 py-10 space-y-12">
        {/* Overview */}
        <section aria-labelledby="overview-heading">
          <h2
            id="overview-heading"
            className="text-2xl font-bold text-gray-900 mb-4"
          >
            What is Bill 96?
          </h2>
          <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
            <p className="text-gray-700 leading-relaxed">
              {bill96Overview.summary}
            </p>
            <div className="mt-4 pt-4 border-t border-gray-100 grid grid-cols-1 sm:grid-cols-3 gap-4 text-sm">
              <div>
                <span className="text-gray-500 uppercase tracking-wide text-xs font-semibold">
                  Official Name
                </span>
                <p className="text-gray-900 font-medium mt-1">
                  {bill96Overview.officialName}
                </p>
              </div>
              <div>
                <span className="text-gray-500 uppercase tracking-wide text-xs font-semibold">
                  Legislative Name
                </span>
                <p className="text-gray-900 font-medium mt-1">
                  {bill96Overview.legislativeName}
                </p>
              </div>
              <div>
                <span className="text-gray-500 uppercase tracking-wide text-xs font-semibold">
                  Amends
                </span>
                <p className="text-gray-900 font-medium mt-1">
                  {bill96Overview.amendedLaw}
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Key Areas */}
        <section aria-labelledby="key-areas-heading">
          <h2
            id="key-areas-heading"
            className="text-2xl font-bold text-gray-900 mb-4"
          >
            Key Areas of Bill 96
          </h2>
          <p className="text-gray-600 mb-6">
            Select any area to expand its details.
          </p>
          <div className="space-y-4">
            {keyAreas.map((area) => (
              <KeyAreaCard key={area.id} area={area} />
            ))}
          </div>
        </section>

        {/* Angle Selector */}
        <section aria-labelledby="angle-heading">
          <h2
            id="angle-heading"
            className="text-2xl font-bold text-gray-900 mb-2"
          >
            What&apos;s Your Angle?
          </h2>
          <p className="text-gray-600 mb-6">
            Select your role to see the specific Bill 96 obligations and risks
            that apply to you.
          </p>
          <AngleSelector
            angles={angles}
            selectedAngle={selectedAngle}
            onSelect={setSelectedAngle}
          />
        </section>

        {/* Personalized Advice */}
        {activeAngle && (
          <section aria-labelledby="advice-heading">
            <h2
              id="advice-heading"
              className="text-2xl font-bold text-gray-900 mb-4"
            >
              Your Bill 96 Summary
            </h2>
            <PersonalizedAdvice angle={activeAngle} />
          </section>
        )}

        {/* Disclaimer */}
        <footer className="border-t border-gray-200 pt-8 pb-4">
          <p className="text-xs text-gray-500 leading-relaxed text-center max-w-3xl mx-auto">
            <strong>Disclaimer:</strong> This tool provides general information
            about Bill 96 for educational purposes only. It does not constitute
            legal advice. Laws and regulations change frequently; always consult
            a qualified Quebec lawyer or the{" "}
            <a
              href="https://www.oqlf.gouv.qc.ca/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 hover:underline"
            >
              Office québécois de la langue française (OQLF)
            </a>{" "}
            for authoritative guidance.
          </p>
        </footer>
      </main>
    </div>
  );
}

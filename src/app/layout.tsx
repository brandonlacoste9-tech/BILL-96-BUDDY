import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Bill 96 Buddy",
  description:
    "Your guide to Bill 96 — Quebec's major reform of its language laws strengthening French as the province's official and common language.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}

import "@/styles/globals.css";

export const metadata = {
  title: "Next.js App",
  description: "Generated with appgen",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

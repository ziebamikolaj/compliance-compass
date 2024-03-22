import React from 'react';
import type { Metadata } from 'next';
import './globals.css';
import Navigation from '@/components/navigation';
import Providers from './providers';

export const metadata: Metadata = {
  title: 'Compliance compass',
  description: 'Compliance compass',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body>
        <Providers>
          <Navigation />
          {children}
        </Providers>
      </body>
    </html>
  );
}

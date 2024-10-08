import '@/styles/global.css'

import type { Metadata } from 'next'
import { Source_Sans_3 } from 'next/font/google'

import { ThemeProviders } from './theme-providers'
import { BarsWrapper } from './layout-bars/bars-wrapper'

export const metadata: Metadata = {
  title: 'IoT System',
}

const sourceSans3 = Source_Sans_3({
  weight: ['400', '600', '700'],
  subsets: ['latin'],
  display: 'swap',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    /* eslint-disable camelcase */
    <html lang="en" className={sourceSans3.className}>
      <body>
        <ThemeProviders>
          <BarsWrapper>{children}</BarsWrapper>
        </ThemeProviders>
      </body>
    </html>
  )
}

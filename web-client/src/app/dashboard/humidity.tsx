'use client'

import { Box, Typography, useTheme } from '@mui/material'
import useMediaQuery from '@mui/material/useMediaQuery'

import { tokens } from '@/styles/theme'
import { LineChart } from '@/components/line-chart'

import { mockHumidityData } from '@/data/mockData'

export function Humidity() {
  const theme = useTheme()
  const colors = tokens(theme.palette.mode)
  const isNonMobile = useMediaQuery('(min-width:600px)')

  return (
    <>
      <Box
        gridColumn={isNonMobile ? 'span 12' : 'span 12'}
        gridRow="span 2"
        sx={{ backgroundColor: colors.primary[400] }}
      >
        <Typography
          variant="h5"
          fontWeight="600"
          sx={{ padding: '30px 30px 0 30px' }}
        >
          Humidity
        </Typography>

        <Box height="250px" ml="-20px">
          <LineChart isDashboard={true} data={mockHumidityData} />
        </Box>
        {/* <Box height="250px" mt="-20px">
          <BarChart isDashboard={true} />
        </Box> */}
      </Box>
    </>
  )
}

'use client'

import useSWR from 'swr'
import { Box, Typography, useTheme } from '@mui/material'
import useMediaQuery from '@mui/material/useMediaQuery'

import { tokens } from '@/styles/theme'
import { LineChart } from '@/components/line-chart'
import { DashboardAPI } from '@/api/dashboard'

export function Humidity() {
  const theme = useTheme()
  const colors = tokens(theme.palette.mode)
  const isNonMobile = useMediaQuery('(min-width:600px)')

  const sensorId = 1 // Replace with the appropriate sensor ID

  // Use useSWR to fetch humidity data
  const { data: humidityData, error } = useSWR(
      [`humidity-data-${sensorId}`, sensorId],
      async () => {
        const res = await DashboardAPI.getHumidityChartData(sensorId)
        if (res.status !== 200) {
          throw new Error('Failed to fetch humidity data')
        }
        return res.data
      }
  )

  // Handle loading and error states
  if (error) return <Typography color="error">An error occurred while fetching humidity data</Typography>
  if (!humidityData) return <Typography>Loading...</Typography>

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
            {/* Pass the fetched humidity data to the LineChart */}
            <LineChart isDashboard={true} data={humidityData} />
          </Box>
        </Box>
      </>
  )
}

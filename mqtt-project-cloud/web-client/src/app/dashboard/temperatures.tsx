'use client'

import useSWR from 'swr'
import { Box, Typography, useTheme } from '@mui/material'
import useMediaQuery from '@mui/material/useMediaQuery'

import { tokens } from '@/styles/theme'
import { LineChart } from '@/components/line-chart'
import { DashboardAPI } from '@/api/dashboard'

export function Temperature() {
  const theme = useTheme()
  const colors = tokens(theme.palette.mode)
  const isNonMobile = useMediaQuery('(min-width:600px)')

  const sensorId = 1  // Replace with the appropriate sensor ID if needed

  // Use useSWR with async function and await
  const { data: temperatureData, error } = useSWR(
      [`temperature-data-${sensorId}`, sensorId],
      async () => {
        const res = await DashboardAPI.getTemperatureChartData(sensorId)

        if (res.status !== 200) {
          throw new Error('Failed to fetch temperature data')
        }

        return res.data
      }
  )

  if (error) return <Typography color="error">An error occurred while fetching temperature data</Typography>
  if (!temperatureData) return <Typography>Loading...</Typography>

  return (
      <Box
          gridColumn={isNonMobile ? 'span 12' : 'span 12'}
          gridRow="span 2"
          sx={{ backgroundColor: colors.primary[400] }}
      >
        <Box
            mt="25px"
            p="0 30px"
            display="flex"
            justifyContent="space-between"
            alignItems="center"
        >
          <Box>
            <Typography variant="h5" fontWeight="600" color={colors.grey[100]}>
              Temperature
            </Typography>
          </Box>
        </Box>

        <Box height="250px" ml="-20px">
          <LineChart isDashboard data={temperatureData} />  {/* Pass the fetched data */}
        </Box>
      </Box>
  )
}

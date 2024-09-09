'use client'

import useSWR from 'swr'
import { Box, Typography, useTheme } from '@mui/material'
import useMediaQuery from '@mui/material/useMediaQuery'

import { tokens } from '@/styles/theme'
import { LineChart } from '@/components/line-chart'
import { DashboardAPI } from '@/api/dashboard'

export function Moisture() {
  const theme = useTheme()
  const colors = tokens(theme.palette.mode)
  const isNonMobile = useMediaQuery('(min-width:600px)')

  const sensorId = 2  // Replace with the appropriate sensor ID if needed

  // Use useSWR with async function and await
  const { data: moistureData, error } = useSWR(
      [`moisture-data-${sensorId}`, sensorId],
      async () => {
        const res = await DashboardAPI.getMoistureChartData(sensorId)

        if (res.status !== 200) {
          throw new Error('Failed to fetch moisture data')
        }

        return res.data
      }
  )

  if (error) return <Typography color="error">An error occurred while fetching moisture data</Typography>
  if (!moistureData) return <Typography>Loading...</Typography>

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
              Moisture
            </Typography>
          </Box>
        </Box>

        <Box height="250px" ml="-20px">
          <LineChart isDashboard data={moistureData} />  {/* Pass the fetched data */}
        </Box>
      </Box>
  )
}

'use client'

import { Box, Typography, useTheme } from '@mui/material'
import useMediaQuery from '@mui/material/useMediaQuery'
// import useSWR from 'swr'

// import { fetcher } from '@/api/setting'
import { tokens } from '@/styles/theme'
import { LineChart } from '@/components/line-chart'

import { mockLineData } from '@/data/mockData'
import DashboardAPI from '@/api/dashboard'
// import { SERVER_BASE_URL, ENDPOINT } from '@/utils/constant'

const Temperatures = () => {
  const theme = useTheme()
  const colors = tokens(theme.palette.mode)
  const isNonMobile = useMediaQuery('(min-width:600px)')

  // const { data: fetchedTemperature } = useSWR(
  //   `${SERVER_BASE_URL}/${ENDPOINT.TEMPERATURE}`,
  //   fetcher,
  // )

  return (
    <>
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
              Temperatures
            </Typography>
          </Box>
        </Box>

        <Box height="250px" ml="-20px">
          <LineChart isDashboard data={mockLineData} />
        </Box>
      </Box>
    </>
  )
}

Temperatures.getInitialProps = async () => {
  const { data } = await DashboardAPI.getLocations()
  return data
}

export default Temperatures

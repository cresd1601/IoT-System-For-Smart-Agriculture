'use client'

import { Box, Typography, useTheme } from '@mui/material'
import useMediaQuery from '@mui/material/useMediaQuery'

import { tokens } from '@/styles/theme'
import { LineChart } from '@/components/line-chart'

import { mockMoistureData } from '@/data/mockData'

export function Moisture() {
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
          <LineChart isDashboard data={mockMoistureData} />
        </Box>
        {/* <Box height="200px">
          <GeographyChart isDashboard={true} />
        </Box> */}
      </Box>
    </>
  )
}

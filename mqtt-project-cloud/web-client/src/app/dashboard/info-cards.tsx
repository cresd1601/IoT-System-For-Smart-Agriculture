'use client'

import { Box, useTheme } from '@mui/material'
import useMediaQuery from '@mui/material/useMediaQuery'
import ThermostatOutlinedIcon from '@mui/icons-material/ThermostatOutlined'
import WaterDropOutlinedIcon from '@mui/icons-material/WaterDropOutlined'
import OpacityOutlinedIcon from '@mui/icons-material/OpacityOutlined'

import { StatBox } from '@/components/stat-box'
import { tokens } from '@/styles/theme'

export function InfoCards() {
  const theme = useTheme()
  const colors = tokens(theme.palette.mode)
  const isNonMobile = useMediaQuery('(min-width:600px)')

  return (
    <>
      <Box
        gridColumn={isNonMobile ? 'span 4' : 'span 12'}
        display="flex"
        alignItems="center"
        justifyContent="center"
        sx={{ backgroundColor: colors.primary[400] }}
      >
        <StatBox
          title="32 &#176; C"
          subtitle="Temperatures"
          progress={91 / 100}
          increase={`${91} %`}
          icon={
            <ThermostatOutlinedIcon
              sx={{ color: colors.greenAccent[600], fontSize: '26px' }}
            />
          }
        />
      </Box>
      <Box
        gridColumn={isNonMobile ? 'span 4' : 'span 12'}
        display="flex"
        alignItems="center"
        justifyContent="center"
        sx={{ backgroundColor: colors.primary[400] }}
      >
        <StatBox
          title="67 %"
          subtitle="Humidity"
          progress={67 / 100}
          increase={`${67} %`}
          icon={
            <WaterDropOutlinedIcon
              sx={{ color: colors.greenAccent[600], fontSize: '26px' }}
            />
          }
        />
      </Box>
      <Box
        gridColumn={isNonMobile ? 'span 4' : 'span 12'}
        display="flex"
        alignItems="center"
        justifyContent="center"
        sx={{ backgroundColor: colors.primary[400] }}
      >
        <StatBox
          title="58 %"
          subtitle="Moisture"
          progress={58 / 100}
          increase={`${58} %`}
          icon={
            <OpacityOutlinedIcon
              sx={{ color: colors.greenAccent[600], fontSize: '26px' }}
            />
          }
        />
      </Box>
    </>
  )
}

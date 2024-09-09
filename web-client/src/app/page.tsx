import { Box } from '@mui/material'

import { DashboardHeader } from './dashboard/header'
import { InfoCards } from './dashboard/info-cards'
import Temperatures from './dashboard/temperatures'
import { Humidity } from './dashboard/humidity'
import { Moisture } from './dashboard/moisture'

export default async function Dashboard() {
  return (
    <Box component="main" m="20px">
      {/* HEADER */}
      <DashboardHeader />

      {/* GRID & CHARTS */}
      <Box
        display="grid"
        gridTemplateColumns="repeat(12, 1fr)"
        gridAutoRows="150px"
        gap="20px"
      >
        <InfoCards />

        {/* ROW 2 */}
        <Temperatures />

        {/* ROW 3 */}
        <Humidity />

        {/* ROW 3 */}
        <Moisture />
      </Box>
    </Box>
  )
}

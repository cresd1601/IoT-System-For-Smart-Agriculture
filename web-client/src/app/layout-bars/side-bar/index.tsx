'use client'

import { usePathname } from 'next/navigation'
import { useState } from 'react'
import { Sidebar, Menu, MenuItem } from 'react-pro-sidebar'
import { Box, IconButton, Typography, useTheme } from '@mui/material'
import HomeOutlinedIcon from '@mui/icons-material/HomeOutlined'
import MenuOutlinedIcon from '@mui/icons-material/MenuOutlined'
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined'
import ThermostatOutlinedIcon from '@mui/icons-material/ThermostatOutlined'
import WaterDropOutlinedIcon from '@mui/icons-material/WaterDropOutlined'
import OpacityOutlinedIcon from '@mui/icons-material/OpacityOutlined'

import { tokens } from '@/styles/theme'
import { SideBarItem } from './item'
import { UserInfo } from './user-info'

interface SideBarProps {
  toggled: boolean
  hideSideBar: () => void
}

export function SideBar({ toggled, hideSideBar }: SideBarProps) {
  const theme = useTheme()
  const colors = tokens(theme.palette.mode)
  const pathname = usePathname()
  const [isCollapsed, setIsCollapsed] = useState(false)
  const [selected, setSelected] = useState(pathname)

  return (
    <Box
      sx={{
        '& .ps-sidebar-container': {
          background: `${colors.primary[400]} !important`,
        },
        '& .ps-sidebar-root': {
          border: 'none',
        },
        '& .ps-menu-button:hover': {
          backgroundColor: `transparent !important`,
          color: `${colors.blueAccent[400]} !important`,
        },
        '& .ps-menu-button.ps-active': {
          color: `${colors.blueAccent[500]} !important`,
        },
      }}
    >
      <Sidebar
        collapsed={isCollapsed}
        style={{ height: '100%' }}
        toggled={toggled}
        breakPoint="md"
        onBackdropClick={hideSideBar}
      >
        <Menu>
          {/* LOGO AND MENU ICON */}
          <MenuItem
            onClick={() => setIsCollapsed(!isCollapsed)}
            icon={isCollapsed ? <MenuOutlinedIcon /> : undefined}
            rootStyles={{
              margin: '10px 0 20px 0',
              color: colors.grey[100],
            }}
          >
            {!isCollapsed && (
              <Box
                display="flex"
                justifyContent="space-between"
                alignItems="center"
                ml="15px"
              >
                <Typography variant="h3" color={colors.grey[100]}>
                  IoT Portal
                </Typography>
                <IconButton onClick={() => setIsCollapsed(!isCollapsed)}>
                  <MenuOutlinedIcon />
                </IconButton>
              </Box>
            )}
          </MenuItem>

          {/* USER */}
          {!isCollapsed && <UserInfo />}

          {/* MENU ITEMS */}
          <Box>
            <SideBarItem
              title="Dashboard"
              to="/"
              icon={<HomeOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
              hideSideBar={hideSideBar}
            />

            <Typography
              variant="h6"
              color={colors.grey[300]}
              sx={{ m: '15px 0 5px 20px' }}
            >
              Data
            </Typography>
            <SideBarItem
              title="Temperatures"
              to="/manages/temperatures"
              icon={<ThermostatOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
              hideSideBar={hideSideBar}
            />
            <SideBarItem
              title="Humidity"
              to="/manages/humidity "
              icon={<WaterDropOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
              hideSideBar={hideSideBar}
            />
            <SideBarItem
              title="Moisture"
              to="/manages/moisture"
              icon={<OpacityOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
              hideSideBar={hideSideBar}
            />

            <Typography
              variant="h6"
              color={colors.grey[300]}
              sx={{ m: '15px 0 5px 20px' }}
            >
              Setting
            </Typography>

            <SideBarItem
              title="System"
              to="/system"
              icon={<SettingsOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
              hideSideBar={hideSideBar}
            />
          </Box>
        </Menu>
      </Sidebar>
    </Box>
  )
}

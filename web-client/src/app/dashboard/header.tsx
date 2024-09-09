'use client';

import { Box, IconButton, useTheme } from '@mui/material';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import CachedOutlinedIcon from '@mui/icons-material/CachedOutlined';

import { Header } from '@/components/header';
import { tokens } from '@/styles/theme';

export function DashboardHeader() {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  console.log('Service IP:', process.env.NEXT_PUBLIC_SERVICE_IP); // Verify the correct IP is being used

  return (
    <Box
      display="flex"
      justifyContent="space-between"
      alignItems="center"
      sx={{
        '@media (max-width: 600px)': {
          flexDirection: 'column',
          justifyContent: 'center',
          textAlign: 'center',
          pb: '20px',
        },
      }}
    >
      <Header title="IoT System" subtitle="Welcome to your Weed Garden." />

      <Box display="flex">
        <Box display="grid" gridTemplateColumns="repeat(2, 1fr)" gap={2}>
          <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DatePicker
              label="Start date"
              // value={value}
              // onChange={(newValue) => setValue(newValue)}
            />
            <DatePicker
              label="End date"
              // value={value}
              // onChange={(newValue) => setValue(newValue)}
            />
          </LocalizationProvider>
        </Box>
        <IconButton>
          <CachedOutlinedIcon
            sx={{ fontSize: '26px', color: colors.greenAccent[500] }}
          />
        </IconButton>
      </Box>
    </Box>
  );
}

'use client'

import useSWR from 'swr'
import { Box } from '@mui/material'
import { DataGrid, GridColDef, GridToolbar } from '@mui/x-data-grid'

import { Header } from '@/components/header'
import { ManageAPI } from '@/api/manage'

export default function TemperaturesInfo() {
    // Use ManageAPI.fetchTemperature method instead of constructing the URL manually
    const { data: fetchedTemperatureData, error } = useSWR(
        ['temperatureData', 1], // Key and sensor-id
        ([_, sensorId]: [any, number]) => ManageAPI.fetchTemperature(sensorId) // Destructure and pass sensorId
    )

    // Handle loading and error states
    if (!fetchedTemperatureData && !error) return <p>Loading...</p>
    if (error) return <p>Error loading data</p>

    // Ensure the data is in the expected format
    const temperatureData = Array.isArray(fetchedTemperatureData) ? fetchedTemperatureData : []

    const columns: GridColDef[] = [
        {
            field: 'date_time',
            headerName: 'Date Time',
            width: 180, // Set a width for the column
        },
        {
            field: 'sensor_name',
            headerName: 'Sensor Name',
            width: 180, // Set a width for the column
        },
        {
            field: 'location',
            headerName: 'Location',
            width: 180, // Set a width for the column
        },
        {
            field: 'temperature',
            headerName: 'Temperature',
            width: 180, // Set a width for the column
            valueFormatter: ({ value }: { value: number }) => {
                if (value == null) {
                    return ''
                }
                return `${value.toLocaleString()} ${String.fromCharCode(176)} C`
            },
        },
    ]

    return (
        <Box m="20px">
            <Header
                title="Temperatures"
                subtitle="List of temperatures information"
            />

            <Box
                m="40px 0 0 0"
                height="72vh"
                sx={{
                    '& .MuiDataGrid-columnHeadersInner': {
                        '& > div': {
                            width: '100%',
                        },
                        width: '100%',
                    },
                    '& .MuiDataGrid-virtualScroller': {
                        scrollbarWidth: 'none' /* Firefox */,
                        '&::-webkit-scrollbar': {
                            display: 'none',
                        },
                    },
                    '& .MuiDataGrid-virtualScrollerRenderZone': {
                        width: '100%',
                        '& > div': {
                            width: '100%',
                        },
                    },
                    '& .MuiDataGrid-toolbarContainer': {
                        paddingLeft: '20px',
                        paddingTop: '20px',
                        paddingBottom: '10px',
                    },
                    '& .MuiDataGrid-columnHeader': {
                        paddingLeft: '25px !important',
                        paddingRight: '25px !important',
                        minWidth: '25% !important',
                    },
                    '& .MuiDataGrid-cell': {
                        minWidth: '25% !important',
                        paddingLeft: '25px !important',
                        paddingRight: '25px !important',
                    },
                }}
            >
                <DataGrid
                    rows={temperatureData} // Ensure temperatureData is in the correct format
                    columns={columns}
                    components={{ Toolbar: GridToolbar }}
                    getRowId={(row) => row.id} // Ensure each row has a unique 'id' field
                />
            </Box>
        </Box>
    )
}

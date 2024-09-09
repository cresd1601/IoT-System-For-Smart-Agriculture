'use client'

import useSWR from 'swr'
import { Box } from '@mui/material'
import { DataGrid, GridColDef, GridToolbar } from '@mui/x-data-grid'

import { Header } from '@/components/header'
import { ManageAPI } from '@/api/manage'

export default function MoistureInfo() {
    // Use manageAPI.fetchMoisture method instead of constructing the URL manually
    const { data: fetchedMoistureData, error } = useSWR(
        ['moistureData', 2], // Key and sensor-id
        ([_, sensorId]: [any, number]) => ManageAPI.fetchMoisture(sensorId) // Destructure and pass sensorId
    )

    // Handle loading and error states
    if (!fetchedMoistureData && !error) return <p>Loading...</p>
    if (error) return <p>Error loading data</p>

    // Ensure the data is in the expected format
    const moistureData = Array.isArray(fetchedMoistureData) ? fetchedMoistureData : []

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
            field: 'moisture',
            headerName: 'Moisture',
            width: 180, // Set a width for the column
            valueFormatter: ({ value }: { value: number }) => {
                if (value == null) {
                    return ''
                }
                return `${value.toLocaleString()} %`
            },
        },
    ]

    return (
        <Box m="20px">
            <Header title="Moisture" subtitle="List of moisture information" />

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
                    rows={moistureData}
                    columns={columns}
                    components={{ Toolbar: GridToolbar }}
                />
            </Box>
        </Box>
    )
}

'use client'

import useSWR from 'swr'
import {Box} from '@mui/material'
import {DataGrid, GridColDef, GridToolbar} from '@mui/x-data-grid'

import {Header} from '@/components/header'
import {ENDPOINT, SERVER_BASE_URL} from "@/utils/constant";
import {fetcher} from "@/api/setting";

export default function HumidityInfo() {
    const {data: fetchedHumidityData} = useSWR<FormValues>(
        `${SERVER_BASE_URL}/${ENDPOINT.HUMIDITY}?sensor-id=1`,
        fetcher,
    )

    // Use fetchedTemperatureData or fallback to initialValues
    const humidityData = fetchedHumidityData || []

    const columns: GridColDef[] = [
        {
            field: 'date_time',
            headerName: 'Date Time',
        },
        {
            field: 'sensor_name',
            headerName: 'Sensor Name',
        },
        {
            field: 'location',
            headerName: 'Location',
        },
        {
            field: 'humidity',
            headerName: 'Humidity',
            valueFormatter: ({value}: { value: number }) => {
                if (value == null) {
                    return ''
                }
                return `${value.toLocaleString()} %`
            },
        },
    ]

    return (
        <Box m="20px">
            <Header title="Humidity" subtitle="List of humidity information"/>
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

                        // Hide scrollbar for Chrome, Safari, and other browsers
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
                        paddingLeft: '20px', // Change the left padding here
                        paddingTop: '20px', // You can also adjust the right padding
                        paddingBottom: '10px', // You can also adjust the right padding
                    },
                    '& .MuiDataGrid-columnHeader': {
                        paddingLeft: '25px !important', // Change the left padding here
                        paddingRight: '25px !important', // You can also adjust the right padding
                        minWidth: '25% !important',
                    },
                    '& .MuiDataGrid-cell': {
                        minWidth: '25% !important',
                        paddingLeft: '25px !important', // Change the left padding here
                        paddingRight: '25px !important', // You can also adjust the right padding
                    },
                }}
            >
                <DataGrid
                    rows={humidityData}
                    columns={columns}
                    components={{Toolbar: GridToolbar}}
                />
            </Box>
        </Box>
    )
}

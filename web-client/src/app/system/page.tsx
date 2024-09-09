'use client'

import {Box, Button, FormControl, InputLabel, MenuItem, Typography, useTheme} from '@mui/material'
import useMediaQuery from '@mui/material/useMediaQuery'
import Slider from '@mui/material/Slider'
import {Formik, FormikHelpers} from 'formik'
import {toast, ToastContainer} from 'react-toastify'
import Select, {SelectChangeEvent} from '@mui/material/Select'
import {useState} from 'react'

import {tokens} from '@/styles/theme'
import {Header} from '@/components/header'
import {fetcher, SettingAPI} from '@/api/setting'
import useSWR from 'swr'
import {ENDPOINT, SERVER_BASE_URL} from '@/utils/constant'

import 'react-toastify/dist/ReactToastify.css'

interface FormValues {
    max_temperature: number
    min_temperature: number
    max_humidity: number
    min_humidity: number
    max_moisture: number
    min_moisture: number
}

const initialValues: FormValues = {
    max_temperature: 0,
    min_temperature: 0,
    max_humidity: 0,
    min_humidity: 0,
    max_moisture: 0,
    min_moisture: 0,
}

const Setting = () => {
    const [sensorId, setSensorId] = useState<number>(1);

    const {data: fetchedSensors} = useSWR<ISensor[]>(
        `${SERVER_BASE_URL}/${ENDPOINT.SENSORS}`,
        fetcher,
    )

    const {data: fetchedSetting} = useSWR<FormValues>(
        `${SERVER_BASE_URL}/${ENDPOINT.SETTING}/${sensorId}`,
        fetcher,
    )

    const handleChange = (event: SelectChangeEvent<number>) => {
        setSensorId(event.target.value as number);
    }

    // Use fetchedSetting or fallback to initialValues
    const settingValues: FormValues = fetchedSetting || initialValues

    const handleSubmit = async (
        values: FormValues,
        formikHelpers: FormikHelpers<FormValues>,
    ) => {
        try {
            const res = await SettingAPI.saveSetting({
                sensor_id: sensorId,
                ...values,
            })

            if (res.statusText === 'OK') {
                toast('You have saved successfully!')
            } else {
                const result = await SettingAPI.createSetting({
                    sensor_id: sensorId,
                    ...values,
                })
                if (result.statusText === 'OK') {
                    toast('You have created successfully!')
                } else {
                    toast('You have failed to save!')
                }
            }
        } catch (error) {
            console.error('Error saving settings:', error)
            toast('An error occurred while saving settings.')
        } finally {
            formikHelpers.setSubmitting(false)
        }
    }

    const isNonMobile = useMediaQuery('(min-width:600px)')
    const theme = useTheme()
    const colors = tokens(theme.palette.mode)

    const sensorSettings = {
        1: {
            options: [
                {
                    name: "temperature"
                },
                {
                    name: "humidity"
                },
            ]
        },
        2: {
            options: [
                {
                    name: "moisture"
                },
            ]
        }
    }

    return (
        <Box m="20px">
            <Box display="flex" sx={{justifyContent: 'space-between'}}>
                <Header title="Setting" subtitle="Save your setting"/>
                <FormControl variant="standard" sx={{m: 1, minWidth: 150}}>
                    <InputLabel id="sensor-label">Sensor</InputLabel>
                    <Select
                        labelId="sensor-label"
                        id="sensor"
                        value={sensorId}
                        onChange={handleChange}
                        label="Sensor"
                    >
                        {fetchedSensors &&
                            fetchedSensors.map((sensor: ISensor) => (
                                <MenuItem key={sensor.id} value={sensor.id}>
                                    {sensor.name}
                                </MenuItem>
                            ))}
                    </Select>
                </FormControl>
            </Box>
            <Formik
                onSubmit={handleSubmit}
                initialValues={settingValues}
                enableReinitialize
            >
                {({values, handleSubmit, handleChange}) => (
                    <form onSubmit={handleSubmit}>
                        <Box
                            display="grid"
                            gap="30px"
                            gridTemplateColumns="repeat(4, minmax(0, 1fr))"
                            sx={{
                                '& > div': {gridColumn: isNonMobile ? 'span 12' : 'span 4'},
                            }}
                        >
                            {sensorSettings[sensorId]?.options.map(option => (
                                <Box key={option.name}>
                                    <Typography
                                        variant="h2"
                                        fontWeight="600"
                                        color={colors.grey[100]}
                                        marginBottom="25px"
                                    >
                                        {option.name.charAt(0).toUpperCase() + option.name.slice(1)}
                                    </Typography>
                                    <Typography
                                        variant="h5"
                                        fontWeight="600"
                                        color={colors.grey[100]}
                                    >
                                        Minimum
                                    </Typography>
                                    <Slider
                                        name={`min_${option.name}`}
                                        onChange={handleChange}
                                        value={values[`min_${option.name}`]}
                                        aria-label="Default"
                                        valueLabelDisplay="auto"
                                    />
                                    <Typography
                                        variant="h5"
                                        fontWeight="600"
                                        color={colors.grey[100]}
                                    >
                                        Maximum
                                    </Typography>
                                    <Slider
                                        name={`max_${option.name}`}
                                        onChange={handleChange}
                                        value={values[`max_${option.name}`]}
                                        aria-label="Default"
                                        valueLabelDisplay="auto"
                                    />
                                </Box>
                            ))}
                        </Box>
                        <Box display="flex" justifyContent="end" mt="20px">
                            <Button type="submit" color="secondary" variant="contained">
                                Save
                            </Button>
                        </Box>
                    </form>
                )}
            </Formik>
            <ToastContainer/>
        </Box>
    )
}

export default Setting

import axios from 'axios'
import { SERVER_BASE_URL, ENDPOINT } from '@/utils/constant'

// Define the initial values for your form
const initialValues = {
  sensor_id: 0,
  max_temperature: 0,
  min_temperature: 0,
  max_humidity: 0,
  min_humidity: 0,
  max_moisture: 0,
  min_moisture: 0,
}

interface SettingValues {
  sensor_id: number
  max_temperature: number
  min_temperature: number
  max_humidity: number
  min_humidity: number
  max_moisture: number
  min_moisture: number
}

export interface ApiResponse {
  status: number
  data: SettingValues
}

// Setting API to interact with the settings endpoint
export const SettingAPI = {
  fetcher: async (url: string) => {
    try {
      const { data } = await axios.get(url)
      return data
    } catch (error) {
      console.error('Error fetching data:', error)
      return null
    }
  },

  fetchSetting: async (sensorId: number): Promise<ApiResponse> => {
    try {
      const { data }  = await axios.get(
          `${SERVER_BASE_URL}/${ENDPOINT.SENSORS}/${sensorId}/${ENDPOINT.SETTING_DETAIL}`
      )
      return data
    } catch (error) {
      console.error('Error fetching setting:', error)
      return null
    }
  },

  saveSetting: async (data: SettingValues): Promise<ApiResponse> => {
    try {
      const response = await axios.put(
          `${SERVER_BASE_URL}/${ENDPOINT.SENSORS}/${data.sensor_id}/${ENDPOINT.SETTING_DETAIL}`,
          data,
          {
            headers: {
              'Content-Type': 'application/json',
            },
          }
      )

      return {
        status: response.status,
        data: response.data,
      }
    } catch (error) {
      console.error('Error saving settings:', error)
      return {
        status: error.response?.status || 500,
        data: initialValues,
      }
    }
  },
}

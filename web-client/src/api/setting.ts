import { ENDPOINT, SERVER_BASE_URL } from '@/utils/constant'
import axios from 'axios'

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
  statusText: string
  data: SettingValues
}

export async function fetcher(url: string) {
  const { data } = await axios.get(url)
  return data
}

export const SettingAPI = {
  createSetting: async (data: SettingValues): Promise<ApiResponse> => {
    try {
      const response: ApiResponse = await axios.post(
        `${SERVER_BASE_URL}/${ENDPOINT.SETTING}`,
        JSON.stringify(data),
        {
          headers: {
            'Content-Type': 'application/json',
          },
        },
      )
      return response
    } catch (error) {
      return {
        statusText: 'Failed',
        data: initialValues,
      }
    }
  },
  saveSetting: async (data: SettingValues): Promise<ApiResponse> => {
    try {
      const response: ApiResponse = await axios.put(
        `${SERVER_BASE_URL}/${ENDPOINT.SETTING}/${data.sensor_id}`,
        JSON.stringify(data),
        {
          headers: {
            'Content-Type': 'application/json',
          },
        },
      )
      return response
    } catch (error) {
      return {
        statusText: 'Failed',
        data: initialValues,
      }
    }
  },
}

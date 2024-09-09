import axios from 'axios'

import { SERVER_BASE_URL, ENDPOINT } from '@/utils/constant'

export const DashboardAPI = {
  // Method to get locations
  getLocations: async () => {
    try {
      const res = await axios.get(`${SERVER_BASE_URL}/${ENDPOINT.LOCATIONS}`)
      return res.data
    } catch (error) {
      console.error('Error fetching locations:', error)
      return null
    }
  },

  // Method to get moisture chart data
  getMoistureChartData: async (sensorId: number) => {
    try {
      const res = await axios.get(
          `${SERVER_BASE_URL}/${ENDPOINT.MOISTURE}/${ENDPOINT.CHART}`,
          {
            params: {
              'sensor-id': sensorId,
            },
            headers: {
              'Accept': 'application/json',
            },
          }
      )
      return {
        status: res.status,
        data: res.data,
      }
    } catch (error) {
      console.error('Error fetching moisture chart data:', error)
      return {
        status: error.response?.status || 500,
        data: null,
      }
    }
  },

  // Method to get temperature chart data
  getTemperatureChartData: async (sensorId: number) => {
    try {
      const res = await axios.get(
          `${SERVER_BASE_URL}/${ENDPOINT.TEMPERATURE}/${ENDPOINT.CHART}`,
          {
            params: {
              'sensor-id': sensorId,
            },
            headers: {
              'Accept': 'application/json',
            },
          }
      )
      return {
        status: res.status,
        data: res.data,
      }
    } catch (error) {
      console.error('Error fetching temperature chart data:', error)
      return {
        status: error.response?.status || 500,
        data: null,
      }
    }
  },

  // Method to get humidity chart data
  getHumidityChartData: async (sensorId: number) => {
    try {
      const res = await axios.get(
          `${SERVER_BASE_URL}/${ENDPOINT.HUMIDITY}/${ENDPOINT.CHART}`,
          {
            params: {
              'sensor-id': sensorId,
            },
            headers: {
              'Accept': 'application/json',
            },
          }
      )
      return {
        status: res.status,
        data: res.data,
      }
    } catch (error) {
      console.error('Error fetching humidity chart data:', error)
      return {
        status: error.response?.status || 500,
        data: null,
      }
    }
  },
}

export default DashboardAPI

import axios from 'axios';
import { ENDPOINT, SERVER_BASE_URL } from '@/utils/constant';

/**
 * ManageAPI object to encapsulate multiple API calls
 */
export const ManageAPI = {
    /**
     * Fetch temperature data
     * @param sensorId - The sensor ID to fetch temperature data for
     * @returns Promise<any> - The response containing temperature data
     */
    async fetchTemperature(sensorId: number): Promise<any> {
        try {
            const response = await axios.get(
                `${SERVER_BASE_URL}/${ENDPOINT.TEMPERATURE}?sensor-id=${sensorId}`
            );
            return response.data;
        } catch (error: any) {
            console.error('Error fetching temperature:', error?.response?.data || error.message);
            throw error?.response?.data || new Error('An error occurred while fetching temperature data.');
        }
    },

    /**
     * Fetch moisture data
     * @param sensorId - The sensor ID to fetch moisture data for
     * @returns Promise<any> - The response containing moisture data
     */
    async fetchMoisture(sensorId: number): Promise<any> {
        try {
            const response = await axios.get(
                `${SERVER_BASE_URL}/${ENDPOINT.MOISTURE}?sensor-id=${sensorId}`
            );
            return response.data;
        } catch (error: any) {
            console.error('Error fetching moisture:', error?.response?.data || error.message);
            throw error?.response?.data || new Error('An error occurred while fetching moisture data.');
        }
    },

    /**
     * Fetch humidity data
     * @param sensorId - The sensor ID to fetch humidity data for
     * @returns Promise<any> - The response containing humidity data
     */
    async fetchHumidity(sensorId: number): Promise<any> {
        try {
            const response = await axios.get(
                `${SERVER_BASE_URL}/${ENDPOINT.HUMIDITY}?sensor-id=${sensorId}`
            );
            return response.data;
        } catch (error: any) {
            console.error('Error fetching humidity:', error?.response?.data || error.message);
            throw error?.response?.data || new Error('An error occurred while fetching humidity data.');
        }
    },
};

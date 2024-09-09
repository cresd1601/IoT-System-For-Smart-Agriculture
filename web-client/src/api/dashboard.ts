import axios from 'axios'

import { SERVER_BASE_URL } from '@/utils/constant'

const DashboardAPI = {
  getLocations: async () => {
    const res = await axios.get(`${SERVER_BASE_URL}/locations`)
    return res.data
  },
  //   register: async (username, email, password) => {
  //     try {
  //       const response = await axios.post(
  //         `${SERVER_BASE_URL}/users`,
  //         JSON.stringify({ user: { username, email, password } }),
  //         {
  //           headers: {
  //             "Content-Type": "application/json",
  //           },
  //         }
  //       );
  //       return response;
  //     } catch (error) {
  //       return error.response;
  //     }
  //   },
  //   save: async (user) => {
  //     try {
  //       const response = await axios.put(
  //         `${SERVER_BASE_URL}/user`,
  //         JSON.stringify({ user }),
  //         {
  //           headers: {
  //             "Content-Type": "application/json",
  //           },
  //         }
  //       );
  //       return response;
  //     } catch (error) {
  //       return error.response;
  //     }
  //   },
  //   follow: async (username) => {
  //     const user: any = JSON.parse(window.localStorage.getItem("user"));
  //     const token = user?.token;
  //     try {
  //       const response = await axios.post(
  //         `${SERVER_BASE_URL}/profiles/${username}/follow`,
  //         {},
  //         {
  //           headers: {
  //             Authorization: `Token ${encodeURIComponent(token)}`,
  //           },
  //         }
  //       );
  //       return response;
  //     } catch (error) {
  //       return error.response;
  //     }
  //   },
}

export default DashboardAPI

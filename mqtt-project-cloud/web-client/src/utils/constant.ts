export const SERVER_BASE_URL = `http://${process.env.NEXT_PUBLIC_CLOUD_SERVICE_IP}:5000/api`;

export const ENDPOINT = {
  TEMPERATURE: 'temperature-data',
  HUMIDITY: 'humidity-data',
  MOISTURE: 'moisture-data',
  LOCATIONS: 'locations',
  SETTING: 'settings',
  SETTING_DETAIL: 'setting',
  SENSORS: 'sensors',
  CHART: 'chart'
};

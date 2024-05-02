import axios from 'axios'

export const api = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_URL
})
api.interceptors.request.use(
  (config) => {
    const authToken = localStorage.getItem('authToken')

    if (authToken) {
      config.headers['Authorization'] = 'Token ' + authToken
    }

    return config
  },
  (error) => {
    Promise.reject(error)
  }
)

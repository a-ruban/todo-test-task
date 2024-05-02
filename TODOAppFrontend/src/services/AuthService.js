import { api } from '@/api.js'

export class AuthService {
  static async performLogin (username, password) {
    const response = await api.post(
      `/auth/login/`,
      {
        username: username,
        password: password
      }
    )
    const authToken = response.data.token
    localStorage.setItem('authToken', authToken)
  }
}

import { api } from '@/api.js'

export class TaskService {
  static async createTask ({ title, content }) {
    const response = await api.post(
      `/tasks/`,
      {
        title: title,
        content: content
      }
    )
  }
  static async getTasks () {
    const response = await api.get(
      `/tasks/`
    )
    return response.data
  }
}

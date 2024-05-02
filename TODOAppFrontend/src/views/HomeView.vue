<template>
  <main class="bg-gray-100">
    <div class="container mx-auto py-8">
      <h1 class="text-3xl font-semibold mb-4">
        Todo App
      </h1>

      <!-- Todo Tasks List -->
      <div class="bg-white rounded-md shadow-md p-4 mb-8">
        <h2 class="text-xl font-semibold mb-4">
          Todo Tasks
        </h2>
        <ul>
          <!-- Sample Todo Tasks -->
          <li
            v-for="task of tasks"
            :key="task.title"
            class="flex justify-between items-center py-2 border-b border-gray-200"
          >
            <div>
              <h3 class="text-lg font-semibold">
                {{ task.title }}
              </h3>
              <p class="text-gray-600">
                {{ task.content }}.
              </p>
            </div>
          </li>
          <!-- End of Sample Todo Tasks -->
        </ul>
      </div>

      <!-- Form to Add Todo Task -->
      <div class="bg-white rounded-md shadow-md p-4">
        <h2 class="text-xl font-semibold mb-4">
          Add Todo Task
        </h2>
        <div>
          <div class="mb-4">
            <label
              for="title"
              class="block text-sm font-medium text-gray-700"
            >Title</label>
            <input
              id="title"
              v-model="newTask.title"
              type="text"
              name="title"
              class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            >
          </div>
          <div class="mb-4">
            <label
              for="content"
              class="block text-sm font-medium text-gray-700"
            >Content</label>
            <textarea
              id="content"
              v-model="newTask.content"
              name="content"
              rows="3"
              class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>
          <button
            class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
            @click="createTask"
          >
            Add Task
          </button>
        </div>
      </div>
    </div>
  </main>
</template>

<script>

import { TaskService } from '@/services/TaskService.js'

export default {
  name: 'HomeView',
  data () {
    return {
      tasks: [],
      newTask: {
        title: '',
        content: ''
      }
    }
  },
  async created () {
    this.tasks = await TaskService.getTasks()
  },
  methods: {
    async createTask () {
      await TaskService.createTask(this.newTask)
      this.tasks.push({ title: this.newTask.title, content: this.newTask.content })
      this.newTask.title = ''
      this.newTask.content = ''
    }
  }
}

</script>

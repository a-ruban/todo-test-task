<template>
  <main class="bg-gray-100 flex items-center justify-center h-screen">
    <div class="max-w-md w-full p-8 bg-white shadow-md rounded-md">
      <h2 class="text-2xl font-semibold mb-6 text-center">
        Login
      </h2>
      <div>
        <div class="mb-4">
          <label
            for="username"
            class="block text-sm font-medium text-gray-700"
          >Username</label>
          <input
            id="username"
            v-model="username"
            type="text"
            name="username"
            class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          >
        </div>
        <div class="mb-6">
          <label
            for="password"
            class="block text-sm font-medium text-gray-700"
          >Password</label>
          <input
            id="password"
            v-model="password"
            type="password"
            name="password"
            class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          >
        </div>
        <div class="flex items-center justify-between">
          <button
            class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
            @click="performLogin"
          >
            Login
          </button>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { AuthService } from '@/services/AuthService.js'

export default {
  name: 'LoginView',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  async created () {},
  methods: {
    async performLogin () {
      await AuthService.performLogin(this.username, this.password)
      this.$router.push({ name: 'home' })
    }
  }
}

</script>

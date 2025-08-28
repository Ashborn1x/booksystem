<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="p-6 border rounded-lg shadow-md w-80">
      <h1 class="text-xl font-bold mb-4">Login</h1>
      <form @submit.prevent="login">
        <input
          v-model="username"
          type="text"
          placeholder="Username"
          class="border px-3 py-2 mb-3 w-full rounded"
        />
        <input
          v-model="password"
          type="password"
          placeholder="Password"
          class="border px-3 py-2 mb-4 w-full rounded"
        />
        <button
          type="submit"
          class="bg-blue-600 text-white px-4 py-2 rounded w-full"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password = ref('')

function login() {
  // fake account
  if (username.value === 'admin' && password.value === '1234') {
    router.push('/dashboard')
  } else {
    alert('Invalid credentials')
  }
}
</script>

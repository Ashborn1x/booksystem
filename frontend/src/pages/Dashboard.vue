<template>
  <div class="min-h-screen flex flex-col items-center justify-center">
    <h1 class="text-2xl font-bold mb-6">Dashboard</h1>
    <button
      @click="logout"
      class="bg-red-600 text-white px-4 py-2 rounded"
    >
      Logout
    </button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

function logout() {
  router.push('/login')
}
</script>

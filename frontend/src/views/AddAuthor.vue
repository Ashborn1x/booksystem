<template>
  <div class="p-6 max-w-md mx-auto">
    <h1 class="text-2xl font-bold mb-4">Add New Author</h1>

    <form @submit.prevent="addAuthor" class="space-y-4">
      <div>
        <label class="block mb-1 font-medium">Author Name</label>
        <input
          v-model="name"
          type="text"
          placeholder="Enter author name"
          class="w-full border rounded px-3 py-2"
        />
      </div>

      <button
        type="submit"
        class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Save Author
      </button>
    </form>

    <p v-if="message" class="mt-4 text-green-600">{{ message }}</p>
    <p v-if="error" class="mt-4 text-red-600">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const name = ref('')
const message = ref('')
const error = ref('')

async function addAuthor() {
  try {
    const res = await axios.post('http://127.0.0.1:5000/authors', {
      name: name.value
    })
    message.value = res.data.message
    error.value = ''
    name.value = '' // clear field after success
  } catch (err) {
    error.value = err.response?.data?.error || "Something went wrong"
    message.value = ''
  }
}
</script>

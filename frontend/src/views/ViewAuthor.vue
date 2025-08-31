<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow">
    <h2 class="text-2xl font-bold mb-4">Author Details</h2>
    <router-link
      :to="{ path: '/add-book', query: { author_id: author.id } }"
      class="block px-4 py-2 hover:bg-gray-200"
    >
      ➕ Book
    </router-link>

    <div v-if="loading">Loading author...</div>
    <div v-else-if="error" class="text-red-500">{{ error }}</div>
    <div v-else>
      <p><span class="font-semibold">ID:</span> {{ author.id }}</p>
      <p><span class="font-semibold">Name:</span> {{ author.name }}</p>
      <p><span class="font-semibold">Books:</span></p>
        <ul v-if="author.books.length" class="list-disc list-inside">
        <li v-for="book in author.books" :key="book.id">
            {{ book.title }}
            <router-link
            :to="{ path: `/update-book/${book.id}`, query: { title: book.title } }"
            class="ml-2 inline-block bg-blue-500 text-white px-2 py-1 rounded hover:bg-blue-600 text-sm"
            >
            Update
            </router-link>
        </li>
        </ul>
        <p v-else class="text-gray-500 italic">No books available</p>
    </div>

    <router-link
      to="/dashboard"
      class="mt-4 inline-block bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
    >
      Back to Authors
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import axios from "axios"

const route = useRoute()
const author = ref({
  id: null,
  name: "",
  books: []
})
const loading = ref(true)
const error = ref("")

onMounted(async () => {
  try {
    const res = await axios.get(`http://127.0.0.1:5000/authors/${route.params.id}`)
    author.value = res.data.author
  } catch (err) {
    error.value = "Failed to load author."
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>

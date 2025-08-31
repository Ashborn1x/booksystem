<template>
  <div class="p-6 max-w-2xl mx-auto">
    <div v-if="loading" class="text-gray-500">Loading genre...</div>

    <div v-else-if="genre">
      <h1 class="text-2xl font-bold mb-4">Genre: {{ genre.genre }}</h1>
      <p class="mb-4 text-gray-600">ID: {{ genre.id }}</p>

      <h2 class="text-xl font-semibold mb-2">Books under this Genre:</h2>
      <ul v-if="genre.books.length > 0" class="list-disc list-inside">
        <li v-for="(book, index) in genre.books" :key="index">
          {{ book }}
        </li>
      </ul>
      <p v-else class="text-gray-500">No books in this genre yet.</p>

      <router-link
        to="/genre-list"
        class="inline-block mt-6 text-blue-600 hover:underline"
      >
        ← Back to Genre List
      </router-link>
    </div>

    <div v-else class="text-red-500">Failed to load genre.</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import axios from "axios"

const route = useRoute()
const genre = ref(null)
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await axios.get(`http://127.0.0.1:5000/genres/${route.params.id}`)
    genre.value = res.data.genre
  } catch (error) {
    console.error("Error fetching genre:", error)
  } finally {
    loading.value = false
  }
})
</script>

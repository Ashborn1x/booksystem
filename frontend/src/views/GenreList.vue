<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-6">Books List</h1>

    <router-link to="/add-author" class="block px-4 py-2 hover:bg-gray-200">
      ➕ Add Author
    </router-link><br>
    <router-link to="/genre-list" class="block px-4 py-2 hover:bg-gray-200">
      Genre List
    </router-link>
    <div v-if="loading">Loading Genre...</div>
    <div v-else>
      <table class="w-full border-collapse border border-gray-300">
        <thead>
          <tr class="bg-gray-100">
            <th class="border border-gray-300 px-4 py-2">ID</th>
            <th class="border border-gray-300 px-4 py-2">Genre</th>
            <th class="border border-gray-300 px-4 py-2">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="genre in genres" :key="genre.id">
            <td class="border border-gray-300 px-4 py-2">{{ genre.id }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ genre.genre }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"

const genres = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await axios.get("http://127.0.0.1:5000/genres")
    genres.value = res.data
  } catch (error) {
    console.error("Error fetching genre:", error)
  } finally {
    loading.value = false
  }
})
</script>

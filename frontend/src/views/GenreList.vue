<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-6">Books List</h1>

    <router-link to="/add-genre" class="block px-4 py-2 hover:bg-gray-200">
      ➕ Add Genre
    </router-link><br>
    <router-link to="/dashboard" class="block px-4 py-2 hover:bg-gray-200">
      Dashboard
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
            <td class="border border-gray-300 px-4 py-2">
              <router-link :to="`/view-genre/${genre.id}`">View</router-link>
              <router-link :to="`/update-genre/${genre.id}`">Update</router-link>
              <button
                @click="deleteGenre(genre.id)"
                class="ml-2 inline-block bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600 text-sm"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <p v-if="message" class="mt-4 text-green-600">{{ message }}</p>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"

const genres = ref([])
const loading = ref(true)
const message = ref("")

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
async function deleteGenre(genreId) {
  if (!confirm("Are you sure you want to delete this author?")) return;

  try {
    await axios.delete(`http://127.0.0.1:5000/genres/${genreId}`)
    genres.value = genres.value.filter(g => g.id !== genreId)
    message.value = "Genre deleted successfully!"
  } catch (err) {
    console.error("Failed to delete genre:", err)
    alert("Error deleting Genre.")
  }
}
</script>

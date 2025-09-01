<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow">
    <h2 class="text-xl font-bold mb-4">Update Genre</h2>

    <form @submit.prevent="updateGenre">
      <div class="mb-4">
        <label class="block mb-1 font-medium">Genre ID</label>
        <input
          v-model="genreId"
          type="number"
          class="w-full border rounded px-3 py-2"
          readonly
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">Genre</label>
        <input
          v-model="form.genre"
          type="text"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>

      <button
        type="submit"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Update Genre
      </button>
    </form>

    <p v-if="message" class="mt-4 text-green-600">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import axios from "axios"

const route = useRoute()
const genreId = ref(route.params.id)

const form = ref({
  genre: ""
})
const message = ref("")

async function loadGenre() {
  try {
    const res = await axios.get(`http://127.0.0.1:5000/genres/${genreId.value}`)
    form.value.genre = res.data.genre.genre
  } catch (err) {
    console.error("Failed to load genre:", err)
  }
}

async function updateGenre() {
  try {
    const res = await axios.put(
      `http://127.0.0.1:5000/genres/${genreId.value}`,
      form.value
    )
    message.value = res.data.message
  } catch (err) {
    console.error("Failed to update genre:", err)
    message.value = "Error updating genre."
  }
}

onMounted(() => {
  loadGenre()
})
</script>

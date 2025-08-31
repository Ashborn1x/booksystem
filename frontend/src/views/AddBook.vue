<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow">
    <h2 class="text-2xl font-bold mb-4">Add Book</h2>

    <form @submit.prevent="addBook">
      <!-- Title -->
      <div class="mb-4">
        <label class="block mb-1 font-medium">Title</label>
        <input
          v-model="form.title"
          type="text"
          class="w-full border rounded px-3 py-2"
          placeholder="Enter book title"
          required
        />
      </div>

      <!-- Genre -->
      <div class="mb-4">
        <label class="block mb-1 font-medium">Genre</label>
        <select
          v-model="form.genre_id"
          class="w-full border rounded px-3 py-2"
          required
        >
          <option disabled value="">Select a genre</option>
          <option
            v-for="genre in genres"
            :key="genre.id"
            :value="genre.id"
          >
            {{ genre.genre }}
          </option>
        </select>
      </div>

      <!-- Submit -->
      <button
        type="submit"
        class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
      >
        Save Book
      </button>
    </form>

    <!-- Back -->
    <router-link
      :to="`/view-author/${route.query.author_id}`"
      class="mt-4 inline-block text-blue-500 hover:underline"
    >
      ← Back to Author
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import axios from "axios"

const route = useRoute()
const router = useRouter()

const form = ref({
  title: "",
  author_id: "",
  genre_id: ""
})

const genres = ref([])

onMounted(async () => {
  try {
    const res = await axios.get("http://127.0.0.1:5000/genres")
    genres.value = res.data.genres || res.data || []

    if (route.query.author_id) {
      form.value.author_id = parseInt(route.query.author_id)
    }
  } catch (err) {
    console.error("Failed to load genres:", err)
  }
})

const addBook = async () => {
  try {
    await axios.post("http://127.0.0.1:5000/books", form.value)

    // Always go back to the author's page after saving
    router.push(`/view-author/${route.query.author_id}`)
  } catch (err) {
    console.error("Failed to add book:", err)
  }
}
</script>

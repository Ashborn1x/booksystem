<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow">
    <h2 class="text-xl font-bold mb-4">Update Book</h2>

    <form @submit.prevent="updateBook">
      <div class="mb-4">
        <label class="block mb-1 font-medium">Book ID</label>
        <input
          v-model="bookId"
          type="number"
          class="w-full border rounded px-3 py-2"
          readonly
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">Title</label>
        <input
          v-model="form.title"
          type="text"
          class="w-full border rounded px-3 py-2"
        />
      </div>

      <!-- Genre -->
      <div class="mb-4">
        <label class="block mb-1 font-medium">Genre</label>
        <select
          v-model="form.genre_id"
          class="w-full border rounded px-3 py-2"
        >
          <option disabled value="">-- Select Genre --</option>
          <option v-for="g in genres" :key="g.id" :value="g.id">
            {{ g.genre }}
          </option>
        </select>
      </div>

      <button
        type="submit"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Update Book
      </button>
    </form>

    <p v-if="message" class="mt-4 text-green-600">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"

const route = useRoute()
const bookId = ref(route.params.id)

const form = ref({
  title: route.query.title || "",
  genre_id: route.query.genre_id || "",
  author_id: route.query.author_id || ""
})
const genres = ref([])
const message = ref("")

// Fetch book details
async function loadBook() {
  try {
    const res = await fetch(`http://127.0.0.1:5000/books/${bookId.value}`)
    const data = await res.json()

    // Only update if not already set from route query
    if (!form.value.title) {
      form.value.title = data.title
    }
    if (!form.value.author_id) {
      form.value.author_id = data.author_id
    }
    if (!form.value.genre_id) {
      form.value.genre_id = data.book.genre_id
    }
  } catch (err) {
    console.error("Failed to load book:", err)
  }
}

// Fetch genres
async function loadGenres() {
  try {
    const res = await fetch("http://127.0.0.1:5000/genres")
    genres.value = await res.json()
  } catch (err) {
    console.error("Failed to load genres:", err)
  }
}

// Update book
async function updateBook() {
  try {
    const response = await fetch(`http://127.0.0.1:5000/books/${bookId.value}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form.value)
    })

    const data = await response.json()
    if (response.ok) {
      message.value = data.message
    } else {
      message.value = data.error || "Failed to update book."
    }
  } catch (err) {
    message.value = "Server error."
  }
}

onMounted(async () => {
  // Load genres first, then book details to ensure genres are available when genre_id is set
  await loadGenres()
  await loadBook()
})
</script>
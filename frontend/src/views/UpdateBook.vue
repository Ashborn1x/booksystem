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
          required
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

      <div class="mb-4">
        <label class="block mb-1 font-medium">Author ID</label>
        <input
          v-model="form.author_id"
          type="number"
          class="w-full border rounded px-3 py-2"
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">Genre ID</label>
        <input
          v-model="form.genre_id"
          type="number"
          class="w-full border rounded px-3 py-2"
        />
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
const bookId = ref(route.params.id) // <-- get book id from URL
const form = ref({
  title: route.query.title || "",   // prefill from query
  author_id: "",
  genre_id: ""
})
const message = ref("")

// Load existing book data for prefill
onMounted(async () => {
  try {
    const res = await fetch(`http://127.0.0.1:5000/books/${bookId.value}`)
    const data = await res.json()
    // if no title from query, fall back to API response
    if (!form.value.title) {
      form.value.title = data.title
    }
    form.value.author_id = data.author_id
    form.value.genre_id = data.genre_id
  } catch (err) {
    console.error("Failed to load book:", err)
  }
})

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
</script>

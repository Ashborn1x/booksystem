<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow">
    <h2 class="text-xl font-bold mb-4">Add a New Book</h2>

    <form @submit.prevent="addBook">
      <div class="mb-4">
        <label class="block mb-1 font-medium">Title</label>
        <input
          v-model="form.title"
          type="text"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">Author ID</label>
        <input
          v-model="form.author_id"
          type="number"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">Genre ID</label>
        <input
          v-model="form.genre_id"
          type="number"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>

      <button
        type="submit"
        class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
      >
        Save Book
      </button>
    </form>

    <p v-if="message" class="mt-4 text-green-600">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue"

const form = ref({
  title: "",
  author_id: "",
  genre_id: ""
})

const message = ref("")

async function addBook() {
  try {
    const response = await fetch("http://127.0.0.1:5000/books", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form.value)
    })

    const data = await response.json()
    if (response.ok) {
      message.value = data.message
      form.value = { title: "", author_id: "", genre_id: "" } // reset form
    } else {
      message.value = data.error || "Failed to add book."
    }
  } catch (err) {
    message.value = "Server error."
  }
}
</script>

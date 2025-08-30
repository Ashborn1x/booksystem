<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-6">Books List</h1>

    <router-link to="/add-author" class="block px-4 py-2 hover:bg-gray-200">
      ➕ Add Author
    </router-link>

    <div v-if="loading">Loading books...</div>
    <div v-else>
      <table class="w-full border-collapse border border-gray-300">
        <thead>
          <tr class="bg-gray-100">
            <th class="border border-gray-300 px-4 py-2">ID</th>
            <th class="border border-gray-300 px-4 py-2">Title</th>
            <th class="border border-gray-300 px-4 py-2">Author</th>
            <th class="border border-gray-300 px-4 py-2">Genre</th>
            <th class="border border-gray-300 px-4 py-2">Description</th>
            <th class="border border-gray-300 px-4 py-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="book in books" :key="book.id">
            <td class="border border-gray-300 px-4 py-2">{{ book.id }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ book.title }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ book.author }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ book.genre }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ book.description }}</td>
            <td class="border border-gray-300 px-4 py-2">
              <router-link
                :to="{
                  path: `/update-book/${book.id}`,
                  query: { title: book.title, author_id: book.author_id, genre_id: book.genre_id }
                }"
              >
                Update
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"

const books = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await axios.get("http://127.0.0.1:5000/books")
    books.value = res.data
  } catch (error) {
    console.error("Error fetching books:", error)
  } finally {
    loading.value = false
  }
})
</script>

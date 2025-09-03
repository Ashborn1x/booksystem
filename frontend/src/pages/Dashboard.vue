<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-6">Author List</h1>

    <router-link to="/add-author" class="block px-4 py-2 hover:bg-gray-200">
      ➕ Add Author
    </router-link><br>
    <router-link to="/genre-list" class="block px-4 py-2 hover:bg-gray-200">
      Genre List
    </router-link>
    <div v-if="loading">Loading Authors...</div>
    <div v-else>
      <table class="w-full border-collapse border border-gray-300">
        <thead>
          <tr class="bg-gray-100">
            <th class="border border-gray-300 px-4 py-2">ID</th>
            <th class="border border-gray-300 px-4 py-2">Author</th>
            <th class="border border-gray-300 px-4 py-2">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="author in authors" :key="author.id">
            <td class="border border-gray-300 px-4 py-2">{{ author.id }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ author.name }}</td>
            <td class="border border-gray-300 px-4 py-2">
              <router-link :to="`/view-author/${author.id}`">View</router-link>
              <router-link :to="`/update-author/${author.id}`">Update</router-link>
              <button
                @click="deleteAuthor(author.id)"
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

const authors = ref([])
const loading = ref(true)
const message = ref("")

onMounted(async () => {
  try {
    const res = await axios.get("http://127.0.0.1:5000/authors")
    authors.value = res.data
  } catch (error) {
    console.error("Error fetching author:", error)
  } finally {
    loading.value = false
  }
})
async function deleteAuthor(authorId) {
  if (!confirm("Are you sure you want to delete this author?")) return;

  try {
    await axios.delete(`http://127.0.0.1:5000/authors/${authorId}`)
    authors.value = authors.value.filter(a => a.id !== authorId)
    message.value = "Author deleted successfully!"
  } catch (err) {
    console.error("Failed to delete author:", err)
    alert("Error deleting Author.")
  }
}


</script>

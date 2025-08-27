<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const authors = ref([])

onMounted(async () => {
  const res = await axios.get('http://127.0.0.1:5000/authors')
  authors.value = res.data
})
</script>

<template>
  <div>
    <h1>Authors</h1>
    <ul>
      <li v-for="a in authors" :key="a.id">
        {{ a.name }}
      </li>
    </ul>
  </div>
</template>

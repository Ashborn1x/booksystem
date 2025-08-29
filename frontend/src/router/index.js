import { createRouter, createWebHistory } from 'vue-router'

// pages
import Login from '../pages/Login.vue'
import Dashboard from '../pages/Dashboard.vue'
import AddAuthor from '../views/AddAuthor.vue'
import AddBook from '../views/AddBook.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/add-author', component: AddAuthor },
  { path: '/add-book', component: AddBook },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

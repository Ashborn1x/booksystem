import { createRouter, createWebHistory } from 'vue-router'

// pages
import Login from '../pages/Login.vue'
import Dashboard from '../pages/Dashboard.vue'
// Author
import AddAuthor from '../views/AddAuthor.vue'
import ViewAuthor from '../views/ViewAuthor.vue'
import UpdateAuthor from '../views/UpdateAuthor.vue'
// Book
import AddBook from '../views/AddBook.vue'
import UpdateBook from '../views/UpdateBook.vue'
// Genre - TBA
import GenreList from '../views/GenreList.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/add-author', component: AddAuthor },
  { path: '/view-author/:id', component: ViewAuthor, props: true },
  { path: '/update-author/:id', component: UpdateAuthor, props: true },
  { path: '/add-book', component: AddBook },
  { path: '/update-book/:id', component: UpdateBook, props: true },
  { path: '/genre-list', component: GenreList },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

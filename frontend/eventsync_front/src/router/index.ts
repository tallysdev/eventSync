import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import SponsorsView from '@/views/SponsorsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create-event',
      name: 'create-event',
      component: () => import('../views/CreateEventPage.vue')
    },
    {
      path: '/create-form',
      name: 'create-form',
      component: () => import('../views/CreateForm.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/events/:id/theme-room',
      name: 'theme-room',
      component: () => import('../views/ThemeRoomView.vue')
    }
  ]
})

export default router

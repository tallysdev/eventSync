import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SponsorsView from '@/views/SponsorsView.vue'
import EventListView from '@/views/EventListView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import { useAuthStore } from '@/stores/auth'
import EventsOrgView from '@/views/EventsOrgView.vue'
import EventsParticipatedView from '@/views/EventsParticipatedView.vue'
import PartcipantView from '@/views/PartcipantView.vue'

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
      component: () => import('../views/EventPageView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/create-form',
      name: 'create-form',
      component: () => import('../views/CreateForm.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/local-form',
      name: 'local-form',
      component: () => import('../views/LocalView.vue'),
      meta: { requiresAuth: true }
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // },
    {
      path: '/sponsors',
      name: 'sponsors',
      component: SponsorsView,
      meta: { requiresAuth: true }
      // para views que sejam privadas usar esse exemplo
      // meta: { requiresAuth: true }
    },
    {
      path: '/events',
      name: 'events',
      component: EventListView
    },
    {
      path: '/events/:id',
      name: 'event-detail',
      component: () => import('../views/EventDetailView.vue')
    },
    {
      path: '/events-organized',
      name: 'events-organized',
      component: EventsOrgView,
      meta: { requiresAuth: true }
    },
    {
      path: '/events-organized/update/:id',
      name: 'event-update',
      component: () => import('../views/EventUpView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/certificates',
      name: 'certificates',
      component: EventsParticipatedView,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/participants/:id',
      name: 'participants',
      component: PartcipantView,
      meta: { requiresAuth: true }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      redirect: { name: 'home' }
    }
  ]
})

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore() // Obtenha a instância do store de autenticação

  await authStore.checkAuth() // Verifique a autenticação do usuário antes de continuar

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    // Se a rota requer autenticação e o usuário não está autenticado,
    // redirecione para a página de login
    next({ name: 'login' })
  } else if (to.name === 'admin' && !authStore.hasAdminPerm) {
    // Se a rota é a página de admin e o usuário não tem permissões de admin,
    // redirecione para a página inicial ou exiba uma mensagem de erro
    console.error('Usuário não tem permissão de administrador.')
    // Você pode redirecionar para a página inicial assim:
    next({ name: 'home' })
    // Ou mostrar uma mensagem de erro e redirecionar para uma página relevante:
    // next(false) // Isso impede a navegação para a página de admin
  } else {
    // Caso contrário, permita o acesso à rota
    next()
  }
})

export default router

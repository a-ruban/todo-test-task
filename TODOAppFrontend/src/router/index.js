import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      requiredAuth: true
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    }
  ]
})

router.beforeEach((to, from, next) => {
  const requiredAuth = to.matched.some(record => record.meta.requiredAuth)
  const isLoggedIn = localStorage.getItem('authToken')

  if (requiredAuth && !isLoggedIn) {
    next('/login')
    nextTick(() => {
      alert('Please, log in to continue.')
    })
  } else {
    next()
  }
})

export default router

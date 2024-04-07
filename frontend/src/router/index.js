import { createRouter, createWebHistory } from 'vue-router'
import GaragemView from '../views/GaragemView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: GaragemView
    },
    {
      path: '/categoria',
      name: 'categoria',
      component: () => import('../views/CategoriaView.vue')
    },
    {
      path: '/marca',
      name: 'marca',
      component: () => import('../views/MarcaView.vue')
    },
    {
      path: '/cor',
      name: 'cor',
      component: () => import('../views/CorView.vue')
    },
    {
      path: '/acessorio',
      name: 'acessorio',
      component: () => import('../views/AcessoriosView.vue')
    },
    {
      path: '/veiculo',
      name: 'veiculo',
      component: () => import('../views/VeiculoView.vue')
    },
    {
      path: '/auth',
      name: 'auth',
      component: () => import('../views/AuthView.vue')
    }
  ]
})

export default router

import {createRouter, createWebHistory} from "vue-router"

export const routers = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'first', component: () => import('@/views/FirstPage.vue') },
    { path: '/second', name: 'second', component: () => import('@/views/SecondPage.vue') },
    { path: '/finish', name: 'finish', component: () => import('@/views/FinishPage.vue') }
  ],
})
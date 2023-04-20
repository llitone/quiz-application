import { createRouter, createWebHistory } from 'vue-router'
import allPosts from '@/components/allPosts.vue'
// import userPost from '@/components/userPost.vue'
// import newUser from '@/components/newUser.vue'
import loginUser from '@/components/loginUser.vue'
import newQuestion from '@/components/newPost.vue'

const routes = [
  {
    path: '/',
    redirect: {
      name: "log"
    }
  },
  {
    path: '/posts',
    name: 'all',
    component: allPosts
  },
  {
    name: 'log',
    path: '/login',
    component: loginUser
  },
  {
    path: '/new',
    component: newQuestion
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

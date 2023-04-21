import { createRouter, createWebHistory } from 'vue-router'
import allPosts from '@/components/allPosts.vue'
// import userPost from '@/components/userPost.vue'
import newUser from '@/components/newSbj.vue'
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
    path: '/admin',
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
  },
  {
    path: '/newsbj',
    component: newUser
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

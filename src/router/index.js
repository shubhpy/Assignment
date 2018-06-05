import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import Users from '@/components/Users'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
      {
      path: '/',
      name: 'Dashboard',
      component: Dashboard,
      children: [
        {
          path: '/',
          redirect : "/login",
          },
        {
          path: '/users',
          name: 'Users',
          component: Users
          },
      ]
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '**',
      redirect: '/login'
    }
  ]
})
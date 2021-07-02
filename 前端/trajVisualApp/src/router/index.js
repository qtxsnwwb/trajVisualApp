import Vue from 'vue'
import Router from 'vue-router'

import Main from '../views/Main'
import Login from '../views/Login'

Vue.use(Router);

export default new Router({
	routes: [
		{
			//默认进入主页
			path: '/',
			component: Main,
			meta: {
				isLogin: false
			}
		}, {
			//登录页
			path: '/login',
			component: Login,
			meta: {
				isLogin: false
			}
		}, {
			//主页
			path: '/main',
			component: Main,
			meta: {
				isLogin: false
			}
		}
	]
});
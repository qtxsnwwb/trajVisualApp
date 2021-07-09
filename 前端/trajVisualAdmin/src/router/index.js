import Vue from 'vue'
import Router from 'vue-router'

import Login from '../views/Login'
import Main from '../views/Main'

Vue.use(Router);

export default new Router({
	routes: [
		{
			//默认进入登录页
			path: '/',
			component: Login,
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
				isLogin: true
			}
		}
	]
});


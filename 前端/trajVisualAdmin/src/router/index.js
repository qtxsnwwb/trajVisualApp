import Vue from 'vue'
import Router from 'vue-router'

import Login from '../views/Login'
import Main from '../views/Main'
import userManage from '../components/userManage'
import test1 from '../components/test1'

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
			},
			children: [
				{
					//用户信息管理页
					path: '/userManage',
					pathname: 'userManage',
					component: userManage,
					meta: {
						isLogin: true,
					}	
				},
				{
					//测试页1
					path: '/test1',
					pathname: 'test1',
					component: test1,
					meta: {
						isLogin: true
					}
				}
			],
		}
	]
});


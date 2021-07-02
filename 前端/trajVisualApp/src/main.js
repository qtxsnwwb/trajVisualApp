import Vue from 'vue'
import App from './App.vue'

import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(router);
Vue.use(ElementUI);
Vue.use(store);
Vue.use(VueAxios, axios);

Vue.config.productionTip = false

new Vue({
	router,
	store,
	render: h => h(App),
}).$mount('#app')

router.beforeEach((to, from, next) => {
	//获取用户登录成功后储存的登录标志
	let getFlag = localStorage.getItem("Flag");
	//判断用户是否已登录
	if(getFlag == 'isLogin'){
		store.state.isLogin = true;
		next();
		//若已登录再想进入登录界面，则直接定向回首页
		if(!to.meta.isLogin){
			next({
				path: '/main'
			})
		}
	}else{
		if(to.meta.isLogin){
			next({
				path: '/login',
			})
		}else{
			next();
		}
	}
});

router.afterEach(router => {
	window.scroll(0, 0);
});



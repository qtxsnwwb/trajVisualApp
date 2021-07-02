<template>
	<div>
		<el-container>
			<!-- 导航栏 -->
			<el-header style="background-color: #18223d;">
				<!-- 此处写导航栏代码 -->
				
				<!-- 登录 -->
				<p v-if="$store.state.isLogin == true">
					欢迎您，{{$store.state.userName}}
					<button @click="logout">注销</button>
				</p>
				<p v-else @click="skipToLogin">登录</p>
			</el-header>
			<!-- 主体部分 -->
			<el-main style="background-color: red;">
				
			</el-main>
		</el-container>
	</div>
	
</template>

<script>
export default {
	name: "Main",
	methods: {
		//跳转到登录界面
		skipToLogin() {
			this.$router.push("/login");
		},
		//注销
		logout() {
			localStorage.removeItem("Flag");
			this.$store.dispatch("userLogin", false);
		}
	}
}
</script>

<style>
* {
	padding: 0;
	margin: 0;
}
p {
	color: #FFFFFF;
}
p:hover {
	cursor: pointer;
}
</style>

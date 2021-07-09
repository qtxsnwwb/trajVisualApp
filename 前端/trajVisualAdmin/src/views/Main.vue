<template>
	<div>
		<el-container>
			<!-- 导航栏 -->
			<el-header style="height: calc(5vh);">
				<el-row type="flex" align="middle">
					<!-- 标题 -->
					<el-col :span="4" class="hidden-sm-and-down">
						<div class="nav-title">
							后台管理系统
						</div>
					</el-col>
					<!-- 菜单 -->
					<el-col :span="16" class="hidden-sm-and-down">
						<el-row type="flex">
							<el-col :span="2" v-for="menu_item in menu_content">
								<div class="nav-menu-item">
									{{menu_item.name}}
								</div>
							</el-col>
						</el-row>
					</el-col>
					<el-col :xs="9" class="hidden-sm-and-up">
						<div class="nav-icon" @click="drawer = true">
							<i class="el-icon-s-unfold" style="font-size: 30px;"></i>
						</div>
					</el-col>
					<!-- 用户信息 -->
					<el-col :span="4" :xs="15">
						<div class="nav-userInfo">
							欢迎您，{{$store.state.userName}}
							<el-button type="info" @click="logout">退出</el-button>
						</div>
					</el-col>
				</el-row>
			</el-header>
			<el-container>
				<!-- 侧边栏 -->
				<el-aside style="background-color: black;width: 15%;">
					
				</el-aside>
				<!-- 主体 -->
				<el-main style="background-color: green;width: 85%;">
					
				</el-main>
			</el-container>
		</el-container>
		
		<!-- 抽屉 -->
		<el-drawer title="后台管理系统" :visible.sync="drawer" :direction="direction" size="60%" class="hidden-sm-and-up">
			<!-- <el-table :data="menu_content">
				<el-table-column property="name" label="demo" width="100"></el-table-column>
				<el-table-column property="date" label="demo2" width="100"></el-table-column>
			</el-table> -->
			<el-row>
				<el-col :span="24" v-for="menu_item in menu_content">
					<div class="drawer-menu-item">
						{{menu_item.name}}
					</div>
				</el-col>
			</el-row>
		</el-drawer>
	</div>
</template>

<script>
export default {
	name: 'Main',
	data() {
		return {
			drawer: false,    //抽屉显示
			direction: "ltr",     //抽屉方向
			menu_content: [      //导航菜单
				{
					name: '首页'
				},
				{
					name: '业务监控'
				},
				{
					name: '系统监控'
				},
				{
					name: '故障发现'
				},
				{
					name: '故障定位'
				},
				{
					name: '故障处理'
				},
				{
					name: '故障管理'
				},
				{
					name: '配置管理'
				}
			],
		}
	},
	methods: {
		//注销
		logout() {
			localStorage.removeItem("Flag");
			this.$store.dispatch("userLogin", false);
			this.$router.push("/login");
		}
	}
}
</script>

<style lang="scss">
* {
	margin: 0;
	padding: 0;
}
.el-header {
	background-color: rgb(40, 162, 234);
}
.nav-title {
	font-size: 22px;
	color: #ffffff;
	text-align: left;
	font-weight: bold;
	line-height: calc(5vh);
	overflow: hidden;
}
.nav-menu-item {
	text-align: center;
	color: #ffffff;
	font-size: 18px;
	line-height: calc(5vh);
}
.nav-icon:hover {
	cursor: pointer;
}
.nav-userInfo {
	text-align: right;
	color: #FFFFFF;
	font-size: 18px;
	line-height: calc(5vh);
}
.drawer-menu-item {
	text-align: center;
	color: #00193A;
	font-size: 22px;
	margin-top: 25px;
	padding: 10px;
}
.drawer-menu-item:hover {
	background-color: rgba($color: #808080, $alpha: 0.2) !important;
	cursor: pointer;
}
.el-aside {
	height: calc(95vh);
}
.el-main {
	height: calc(95vh);
}
</style>

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
							<el-col :span="2" v-for="(menu_item, index) in menu_content">
								<div class="nav-menu-item" @click="selectMenu(index)">
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
				<el-aside style="background-color: rgb(51, 51, 51);width: 13%;" class="hidden-sm-and-down">
					<el-menu v-for="aside_item in aside_content" background-color="rgb(51, 51, 51)" text-color="#fff" active-text-color="rgb(40, 162, 234)" router :default-active="'/userManage'">
						<el-menu-item  :index="aside_item.route">
							<i class="el-icon-menu"></i>
							<span class="aside-span">{{aside_item.name}}</span>
						</el-menu-item>
					</el-menu>
				</el-aside>
				<!-- 主体 -->
				<el-main style="width: 87%;">
					<router-view></router-view>
				</el-main>
			</el-container>
		</el-container>
		
		<!-- 抽屉 -->
		<el-drawer title="后台管理系统" :visible.sync="drawer" :direction="direction" size="45%" class="hidden-sm-and-up">
			<el-menu v-for="(menu_item, index) in menu_content" router :default-active="'/userManage'">
				<el-submenu index="1">
					<template slot="title">
						<i class="el-icon-document"></i>
						{{menu_item.name}}
					</template>
					
					<el-menu-item-group v-for="aside_item in menu_item.aside">
						<el-menu-item :index="aside_item.route" @click="drawer = false">
							<i class="el-icon-menu"></i>
							{{aside_item.name}}
						</el-menu-item>
					</el-menu-item-group>
				</el-submenu>
			</el-menu>
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
					name: '首页',
					aside: ''
				},
				{
					name: '业务监控',
					aside: ''
				},
				{
					name: '系统监控',
					aside: ''
				},
				{
					name: '故障发现',
					aside: ''
				},
				{
					name: '故障定位',
					aside: ''
				},
				{
					name: '故障处理',
					aside: ''
				},
				{
					name: '故障管理',
					aside: ''
				},
				{
					name: '配置管理',
					aside: ''
				}
			],
			aside_content: '',     //侧边栏内容
			aside_0: [
				{
					name: '用户信息管理',
					route: '/userManage'
				},
				{
					name: '测试1',
					route: '/test1'
				},
				{
					name: '测试2',
					route: '4-1'
				}
			],
			aside_1: [
				{
					name: '测试3',
					route: ''
				},
				{
					name: '测试4',
					route: ''
				},
				{
					name: '测试5',
					route: ''
				}
			],
			aside_2: [
				{
					name: '测试6',
					route: ''
				},
				{
					name: '测试7',
					route: ''
				},
				{
					name: '测试8',
					route: ''
				}
			]
		}
	},
	methods: {
		//注销
		logout() {
			localStorage.removeItem("Flag");
			this.$store.dispatch("userLogin", false);
			this.$router.push("/login");
		},
		//导航栏选择侧边栏
		selectMenu(index) {
			if(index == 0){
				this.aside_content = this.aside_0;
			}else if(index == 1){
				this.aside_content = this.aside_1;
			}else if(index == 2){
				this.aside_content = this.aside_2;
			}
		},
	},
	mounted() {
		//挂载侧边栏菜单
		this.aside_content = this.aside_0;
		//挂载导航栏子菜单
		var menuData = this.menu_content;
		menuData[0].aside = this.aside_0;
		menuData[1].aside = this.aside_1;
		menuData[2].aside = this.aside_2;
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
.nav-menu-item:hover {
	cursor: pointer;
	background-color: rgba($color: #FFFFFF, $alpha: 0.2) !important;
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
.aside-span {
	font-size: 18px;
}
.el-aside {
	height: calc(95vh);
}
.el-main {
	height: calc(95vh);
}
</style>

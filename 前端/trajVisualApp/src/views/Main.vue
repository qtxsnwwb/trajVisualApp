<template>
	<div>
		<el-container>
			<!-- 导航栏 -->
			<el-header style="background-color: #18223d;height: calc(5vh);">
				<!-- 此处写导航栏代码 -->
				
				<!-- 登录 -->
				<p v-if="$store.state.isLogin == true">
					欢迎您，{{$store.state.userName}}
					<button @click="logout">注销</button>
				</p>
				<p v-else @click="skipToLogin">登录</p>
			</el-header>
			<!-- 主体部分 -->
			<el-main style="padding: 0;">
				<div id="map"></div>
			</el-main>
		</el-container>
	</div>
	
</template>

<script>
export default {
	name: "Main",
	data() {
		return {
			map: ""
		};
	},
	methods: {
		//跳转到登录界面
		skipToLogin() {
			this.$router.push("/login");
		},
		//注销
		logout() {
			localStorage.removeItem("Flag");
			this.$store.dispatch("userLogin", false);
		},
		//初始化地图
		initMap() {
			this.map = L.map("map", {
				center: [40.02404009136253, 116.50641060224784],     //地图中心
				zoom: 11,    //缩放比例
				// zoomControl: false,     //禁用 + - 按钮
				doubleClickZoom: false,    //禁用双击放大
				attributionControl: false     //移除右下角Leaflet标识
			});
			//天地图影像图底图（墨卡托坐标）
			let basicLayer = L.tileLayer(
				"http://t4.tianditu.gov.cn/DataServer?T=img_w&x={x}&y={y}&l={z}&tk=efe5e7d29b0c9728d44edba8dc08c8d7",
			).addTo(this.map);
			//天地图影像图标记（墨卡托坐标）
			let markLayer = L.tileLayer(
				"http://t4.tianditu.gov.cn/DataServer?T=cia_w&x={x}&y={y}&l={z}&tk=efe5e7d29b0c9728d44edba8dc08c8d7"
			).addTo(this.map);
			// this.map.removeLayer(name);     //移除图层
			
			var that = this;
			//缩放事件
			this.map.on("zoomend", function(e){
				// var zoom_val = e.target.getZoom();     //获取缩放级别
				that.getTrajData();
			});
			//拖动地图事件
			this.map.on("moveend", function(e){
				that.getTrajData();
			});
			
			
		},
		//读取轨迹数据
		getTrajData() {
			var leftdown_lng = this.map.getBounds().getSouthWest().lng;     //左下角经度
			var leftdown_lat = this.map.getBounds().getSouthWest().lat;     //左下角纬度
			var rightup_lng = this.map.getBounds().getNorthEast().lng;      //右上角经度
			var rightup_lat = this.map.getBounds().getNorthEast().lat;      //右上角纬度
			console.log(leftdown_lat)
			//向后端发送请求，读取轨迹数据
			
		}
	},
	mounted() {
		this.initMap();
	}
}
</script>

<style lang="scss">
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
#map {
	width: 100%;
	height: calc(95vh);
	z-index: 1;
}
</style>

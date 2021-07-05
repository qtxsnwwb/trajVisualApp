<template>
	<div>
		<el-container>
			<!-- 导航栏 -->
			<el-header style="background-color: #18223d;height: calc(5vh);">
				<!-- 此处写导航栏代码 -->
				
				<!-- 切换地图下拉菜单 -->
				<el-dropdown @command="changeMap">
					<span class="el-dropdown-link">
						切换地图<i class="el-icon-arrow-down el-icon--right"></i> 
					</span>
					<el-dropdown-menu slot="dropdown">
						<el-dropdown-item icon="el-icon-circle-check" command="tianditu_1">天地图街道图</el-dropdown-item>
						<el-dropdown-item icon="el-icon-circle-check" command="tianditu_2">天地图影像图</el-dropdown-item>
						<el-dropdown-item icon="el-icon-circle-check" command="tianditu_3">天地图地形图</el-dropdown-item>
					</el-dropdown-menu>
				</el-dropdown>
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
//引入鹰眼图组件
import MiniMap from 'leaflet-minimap'
import 'leaflet-minimap/dist/Control.MiniMap.min.css'
export default {
	name: "Main",
	data() {
		return {
			map: "",     //地图
			trajIcon: "",     //图标
			// point: ""
			tianditu_1_tile: "",     //天地图矢量底图
			tianditu_1_marker: "",      //天地图矢量标记
			tianditu_2_tile: "",     //天地图影像底图
			tianditu_2_marker: "",      //天地图影像标记
			tianditu_3_tile: "",     //天地图地形底图
			tianditu_3_marker: "",      //天地图地形标记
			basicLayer: "",       //底图图层
			markerLayer: "",      //注解图层
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
			//初始化地图对象
			this.map = L.map("map", {
				center: [40.02404009136253, 116.50641060224784],     //地图中心
				zoom: 11,    //缩放比例
				// zoomControl: false,     //禁用 + - 按钮
				doubleClickZoom: false,    //禁用双击放大
				attributionControl: false     //移除右下角Leaflet标识
			});
			//初始化地图图层（墨卡托坐标）
			this.tianditu_1_tile = "http://t4.tianditu.gov.cn/DataServer?T=vec_w&x={x}&y={y}&l={z}&tk=efe5e7d29b0c9728d44edba8dc08c8d7";
			this.tianditu_1_marker = "http://t4.tianditu.gov.cn/DataServer?T=cva_w&x={x}&y={y}&l={z}&tk=efe5e7d29b0c9728d44edba8dc08c8d7";
			this.tianditu_2_tile = "http://t4.tianditu.gov.cn/DataServer?T=img_w&x={x}&y={y}&l={z}&tk=efe5e7d29b0c9728d44edba8dc08c8d7";
			this.tianditu_2_marker = "http://t4.tianditu.gov.cn/DataServer?T=cia_w&x={x}&y={y}&l={z}&tk=efe5e7d29b0c9728d44edba8dc08c8d7";
			this.tianditu_3_tile = "http://t4.tianditu.gov.cn/DataServer?T=ter_w&x={x}&y={y}&l={z}&tk=efe5e7d29b0c9728d44edba8dc08c8d7";
			this.tiandutu_3_marker = "http://t4.tianditu.gov.cn/DataServer?T=cta_w&x={x}&y={y}&l={z}&tk=efe5e7d29b0c9728d44edba8dc08c8d7";
			//天地图影像图底图（墨卡托坐标）
			this.basicLayer = L.tileLayer(
				this.tianditu_1_tile,
			).addTo(this.map);
			
			//天地图影像图标记（墨卡托坐标）
			this.markLayer = L.tileLayer(
				this.tianditu_1_marker,
			).addTo(this.map);
			// this.map.removeLayer(name);     //移除图层
			
			//初始化图标
			this.trajIcon = L.divIcon({
				className: 'my-div-icon',     //自定义icon css样式
				iconSize: [15, 15]     //点大小
			});
			
			//添加鹰眼图
			var osmUrl = "http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineCommunity/MapServer/tile/{z}/{y}/{x}";     //ArcGis地图
			var osm = new L.tileLayer(osmUrl, {minZoom: 0, maxZoom: 13});
			var miniMap = new MiniMap(osm, {toggleDisplay: true, width: 300, height: 300}).addTo(this.map);
			
			//初始化调用轨迹数据
			this.getTrajData();
			
			//初始化绘制轨迹
			this.drawTrajectory();
			
			var that = this;
			//拖动地图事件
			this.map.on("moveend", function(e){
				that.getTrajData();
			});
			
			//地图点击事件
			var clickpop = L.popup();
			this.map.on("click", function(e){
				content = "经度：" + e.latlng.lng + "<br/>纬度：" + e.latlng.lat;
				clickpop.setLatLng(e.latlng).setContent(content).openOn(that.map);
			});
		},
		//读取轨迹数据
		getTrajData() {
			var leftdown_lng = this.map.getBounds().getSouthWest().lng;     //左下角经度
			var leftdown_lat = this.map.getBounds().getSouthWest().lat;     //左下角纬度
			var rightup_lng = this.map.getBounds().getNorthEast().lng;      //右上角经度
			var rightup_lat = this.map.getBounds().getNorthEast().lat;      //右上角纬度
			// console.log(leftdown_lat)
			//向后端发送请求，读取轨迹数据
			
			//模拟JSON获取轨迹数据
			var group = L.layerGroup().addTo(this.map);      //图层组
			this.axios.get('/point.json')
			.then(function(response){
				var point = response.data;     //全部轨迹数据
				for(var i=0; i<point.length; i++){
					var lon = point[i].lon;
					var lat = point[i].lat;
					var marker = L.marker([lon, lat], {
						icon: this.trajIcon,
					}).addTo(group);
				}
			}.bind(this))
			.catch(function(error){
				console.log(error);
			});
			
			
		},
		//切换地图
		changeMap(command) {
			if(command == "tianditu_1"){
				this.basicLayer.setUrl(this.tianditu_1_tile, false);
				this.markLayer.setUrl(this.tianditu_1_marker, false);
			}else if(command == "tianditu_2"){
				this.basicLayer.setUrl(this.tianditu_2_tile, false);
				this.markLayer.setUrl(this.tianditu_2_marker, false);
			}else{
				this.basicLayer.setUrl(this.tianditu_3_tile, false);
				this.markLayer.setUrl(this.tianditu_3_marker, false);
			}
		},
		//绘制轨迹
		drawTrajectory() {
			var latlngs = [
			    [[17.385044, 78.486671], [16.506174, 80.648015], [17.686816, 83.218482]],
			    [[13.082680, 80.270718], [12.971599, 77.594563],[15.828126, 78.037279]]
			];
			var multiPolyLineOptions = {color: 'red'};
			var multiPolyline = L.polyline(latlngs, multiPolyLineOptions);
			multiPolyline.addTo(this.map);
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
.el-dropdown-link {
	cursor: pointer;
	color: #409EFF;
}
.el-icon-arrow-down {
	font-size: 12px;
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
.my-div-icon {
	width: 15px;
	height: 15px;
	background-color: red;
	border-radius: 50%;
}
</style>

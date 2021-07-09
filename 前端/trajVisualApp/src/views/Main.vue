<template>
	<div>
		<el-container>
			<!-- 导航栏 -->
			<el-header style="background-color: #18223d;height: calc(5vh);">
				<!-- 此处写导航栏代码 -->
				<div>
					<el-row>
						<el-col :span="20">
							<el-menu class="el-menu-traj"
									mode="horizontal"
									background-color="#18223d"
									text-color="#fffefd"
									active-text-color="#ffffff"
									style="border-bottom: none;">
								<el-row>
									<!-- 标题 -->
									<el-col :span="5" :xs="0" class="hidden-sm-and-down">
										<el-menu-item style="text-align: left;">
											<span class="title-span">船舶轨迹大数据可视化系统</span>
										</el-menu-item>
									</el-col>
									<el-col :span="1.5" :xs="7" style="margin-left: 15px;">
										<el-menu-item>
											<span class="func-span">船舶交通网络</span>
										</el-menu-item>
									</el-col>
									<el-col :span="1.5" :xs="7">
										<el-menu-item>
											<span class="func-span">轨迹聚类</span>
										</el-menu-item>
									</el-col>
									<el-col :span="1.5" :xs="7">
										<el-menu-item>
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
										</el-menu-item>
									</el-col>
								</el-row>
							</el-menu>
						</el-col>
						<!-- 登录 -->
						<el-col :span="4" :xs="2" style="text-align: right;">
							<div class="rightsection">
								<span v-if="$store.state.isLogin == true">
									欢迎您，{{$store.state.userName}}
									<el-button type="primary" @click="logout">退出</el-button>
								</span>
								<span class="btn-click" v-else @click="skipToLogin">登录</span>
							</div>
						</el-col>
					</el-row>
				</div>
			</el-header>
			<!-- 主体部分 -->
			<el-main style="padding: 0;">
				<div id="map" v-loading="loading" element-loading-text="拼命加载中" element-loading-spinner="el-icon-loading" element-loading-background="rgba(0, 0, 0, 0.8)"></div>
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
			loading: true       //加载动画
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
				var content = "经度：" + e.latlng.lng + "<br/>纬度：" + e.latlng.lat;
				clickpop.setLatLng(e.latlng).setContent(content).openOn(that.map);
			});
			
			//关闭加载动画
			this.loading = false;
		},
		//读取轨迹数据
		getTrajData() {
			this.loading = true;     //开启加载动画
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
			
			this.loading = false;     //关闭加载动画
		},
		//切换地图
		changeMap(command) {
			this.loading = true;      //开启加载动画
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
			this.loading = false;       //关闭加载动画
		},
		//绘制轨迹
		drawTrajectory() {
			this.loading = true;        //开启加载动画
			var latlngs = [
			    [[17.385044, 78.486671], [16.506174, 80.648015], [17.686816, 83.218482]],
			    [[13.082680, 80.270718], [12.971599, 77.594563],[15.828126, 78.037279]]
			];
			var multiPolyLineOptions = {color: 'red'};
			var multiPolyline = L.polyline(latlngs, multiPolyLineOptions);
			multiPolyline.addTo(this.map);
			this.loading = false;         //关闭加载动画
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
.title-span {
	font-size: 25px;
}
.func-span {
	font-size: 18px;
}
.el-menu-item {
	text-align: center;
}
.el-menu-item:hover {
	background-color: rgba($color: #ffffff, $alpha: 0.2) !important;
}
.rightsection {
	line-height: 60px;
	font-size: 18px;
	color: #ffffff;
}
.btn-click:hover {
	padding: 15px;
	cursor: pointer;
	background-color: rgba($color: #ffffff, $alpha: 0.2);
}
.el-dropdown-link {
	// cursor: pointer;
	color: #ffffff;
	font-size: 18px;
}
.el-icon-arrow-down {
	font-size: 12px;
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

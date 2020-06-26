<template>
  <div id="app">
   <div class="wrapper">
      <Topheader></Topheader>
      <div class="page-wrap">
        <Sidebar></Sidebar>
          <div class="main-content">
            <div class="container-fluid">
                <div id ="main_app">
                </div>
            </div>
          </div>
          <Rightsidebar></Rightsidebar>
          <Chartpanel></Chartpanel>
          <Footer></Footer>
            
      </div>
     
      <router-view/>
    </div>
    <Togglemenu></Togglemenu>
    
  </div>

</template>

<script>
import Sidebar from "./components/layouts/Sidebar";
import Topheader from "./components/layouts/Topheader";
import Rightsidebar from "./components/layouts/Rightsidebar";
import Chartpanel from "./components/layouts/Chartpanel";
import Footer from "./components/layouts/Footer";
import Togglemenu from "./components/layouts/Togglemenu";




export default {
  name: 'App',
  components:{
   Sidebar,
   Topheader,
   Rightsidebar,
   Chartpanel,
   Footer,
   Togglemenu,
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

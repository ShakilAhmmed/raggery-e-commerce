<template>
  <div id="app">
    <div class="wrapper">
      <Topheader></Topheader>
      <div class="page-wrap">
        <Sidebar></Sidebar>
        <div class="main-content">
          <div class="container-fluid">
            <PageHead></PageHead>
            <div id="main_app">
                <router-view/>
            </div>
          </div>
        </div>
        <Rightsidebar></Rightsidebar>
        <Chartpanel></Chartpanel>
        <Footer></Footer>

      </div>


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
  import PageHead from "./components/layouts/PageHeader";


  export default {
    name: 'App',
    components: {
      Sidebar,
      Topheader,
      Rightsidebar,
      Chartpanel,
      Footer,
      Togglemenu,
      PageHead
    },
  }
</script>



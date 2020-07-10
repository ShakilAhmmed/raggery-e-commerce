<template>
  <div id="sidebar">

    <div class="app-sidebar colored">
      <div class="sidebar-header">
        <a class="header-brand" href="index.html">
          <div class="logo-img">
            <img src="static/admin_asset/src/img/brand-white.svg" class="header-brand-img" alt="lavalite">
          </div>
          <span class="text">Raggery</span>
        </a>
        <button type="button" class="nav-toggle"><i data-toggle="expanded" class="ik ik-toggle-right toggle-icon"></i>
        </button>
        <button id="sidebarClose" class="nav-close"><i class="ik ik-x"></i></button>
      </div>

      <div class="sidebar-content">
        <div class="nav-container">

          <nav id="main-menu-navigation" class="navigation-main">
            <div class="nav-lavel">Navigation</div>
            <div class="nav-item active">
              <router-link to="/"><i class="ik ik-bar-chart-2"></i><span>Dashboard</span></router-link>
            </div>
            <div class="nav-item">
              <a href="pages/navbar.html"><i class="ik ik-menu"></i><span>Navigation</span> <span
                class="badge badge-success">New</span></a>
            </div>
            <div class="nav-item has-sub">
              <a href="javascript:void(0)"><i class="ik ik-layers"></i><span>Settings</span> <span
                class="badge badge-danger">150+</span></a>
              <div class="submenu-content">
                <router-link to="/menu" class="menu-item">Menu</router-link>
                <router-link to="/category" class="menu-item">Category</router-link>
                <router-link to="/sub_category" class="menu-item">Sub Category</router-link>
                <router-link to="/tree_view" class="menu-item">View</router-link>
                <router-link to="/color" class="menu-item">Color</router-link>
              </div>
            </div>

            <div class="nav-item has-sub">
              <a href="javascript:void(0)"><i class="ik ik-layers"></i><span>Address Settings</span> <span
                class="badge badge-danger">150+</span></a>
              <div class="submenu-content">
                <router-link to="/division" class="menu-item">Division</router-link>
              </div>
            </div>
          </nav>


        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: "Sidebar"
  }
</script>

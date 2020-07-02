import Vue from "vue";
import Router from "vue-router";
import Dashboard from "@/components/Dashboard";
import MenuComponent from "@/components/Backend/Menu/MenuComponent";
import ColorComponent from "@/components/Backend/Menu/ColorComponent";
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Dashboard",
      component: Dashboard,
      meta:{
        "page_title" :"Dashboard",
        "menu" :"Home",
        "page_description":"Home",
      }
    },
    {
      path: "/menu",
      name: "Menu",
      component: MenuComponent,
      meta:{
        "page_title" :"Menu",
        "menu" :"Settings",
        "page_description":"Create Site Menu",
      }
    },
    {
      path: "/color",
      name : "Color",
      component: ColorComponent,
      meta:{
        "page_title" :"Color",
        "menu" :"product",
        "page_description":"Create Site Color",
      }
    }
  ]
});

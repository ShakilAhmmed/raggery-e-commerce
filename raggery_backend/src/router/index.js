import Vue from "vue";
import Router from "vue-router";
import Dashboard from "../components/Dashboard";
import MenuComponent from "../components/Backend/Menu/MenuComponent";
import CategoryComponent from "../components/Backend/Category/CategoryComponent";
import ColorComponent from "@/components/Backend/Menu/ColorComponent";
import SubCategoryComponent from "../components/Backend/SubCategory/SubCategoryComponent";
import TreeView from "../components/Backend/TreeView/TreeView";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Dashboard",
      component: Dashboard,
      meta: {
        "page_title": "Dashboard",
        "menu": "Home",
        "page_description": "Home",
      }
    },
    {
      path: "/menu",
      name: "Menu",
      component: MenuComponent,
      meta: {
        "page_title": "Menu",
        "menu": "Settings",
        "page_description": "Create Site Menu",
      }
    },
    {
      path: "/category",
      name: "CategoryComponent",
      component: CategoryComponent,
      meta: {
        "page_title": "Category",
        "menu": "Settings",
        "page_description": "Create Site Category",
      }
    },
    {
      path: "/sub_category",
      name: "Sub Category",
      component: SubCategoryComponent,
      meta: {
        "page_title": "Sub Category",
        "menu": "Settings",
        "page_description": "Create Site Sub Category",
      }
    },
    {
      path: "/tree_view",
      name: "Tree View",
      component: TreeView,
      meta: {
        "page_title": "Tree View",
        "menu": "Settings",
        "page_description": "Tree View",
      }
    },
    {
      path: "/color",
      name: "Color",
      component: ColorComponent,
      meta: {
        "page_title": "Color",
        "menu": "product",
        "page_description": "Create Site Color",
      }
    }
  ]
});

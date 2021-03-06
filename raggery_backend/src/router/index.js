import Vue from "vue";
import Router from "vue-router";
import Dashboard from "../components/Dashboard";
import MenuComponent from "../components/Backend/Menu/MenuComponent";
import CategoryComponent from "../components/Backend/Category/CategoryComponent";
import ColorComponent from "@/components/Backend/Menu/ColorComponent";
import SubCategoryComponent from "../components/Backend/SubCategory/SubCategoryComponent";
import TreeView from "../components/Backend/TreeView/TreeView";
import Division from "../components/Backend/Address/Division";
import District from "../components/Backend/Address/District";
import SubDistrict from "../components/Backend/Address/SubDistrict";
import BrandComponent from "../components/Backend/Brand/BrandComponent";
import SizeComponent from "../components/Backend/Size/SizeComponent";

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
      path: "/division",
      name: "Division",
      component: Division,
      meta: {
        "page_title": "Division",
        "menu": "Address Settings",
        "page_description": "Division",
      }
    },
    {
      path: "/district",
      name: "District",
      component: District,
      meta: {
        "page_title": "District",
        "menu": "Address Settings",
        "page_description": "District",
      }
    },
    {
      path: "/sub_district",
      name: "Sub District",
      component: SubDistrict,
      meta: {
        "page_title": "Sub District",
        "menu": "Address Settings",
        "page_description": "District",
      }
    },
    {
      path: "/color",
      name: "Color",
      component: ColorComponent,
      meta: {
        "page_title": "Color",
        "menu": "Product",
        "page_description": "Create Site Color",
      }

    },
    {
      path: "/brand",
      name: "Brand",
      component: BrandComponent,
      meta: {
        "page_title": "Brand",
        "menu": "Product",
        "page_description": "Create Brand",
      }

    },
    {
      path: "/size",
      name: "Size",
      component: SizeComponent,
      meta: {
        "page_title": "Size",
        "menu": "Product",
        "page_description": "Create Size",
      }

    },

  ]
});

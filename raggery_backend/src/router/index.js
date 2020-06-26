import Vue from "vue";
import Router from "vue-router";
import HelloWorld from "@/components/Dashboard";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Dashboard",
      component: HelloWorld
    }
  ]
});

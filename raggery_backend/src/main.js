import Vue from 'vue';
import App from './App';
import router from './router';
import axios from 'axios';
import VueAxios from 'vue-axios';
import VueToastr2 from 'vue-toastr-2'
import 'vue-toastr-2/dist/vue-toastr-2.min.css'
import Paginate from 'vuejs-paginate';
import Loading from 'vue-loading-overlay';
// Import stylesheet
import 'vue-loading-overlay/dist/vue-loading.css';
// Init plugin

Vue.component('paginate', Paginate);
Vue.use(VueAxios, axios);
 Vue.use(Loading,{
   loader: 'dots',
   backgroundColor: '#ffffff',
 });
window.toastr = require('toastr');
Vue.use(VueToastr2);
Vue.config.productionTip = false;
window.basePath = "http://127.0.0.1:8000/api/v1/";
window.perPage = 5;

Vue.mixin({
  data() {
    return {
      base_path: "api/v1/",
      host_address: "http://127.0.0.1:8001/"
    }
  },
  methods: {
    Slugify: function (event) {
      let slug = "";
      let title = event.target.value;
      // Change to lower case
      let titleLower = title.toLowerCase();
      // Letter "e"
      slug = titleLower.replace(/e|é|è|ẽ|ẻ|ẹ|ê|ế|ề|ễ|ể|ệ/gi, 'e');
      // Letter "a"
      slug = slug.replace(/a|á|à|ã|ả|ạ|ă|ắ|ằ|ẵ|ẳ|ặ|â|ấ|ầ|ẫ|ẩ|ậ/gi, 'a');
      // Letter "o"
      slug = slug.replace(/o|ó|ò|õ|ỏ|ọ|ô|ố|ồ|ỗ|ổ|ộ|ơ|ớ|ờ|ỡ|ở|ợ/gi, 'o');
      // Letter "u"
      slug = slug.replace(/u|ú|ù|ũ|ủ|ụ|ư|ứ|ừ|ữ|ử|ự/gi, 'u');
      // Letter "d"
      slug = slug.replace(/đ/gi, 'd');
      // Trim the last whitespace
      slug = slug.replace(/\s*$/g, '');
      // Change whitespace to "-"
      slug = slug.replace(/\s+/g, '-');
      slug = slug.replace("'", '');
      return slug;

    },
    Loader: function () {
         let loader = this.$loading.show();
        setTimeout(() => loader.hide(), 2000)
    },


  }
});


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})

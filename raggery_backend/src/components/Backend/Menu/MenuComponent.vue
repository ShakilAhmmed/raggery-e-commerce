<template>
  <div id="menu">
    <button type="button" class="modal_button btn btn-primary" data-toggle="modal"
            data-target="#demoModal">
      Create Menu
    </button>
    <div class="modal fade" id="demoModal" tabindex="-1" role="dialog" aria-labelledby="demoModalLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="demoModalLabel">Create Menu</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="AddMenu">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">

                  <div class="form-group">
                    <label for="exampleInputName">Name</label>
                    <input type="text" v-model="MenuForm.name" @keyup="MakeMenuSlug" class="form-control"
                           id="exampleInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputSlug">Slug</label>
                    <input type="text" v-model="MenuForm.slug" class="form-control" id="exampleInputSlug" readonly>
                    <span class="mt-5 text-danger" v-if="AllError.slug" v-text="AllError.slug[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputStatus">Status</label>
                    <select id="exampleInputStatus" class="form-control" v-model="MenuForm.status">
                      <option value="" selected disabled>Select</option>
                      <option value="1">Active</option>
                      <option value="0">Inactive</option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.status" v-text="AllError.status[0]"></span>
                  </div>

                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-light" data-dismiss="modal">Close</button>
              <button type="submit" class="btn btn-primary mr-2">Save</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <br>
    <div>

    </div>
    <div class="card">
      <div class="card-header d-block">
        <div class="row">
          <div class="col-md-1">
            <div class="form-group">
              <select class="form-control">
                <option>1</option>
              </select>
            </div>
          </div>
          <div class="col-md-9"></div>
          <div class="col-md-2">
            <div class="form-group">
              <input class="form-control"/>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body p-0 table-border-style">
        <div class="table-responsive">
          <table class="table">
            <thead>
            <tr>
              <th>Sl No</th>
              <th>Name</th>
              <th>Slug</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(menu,index) in MenuList">
              <th scope="row">{{index+1}}</th>
              <td>{{menu.name}}</td>
              <td>{{menu.slug}}</td>
              <td>
                <span v-if="menu.status === true" class="badge badge-pill badge-success mb-1">Active</span>
                <span v-else class="badge badge-pill badge-danger mb-1">Inactive</span>
              </td>
              <td>@mdo</td>
            </tr>

            </tbody>
          </table>
          <paginate
            :page-count="total_page"
            :click-handler="paginate"
            :prev-text="'Prev'"
            :next-text="'Next'"
            :container-class="'pagination'"
            :page-link-class="'page-link'"
            :prev-link-class="'page-link'"
            :next-link-class="'page-link'"
            :prev-class="'paginate_button page-item previous'"
            :next-class="'paginate_button page-item next'"
            :page-class="'paginate_button page-item'">
          </paginate>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  export default {
    name: "MenuComponent",
    data() {
      return {
        MenuForm: {
          name: '',
          slug: '',
          status: ''
        },
        AllError: [],
        MenuList: [],
        total_page: 0
      }
    },
    methods: {
      paginate: function (pageNum) {
        const _this = this;
        _this.GetMenu(pageNum)
      },
      GetMenu: function (page = 1) {
        const _this = this;
        this.axios.get(basePath + "menu?page=" + page)
          .then((response) => {
            _this.MenuList = response.data.results;
            _this.total_page = Math.ceil(response.data.count / perPage);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      AddMenu: function () {
        const _this = this;
        this.axios.post(basePath + "menu", _this.MenuForm)
          .then((response) => {
            this.$toastr.success('New Menu Added Successfully!', 'Success');
            _this.Reset();
          })
          .catch((error) => {
            _this.AllError = error.response.data.errors;
          })
      },
      Reset: function () {
        const _this = this;
        _this.AllError = []
        Object.keys(_this.MenuForm).forEach(function (key, index) {
          _this.MenuForm[key] = '';
        });
      },
      MakeMenuSlug: function (event) {
        const _this = this;
        _this.MenuForm.slug = this.Slugify(event);
      }
    },
    created() {
      this.Loader();
      this.GetMenu();
    }
  }
</script>

<style scoped>

</style>

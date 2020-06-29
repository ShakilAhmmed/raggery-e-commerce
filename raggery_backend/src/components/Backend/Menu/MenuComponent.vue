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


    <div class="modal fade" id="menuEditModal" tabindex="-1" role="dialog" aria-labelledby="demoModalLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="menuEditLabel">Create Menu</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="EditMenu">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">

                  <div class="form-group">
                    <label for="editInputName">Name</label>
                    <input type="text" v-model="EditMenuForm.name" @keyup="MakeMenuSlug($event,true)"
                           class="form-control"
                           id="editInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="editInputSlug">Slug</label>
                    <input type="text" v-model="EditMenuForm.slug" class="form-control" id="editInputSlug" readonly>
                    <span class="mt-5 text-danger" v-if="AllError.slug" v-text="AllError.slug[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="editInputStatus">Status</label>
                    <select id="editInputStatus" class="form-control" v-model="EditMenuForm.status">
                      <option value="" disabled>Select</option>
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
              <label>
                <select class="form-control limit" v-model="limit">
                  <option v-for="limit_value in limits"> {{ limit_value }}</option>
                </select>
              </label>
            </div>
          </div>
          <div class="col-md-9"></div>
          <div class="col-md-2">
            <div class="form-group">
              <input v-model="search_key" class="form-control"/>
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
              <td>
                <button class="btn btn-danger" @click="deleteMenu(index,menu.id)">
                  <font-awesome-icon icon="trash"/>
                </button>
                <button @click="statusChange(menu.id)"
                        :class="menu.status === true ? 'btn btn-success' : 'btn btn-warning'">
                  <font-awesome-icon v-if="menu.status === true" icon="check-circle"/>
                  <font-awesome-icon v-else icon="times-circle"/>
                </button>

                <button class="btn btn-primary" data-toggle="modal"
                        data-target="#menuEditModal" @click="viewMenu(menu.id)">
                  <font-awesome-icon icon="pencil-alt"/>
                </button>
              </td>
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
        EditMenuForm: {
          id: '',
          name: '',
          slug: '',
          status: ''
        },
        AllError: [],
        MenuList: [],
        total_page: 0,
        search_key: '',
        limit: 5,
        limits: limitOption
      }
    },
    watch: {
      'search_key': function () {
        this.GetMenu();
      },
      'limit': function () {
        this.GetMenu();
      }
    },
    methods: {
      paginate: function (pageNum) {
        const _this = this;
        _this.GetMenu(pageNum)
      },
      GetMenu: function (page = 1) {
        const _this = this;
        this.axios.get(basePath + "menu?limit=" + _this.limit + "&page=" + page + "&q=" + _this.search_key)
          .then((response) => {
            _this.MenuList = response.data.results;
            _this.total_page = Math.ceil(response.data.count / _this.limit);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      AddMenu: function () {
        const _this = this;
        this.axios.post(basePath + "menu/", _this.MenuForm)
          .then((response) => {
            this.$toastr.success('New Menu Added Successfully!', 'Success');
            _this.GetMenu();
            _this.Reset("demoModal", _this.MenuForm);
          })
          .catch((error) => {
            _this.AllError = error.response.data.errors;
          })
      },
      EditMenu: function () {
        const _this = this;
        this.axios.put(basePath + "menu/" + _this.EditMenuForm.id, _this.EditMenuForm)
          .then((response) => {
            console.log(response);
            this.$toastr.success('Menu Updated Successfully!', 'Success');
            _this.GetMenu();
            _this.Reset("menuEditModal", _this.EditMenuForm);
          })
          .catch((error) => {
            _this.AllError = error.response.data.errors;
          })
      },
      Reset: function (modal_name, form) {
        const _this = this;
        $("#" + modal_name).modal('hide');
        _this.AllError = []
        Object.keys(form).forEach(function (key, index) {
          form[key] = '';
        });
      },
      viewMenu: function (menu_id) {
        const _this = this;
        this.axios.get(basePath + "menu/" + menu_id)
          .then((response) => {
            _this.EditMenuForm = response.data;
            _this.EditMenuForm.status = response.data.status === true ? 1 : 0;
          })
          .catch((error) => {
            console.log(error)
          })
      },
      deleteMenu: function (index, menu_id) {
        const _this = this;
        this.$swal.fire({
          title: 'Are you sure?',
          text: "You won't be able to revert this!",
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
          if (result.value) {
            this.axios.delete(basePath + "menu/delete/" + menu_id)
              .then((response) => {
                console.log(response)
                _this.MenuList.splice(index, 1);
                this.$swal.fire('Deleted!', 'Menu Deleted Successfully', 'success');
              })
              .catch((error) => {
                console.log(error)
              })
          }
        })
      },
      statusChange: function (menu_id) {
        const _this = this;
        this.axios.patch(basePath + "menu/status/" + menu_id)
          .then((response) => {
            _this.GetMenu();
            if (response.data.type === true) {
              this.$toastr.success(response.data.message, 'Success');
            } else {
              this.$toastr.warning(response.data.message, 'Success');
            }
          })
          .catch((error) => {
            console.log(error)
          })
      },
      MakeMenuSlug: function (event, is_update = false) {
        const _this = this;
        if (is_update === true) {
          _this.EditMenuForm.slug = this.Slugify(event);
        } else {
          _this.MenuForm.slug = this.Slugify(event);
        }

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

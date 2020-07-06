<template>
  <div id="menu">
    <button type="button" class="modal_button btn btn-primary" data-toggle="modal"
            data-target="#demoModal">
      Create Sub Category
    </button>
    <div class="modal fade" id="demoModal" tabindex="-1" role="dialog" aria-labelledby="demoModalLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="demoModalLabel">Create Sub Category</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="AddSubCategory">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">

                  <div class="form-group">
                    <label for="exampleInputMenu">Menu</label>
                    <select type="text" v-model="SubCategoryForm.menu_id" @change="getCategory" class="form-control"
                            id="exampleInputMenu">
                      <option v-for="(menu, index) in Menu" :value="menu.id" v-text="menu.name"></option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.menu_id" v-text="AllError.menu_id[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputCategory">Category</label>
                    <select type="text" v-model="SubCategoryForm.category_id" class="form-control"
                            id="exampleInputCategory">
                      <option disabled v-if="Category.length === 0">No Data Found</option>
                      <option v-else v-for="(category, index) in Category" :value="category.id"
                              v-text="category.name"></option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.category_id" v-text="AllError.category_id[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputName">Sub Category Name</label>
                    <input type="text" v-model="SubCategoryForm.name" @keyup="MakeSubCategorySlug" class="form-control"
                           id="exampleInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputSlug">Slug</label>
                    <input type="text" v-model="SubCategoryForm.slug" class="form-control" id="exampleInputSlug"
                           readonly>
                    <span class="mt-5 text-danger" v-if="AllError.slug" v-text="AllError.slug[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputStatus">Status</label>
                    <select id="exampleInputStatus" class="form-control" v-model="SubCategoryForm.status">
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


    <div class="modal fade" id="editCategoryModal" tabindex="-1" role="dialog" aria-labelledby="demoModalLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="menuEditLabel">Edit Category</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="EditSubCategory">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">

                  <div class="form-group">
                    <label for="editInputMenu">Menu</label>
                    <select type="text" v-model="EditSubCategoryForm.menu_id" @change="getCategory" class="form-control"
                            id="editInputMenu">
                      <option v-for="(menu, index) in Menu" :value="menu.id" v-text="menu.name"></option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.menu_id" v-text="AllError.menu_id[0]"></span>
                  </div>

                  <div class="form-group">
                    <label for="editInputCategory">Category</label>
                    <select type="text" v-model="EditSubCategoryForm.category_id" class="form-control"
                            id="editInputCategory">
                      <option v-for="(category, index) in Category" :value="category.id"
                              v-text="category.name"></option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.menu_id" v-text="AllError.menu_id[0]"></span>
                  </div>

                  <div class="form-group">
                    <label for="editInputName">Name</label>
                    <input type="text" v-model="EditSubCategoryForm.name" @keyup="MakeSubCategorySlug($event,true)"
                           class="form-control"
                           id="editInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="editInputSlug">Slug</label>
                    <input type="text" v-model="EditSubCategoryForm.slug" class="form-control" id="editInputSlug"
                           readonly>
                    <span class="mt-5 text-danger" v-if="AllError.slug" v-text="AllError.slug[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="editInputStatus">Status</label>
                    <select id="editInputStatus" class="form-control" v-model="EditSubCategoryForm.status">
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
              <th>Menu</th>
              <th>Category</th>
              <th>Name</th>
              <th>Slug</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(sub_category,index) in SubCategoryList">
              <th scope="row">{{index+1}}</th>
              <td>{{sub_category.menu.name}}</td>
              <td>{{sub_category.category.name}}</td>
              <td>{{sub_category.name}}</td>
              <td>{{sub_category.slug}}</td>
              <td>
                <span v-if="sub_category.status === true" class="badge badge-pill badge-success mb-1">Active</span>
                <span v-else class="badge badge-pill badge-danger mb-1">Inactive</span>
              </td>
              <td>
                <button class="btn btn-danger" @click="deleteSubCategory(index,sub_category.id)">
                  <font-awesome-icon icon="trash"/>
                </button>
                <button @click="statusChange(sub_category.id)"
                        :class="sub_category.status === true ? 'btn btn-success' : 'btn btn-warning'">
                  <font-awesome-icon v-if="sub_category.status === true" icon="check-circle"/>
                  <font-awesome-icon v-else icon="times-circle"/>
                </button>

                <button class="btn btn-primary" data-toggle="modal"
                        data-target="#editCategoryModal" @click="viewSubCategory(sub_category.id)">
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
    name: "SubCategoryComponent",
    data() {
      return {
        Menu: [],
        Category: [],
        SubCategoryForm: {
          menu_id: '',
          category_id: '',
          name: '',
          slug: '',
          status: ''
        },
        EditSubCategoryForm: {
          id: '',
          menu_id: '',
          category_id: '',
          name: '',
          slug: '',
          status: ''
        },
        AllError: [],
        SubCategoryList: [],
        total_page: 0,
        search_key: '',
        limit: 5,
        limits: limitOption
      }
    },
    watch: {
      'search_key': function () {
        this.GetSubCategory();
      },
      'limit': function () {
        this.GetSubCategory();
      }
    },
    methods: {
      paginate: function (pageNum) {
        const _this = this;
        _this.GetSubCategory(pageNum)
      },
      getMenu: function () {
        const _this = this;
        this.axios.get(basePath + "menu/all_menu")
          .then((response) => {
            _this.Menu = response.data.results;
          })
          .catch((error) => {
            console.log(error)
          })
      },
      getCategory: function () {
        const _this = this;
        this.axios.get(basePath + "category/menu_wise_category/" + _this.SubCategoryForm.menu_id)
          .then((response) => {
            _this.Category = response.data;
          })
          .catch((error) => {
            console.log(error)
          })
      },
      GetSubCategory: function (page = 1) {
        const _this = this;
        this.axios.get(basePath + "subcategory?limit=" + _this.limit + "&page=" + page + "&q=" + _this.search_key)
          .then((response) => {
            _this.SubCategoryList = response.data.results;
            _this.total_page = Math.ceil(response.data.count / _this.limit);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      AddSubCategory: function () {
        const _this = this;
        this.axios.post(basePath + "subcategory/", _this.SubCategoryForm)
          .then((response) => {
            this.$toastr.success('New Sub Category Added Successfully!', 'Success');
            _this.GetSubCategory();
            _this.Reset("demoModal", _this.SubCategoryForm);
          })
          .catch((error) => {
            _this.AllError = error.response.data.errors;
          })
      },
      EditSubCategory: function () {
        const _this = this;
        this.axios.put(basePath + "subcategory/" + _this.EditSubCategoryForm.id, _this.EditSubCategoryForm)
          .then((response) => {
            console.log(response);
            this.$toastr.success('Sub Category Updated Successfully!', 'Success');
            _this.GetCategory();
            _this.Reset("categoryEditModal", _this.EditSubCategoryForm);
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
      viewSubCategory: function (category_id) {
        const _this = this;
        this.axios.get(basePath + "subcategory/" + category_id)
          .then((response) => {
            console.log(response);
            _this.EditSubCategoryForm = response.data;
            _this.EditSubCategoryForm.menu_id = response.data.menu.id;
            _this.EditSubCategoryForm.category_id = response.data.category.id;
            _this.EditSubCategoryForm.status = response.data.status === true ? 1 : 0;
          })
          .catch((error) => {
            console.log(error)
          })
      },
      deleteSubCategory: function (index, sub_category_id) {
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
            this.axios.delete(basePath + "subcategory/delete/" + sub_category_id)
              .then((response) => {
                console.log(response)
                _this.SubCategoryList.splice(index, 1);
                this.$swal.fire('Deleted!', 'Sub Category Deleted Successfully', 'success');
              })
              .catch((error) => {
                console.log(error)
              })
          }
        })
      },
      statusChange: function (sub_category_id) {
        const _this = this;
        this.axios.patch(basePath + "subcategory/status/" + sub_category_id)
          .then((response) => {
            _this.GetCategory();
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
      MakeSubCategorySlug: function (event, is_update = false) {
        const _this = this;
        if (is_update === true) {
          _this.EditSubCategoryForm.slug = this.Slugify(event);
        } else {
          _this.SubCategoryForm.slug = this.Slugify(event);
        }

      }
    },
    created() {
      this.Loader();
      this.getMenu();
      this.GetSubCategory();
    }
  }
</script>

<style scoped>

</style>

<template>
  <div id="menu">
    <button type="button" style="float: right;" class="btn btn-primary" data-toggle="modal" data-target="#demoModal">
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
        AllError: []
      }
    },
    methods: {
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
    }
  }
</script>

<style scoped>

</style>

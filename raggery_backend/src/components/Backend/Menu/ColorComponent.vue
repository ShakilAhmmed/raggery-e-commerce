<template>
  <div id="color">
    <button type="button" class="modal_button btn btn-primary" @click="viewMenu(id='')" data-toggle="modal"
            data-target="#demoModal">
      Create Color
    </button>
    <div class="modal fade" id="demoModal" tabindex="-1" role="dialog" aria-labelledby="demoModalLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="demoModalLabel">Create Color</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="AddColor">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">

                  <div class="form-group">
                    <label for="exampleInputName">Name</label>
                    <input type="text" v-model="ColorForm.name" class="form-control"
                           id="exampleInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputCode">Code</label>
                    <input type="text" v-model="ColorForm.code" class="form-control" >
                    <span class="mt-5 text-danger" v-if="AllError.code" v-text="AllError.code[0]"></span>

                  </div>
                  <div class="form-group">
                    <label for="exampleInputStatus">Status</label>
                    <select id="exampleInputStatus" class="form-control" v-model="ColorForm.status">
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
              <th>Code</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(color,index) in ColorList">
              <th scope="row">{{index+1}}</th>
              <td>{{color.name}}</td>
              <td>{{color.code}}</td>
              <td>
                <span v-if="color.status === true" class="badge badge-pill badge-success mb-1">Active</span>
                <span v-else class="badge badge-pill badge-danger mb-1">Inactive</span>
              </td>
              <td>
                <button class="btn btn-danger" @click="DeleteColor(index,color.id)">
                  <font-awesome-icon icon="trash"/>
                </button>
                <button @click="statusChange(color.id)"
                        :class="color.status === true ? 'btn btn-success' : 'btn btn-warning'">
                  <font-awesome-icon v-if="color.status === true" icon="check-circle"/>
                  <font-awesome-icon v-else icon="times-circle"/>
                </button>


                <button class="btn btn-primary" data-toggle="modal"
                        data-target="#demoModal" @click="viewMenu(color.id)">
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
    name: "ColorComponent",
    data() {
      return {
        ColorForm: {
          id: '',
          name: '',
          code: '',
          status: ''
        },
        AllError: [],
        ColorList: [],
        total_page: 0
      }
    },
    methods: {
      paginate: function (pageNum) {
        const _this = this;
        _this.GetColor(pageNum)
      },
      GetColor: function (page = 1) {
        const _this = this;
        this.axios.get(basePath + "color?page=" + page)
          .then((response) => {
            _this.ColorList = response.data.results;
            _this.total_page = Math.ceil(response.data.count / perPage);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      AddColor: function () {
        const _this = this;
        if(_this.ColorForm.id == ''){
          console.log(_this.ColorForm);
          this.axios.post(basePath + "color/", _this.ColorForm)
          .then((response) => {
          console.log(response)
            this.$toastr.success('New Menu Added Successfully!', 'Success');
            _this.GetColor();
            _this.Reset("demoModal", _this.ColorForm);
          })
          .catch((error) => {
          console.log(error);
              _this.AllError = error.response.data.errors;

          })
        }
        else{

          this.axios.put(basePath + "color/" + _this.ColorForm.id, _this.ColorForm)
          .then((response) => {
            this.$toastr.success('Color Updated Successfully!', 'Success');
            _this.GetColor();
            _this.Reset("demoModal", _this.ColorForm);
          })
          .catch((error) => {
            _this.AllError = error.response.data.errors;
          })

        }
      },
      viewMenu: function (color_pk) {
        const _this = this;
        if(color_pk == ''){

         _this.Reset("demoModal", _this.ColorForm);

        }
        else{
          _this.Reset("demoModal", _this.ColorForm);
          this.axios.get(basePath + "color/" + color_pk)
          .then((response) => {
            _this.ColorForm = response.data;
            _this.ColorForm.status = response.data.status === true ? 1 : 0;
          })
          .catch((error) => {
            console.log(error)
          })
        }
      },
      Reset: function (modal_name, form) {
        const _this = this;
        $("#" + modal_name).modal('hide');
        _this.AllError = [];
        Object.keys(form).forEach(function (key, index) {
          form[key] = '';
        });

      },

      DeleteColor: function (index, color_pk) {
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
            this.axios.delete(basePath + "color/delete/" + color_pk)
              .then((response) => {
                _this.ColorList.splice(index, 1);
                this.$swal.fire('Deleted!', 'Menu Deleted Successfully', 'success');
              })
              .catch((error) => {
                console.log(error.response.data.error)
              })
          }
        })
      },
      statusChange: function (color_pk) {
        const _this = this;
        this.axios.patch(basePath + "color/status/" + color_pk)
          .then((response) => {
            _this.GetColor();
            if (response.data.type === true) {
              this.$toastr.success(response.data.message, 'Success');
            } else {
              this.$toastr.warning(response.data.message, 'Success');
            }
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },


    created() {
      this.Loader();
      this.GetColor();
    }
  }
</script>

<style scoped>

</style>

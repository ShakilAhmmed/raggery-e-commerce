<template>
  <div id="size">
    <button type="button" class="modal_button btn btn-primary" @click="viewSize(id='')" data-toggle="modal"
            data-target="#demoModal">
      Create Size
    </button>
    <div class="modal fade" id="demoModal" tabindex="-1" role="dialog" aria-labelledby="demoModalLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="demoModalLabel">Create Size</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="AddSize">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">
                  <div class="form-group">
                    <label for="exampleInputCode">Name</label>
                    <input type="text" v-model="SizeForm.name" class="form-control"  >
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>

                  </div>    
                  <div class="form-group">
                    <label for="exampleInputStatus">Status</label>
                    <select id="exampleInputStatus" class="form-control" v-model="SizeForm.status">
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
              <th>Status</th>
              <th>Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(size,index) in SizeList">
              <th scope="row">{{index+1}}</th>
              <td>{{size.name}}</td>
              <td>
                <span v-if="size.status === true" class="badge badge-pill badge-success mb-1">Active</span>
                <span v-else class="badge badge-pill badge-danger mb-1">Inactive</span>
              </td>
              <td>
                <button class="btn btn-danger" @click="DeleteSize(index,size.id)">
                  <font-awesome-icon icon="trash"/>
                </button>
                <button @click="statusChange(size.id)"
                        :class="size.status === true ? 'btn btn-success' : 'btn btn-warning'">
                  <font-awesome-icon v-if="size.status === true" icon="check-circle"/>
                  <font-awesome-icon v-else icon="times-circle"/>
                </button>


                <button class="btn btn-primary" data-toggle="modal"
                        data-target="#demoModal" @click="viewSize(size.id)">
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
    name: "SizeComponent",
    data() {
      return {
        SizeForm: {
          id: '',
          name: '',
          status: ''
        },
        AllError: [],
        SizeList: [],
        total_page: 0 
      }
    },
    methods: {
      paginate: function (pageNum) {
        const _this = this;
        _this.GetSize(pageNum)
      },
      GetSize: function (page = 1) {
        const _this = this;
        this.axios.get(basePath + "size?page=" + page)
          .then((response) => {
            _this.SizeList = response.data.results;
            _this.total_page = Math.ceil(response.data.count / perPage);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      AddSize: function () {
        const _this = this;
        if(_this.SizeForm.id == ''){
          console.log(_this.SizeForm);
          this.axios.post(basePath + "size/", _this.SizeForm)
          .then((response) => {
          console.log(response)
            this.$toastr.success('New Menu Added Successfully!', 'Success');
            _this.GetSize();
            _this.Reset("demoModal", _this.SizeForm);
          })
          .catch((error) => {
          console.log(error);
              _this.AllError = error.response.data.errors;

          })
        }
        else{

          this.axios.put(basePath + "size/" + _this.SizeForm.id, _this.SizeForm)
          .then((response) => {
            this.$toastr.success('Size Updated Successfully!', 'Success');
            _this.GetSize();
            _this.Reset("demoModal", _this.SizeForm);
          })
          .catch((error) => {
            _this.AllError = error.response.data.errors;
          })

        }
      },
      viewSize: function (size_pk) {
        const _this = this;
        if(size_pk == ''){

         _this.Reset("demoModal", _this.SizeForm);

        }
        else{
          _this.Reset("demoModal", _this.SizeForm);
          this.axios.get(basePath + "size/" + size_pk)
          .then((response) => {
            _this.SizeForm = response.data;
            _this.SizeForm.status = response.data.status === true ? 1 : 0;
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

      DeleteSize: function (index, size_pk) {
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
            this.axios.delete(basePath + "size/delete/" + size_pk)
              .then((response) => {
                _this.SizeList.splice(index, 1);
                this.$swal.fire('Deleted!', 'Menu Deleted Successfully', 'success');
              })
              .catch((error) => {
                console.log(error.response.data.error)
              })
          }
        })
      },
      statusChange: function (size_pk) {
        const _this = this;
        this.axios.patch(basePath + "size/status/" + size_pk)
          .then((response) => {
            _this.GetSize();
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
      this.GetSize();
    }
  }
</script>

<style scoped>

</style>

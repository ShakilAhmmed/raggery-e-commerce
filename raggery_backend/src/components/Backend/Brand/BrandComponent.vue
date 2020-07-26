<template>
  <div id="brand">
    <button type="button" class="modal_button btn btn-primary" @click="viewBrand(id='')" data-toggle="modal"
            data-target="#demoModal">
      Create Brand
    </button>
    <div class="modal fade" id="demoModal" tabindex="-1" role="dialog" aria-labelledby="demoModalLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="demoModalLabel">Create Brand</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="AddBrand">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">
                  <div class="form-group">
                    <label for="exampleInputCode">Name</label>
                     <input type="text" v-model="BrandForm.name" @keyup="MakeBrandSlug" class="form-control"
                           id="exampleInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>

                  </div>
                  <div class="form-group">
                    <label for="exampleInputCode">Slug</label>
                      <input type="text" v-model="BrandForm.slug" class="form-control" id="exampleInputSlug" readonly>
                    <span class="mt-5 text-danger" v-if="AllError.slug" v-text="AllError.slug[0]"></span>

                  </div>
                  <div class="form-group">
                    <label for="exampleInputCode">Contact</label>
                    <input type="text" v-model="BrandForm.contact_p" class="form-control"  >
                    <span class="mt-5 text-danger" v-if="AllError.contact_p" v-text="AllError.contact_p[0]"></span>

                  </div>
                  <div class="form-group">
                    <label for="exampleInputCode">Address</label>
                    <textarea  v-model="BrandForm.address" class="form-control"  cols="4" rows="4"></textarea>
                    <span class="mt-5 text-danger" v-if="AllError.address" v-text="AllError.address[0]"></span>

                  </div>                                   
                  <div class="form-group">
                    <label for="exampleInputStatus">Status</label>
                    <select id="exampleInputStatus" class="form-control" v-model="BrandForm.status">
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
              <th>Contact</th>
              <th>Address</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(brand,index) in BrandList">
              <th scope="row">{{index+1}}</th>
              <td>{{brand.name}}</td>
              <td>{{brand.slug}}</td>
              <td>{{brand.contact_p}}</td>
              <td>{{brand.address}}</td>
              <td>
                <span v-if="brand.status === true" class="badge badge-pill badge-success mb-1">Active</span>
                <span v-else class="badge badge-pill badge-danger mb-1">Inactive</span>
              </td>
              <td>
                <button class="btn btn-danger" @click="DeleteBrand(index,brand.id)">
                  <font-awesome-icon icon="trash"/>
                </button>
                <button @click="statusChange(brand.id)"
                        :class="brand.status === true ? 'btn btn-success' : 'btn btn-warning'">
                  <font-awesome-icon v-if="brand.status === true" icon="check-circle"/>
                  <font-awesome-icon v-else icon="times-circle"/>
                </button>


                <button class="btn btn-primary" data-toggle="modal"
                        data-target="#demoModal" @click="viewBrand(brand.id)">
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
    name: "BrandComponent",
    data() {
      return {
        BrandForm: {
          id: '',
          name: '',
          slug: '',
          contact_p: '',
          address: '',
          status: ''
        },
        AllError: [],
        BrandList: [],
        total_page: 0 
      }
    },
    methods: {

      paginate: function (pageNum) {
        const _this = this;
        _this.GetBrand(pageNum)
      },
     
      GetBrand: function (page = 1) {
        const _this = this;
        this.axios.get(basePath + "brand?page=" + page)
          .then((response) => {
            _this.BrandList = response.data.results;
            _this.total_page = Math.ceil(response.data.count / perPage);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      AddBrand: function () {
        const _this = this;
        if(_this.BrandForm.id == ''){
          console.log(_this.BrandForm);
          this.axios.post(basePath + "brand/", _this.BrandForm)
          .then((response) => {
          console.log(response)
            this.$toastr.success('New Menu Added Successfully!', 'Success');
            _this.GetBrand();
            _this.Reset("demoModal", _this.BrandForm);
          })
          .catch((error) => {
          console.log(error);
              _this.AllError = error.response.data.errors;

          })
        }
        else{

          this.axios.put(basePath + "brand/" + _this.BrandForm.id, _this.BrandForm)
          .then((response) => {
            this.$toastr.success('Brand Updated Successfully!', 'Success');
            _this.GetBrand();
            _this.Reset("demoModal", _this.BrandForm);
          })
          .catch((error) => {
            _this.AllError = error.response.data.errors;
          })

        }
      },
      viewBrand: function (brand_pk) {
        const _this = this;
        if(brand_pk == ''){

         _this.Reset("demoModal", _this.BrandForm);

        }
        else{
          _this.Reset("demoModal", _this.BrandForm);
          this.axios.get(basePath + "brand/" + brand_pk)
          .then((response) => {
            _this.BrandForm = response.data;
            _this.BrandForm.status = response.data.status === true ? 1 : 0;
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

      DeleteBrand: function (index, brand_pk) {
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
            this.axios.delete(basePath + "brand/delete/" + brand_pk)
              .then((response) => {
                _this.BrandList.splice(index, 1);
                this.$swal.fire('Deleted!', 'Menu Deleted Successfully', 'success');
              })
              .catch((error) => {
                console.log(error.response.data.error)
              })
          }
        })
      },
      statusChange: function (brand_pk) {
        const _this = this;
        this.axios.patch(basePath + "brand/status/" + brand_pk)
          .then((response) => {
            _this.GetBrand();
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
      MakeBrandSlug: function (event) {
        const _this = this;
        if (_this.BrandForm.id != '') {
          _this.BrandForm.slug = this.Slugify(event);
        } else {
          _this.BrandForm.slug = this.Slugify(event);
        }

      }

    },

    created() {
      this.Loader();
      this.GetBrand();
    }
  }
</script>

<style scoped>

</style>

<template>
  <div id="menu">
    <button type="button" class="modal_button btn btn-primary" data-toggle="modal"
            data-target="#demoModal">
      Create District
    </button>
    <div class="modal fade" id="demoModal" tabindex="-1" role="dialog" aria-labelledby="demoModalLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="demoModalLabel">Create District</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="AddDistrict">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">

                  <div class="form-group">
                    <label for="exampleInputDivision">Division</label>
                    <select type="text" v-model="DistrictForm.division_id" class="form-control"
                            id="exampleInputDivision">
                      <option disabled selected>--Select--</option>
                      <option v-for="(division,index) in DivisionList" :value="division.id">{{division.name}}</option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.division_id" v-text="AllError.division_id[0]"></span>
                  </div>

                  <div class="form-group">
                    <label for="exampleInputName">Name</label>
                    <input type="text" v-model="DistrictForm.name" @keyup="MakeDistrictSlug" class="form-control"
                           id="exampleInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputSlug">Slug</label>
                    <input type="text" v-model="DistrictForm.slug" class="form-control" id="exampleInputSlug" readonly>
                    <span class="mt-5 text-danger" v-if="AllError.slug" v-text="AllError.slug[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputStatus">Is Coverage?</label>
                    <select id="exampleInputStatus" class="form-control" v-model="DistrictForm.is_coverage_area">
                      <option value="" selected disabled>Select</option>
                      <option value="1">Yes</option>
                      <option value="0">No</option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.is_coverage_area"
                          v-text="AllError.is_coverage_area[0]"></span>
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
            <h5 class="modal-title" id="menuEditLabel">Edit District</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="EditDistrict">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">

                  <div class="form-group">
                    <label for="editInputDivision">Division</label>
                    <select type="text" v-model="EditDistrictForm.division_id" class="form-control"
                            id="editInputDivision">
                      <option disabled selected>--Select--</option>
                      <option v-for="(division,index) in DivisionList" :value="division.id">{{division.name}}</option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.division_id" v-text="AllError.division_id[0]"></span>
                  </div>

                  <div class="form-group">
                    <label for="editInputName">Name</label>
                    <input type="text" v-model="EditDistrictForm.name" @keyup="MakeDistrictSlug($event,true)"
                           class="form-control"
                           id="editInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="editInputSlug">Slug</label>
                    <input type="text" v-model="EditDistrictForm.slug" class="form-control" id="editInputSlug" readonly>
                    <span class="mt-5 text-danger" v-if="AllError.slug" v-text="AllError.slug[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="editInputStatus">Is Coverage?</label>
                    <select id="editInputStatus" class="form-control" v-model="EditDistrictForm.is_coverage_area">
                      <option value="" disabled>Select</option>
                      <option value="1">Yes</option>
                      <option value="0">No</option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.is_coverage_area"
                          v-text="AllError.is_coverage_area[0]"></span>
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
              <th>Division</th>
              <th>Name</th>
              <th>Slug</th>
              <th>Is Coverage</th>
              <th>Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(district,index) in DistrictList">
              <th scope="row">{{index+1}}</th>
              <td>{{district.division.name}}</td>
              <td>{{district.name}}</td>
              <td>{{district.slug}}</td>
              <td>
                <span v-if="district.is_coverage_area === true" class="badge badge-pill badge-success mb-1">Coverage Area</span>
                <span v-else class="badge badge-pill badge-danger mb-1">Not Coverage Area</span>
              </td>
              <td>
                <button class="btn btn-danger" @click="deleteDistrict(index,district.id)">
                  <font-awesome-icon icon="trash"/>
                </button>

                <button class="btn btn-primary" data-toggle="modal"
                        data-target="#menuEditModal" @click="viewDistrict(district.id)">
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
    name: "DistrictComponent",
    data() {
      return {
        DistrictForm: {
          division_id: '',
          name: '',
          slug: '',
          is_coverage_area: ''
        },
        EditDistrictForm: {
          id: '',
          division_id: '',
          name: '',
          slug: '',
          is_coverage_area: ''
        },
        AllError: [],
        DivisionList: [],
        DistrictList: [],
        total_page: 0,
        search_key: '',
        limit: 5,
        limits: limitOption
      }
    },
    watch: {
      'search_key': function () {
        this.GetDistrict();
      },
      'limit': function () {
        this.GetDistrict();
      }
    },
    methods: {
      paginate: function (pageNum) {
        const _this = this;
        _this.GetDistrict(pageNum)
      },
      GetDistrict: function (page = 1) {
        const _this = this;
        this.axios.get(basePath + "address/district?limit=" + _this.limit + "&page=" + page + "&q=" + _this.search_key)
          .then((response) => {
            _this.DistrictList = response.data.results;
            _this.total_page = Math.ceil(response.data.count / _this.limit);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      AddDistrict: function () {
        const _this = this;
        this.axios.post(basePath + "address/district/", _this.DistrictForm)
          .then((response) => {
            this.$toastr.success('New District Added Successfully!', 'Success');
            _this.GetDistrict();
            _this.Reset("demoModal", _this.DistrictForm);
          })
          .catch((error) => {
            _this.AllError = error.response.data.errors;
          })
      },
      EditDistrict: function () {
        const _this = this;
        this.axios.put(basePath + "address/district/" + _this.EditDistrictForm.id, _this.EditDistrictForm)
          .then((response) => {
            console.log(response);
            this.$toastr.success('District Updated Successfully!', 'Success');
            _this.GetDistrict();
            _this.Reset("menuEditModal", _this.EditDistrictForm);
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
      viewDistrict: function (district_id) {
        const _this = this;
        this.axios.get(basePath + "address/district/" + district_id)
          .then((response) => {
            _this.EditDistrictForm = response.data;
            _this.EditDistrictForm.division_id = response.data.division.id;
            _this.EditDistrictForm.is_coverage_area = response.data.is_coverage_area === true ? 1 : 0;
          })
          .catch((error) => {
            console.log(error)
          })
      },
      deleteDistrict: function (index, district_id) {
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
            this.axios.delete(basePath + "address/district/" + district_id)
              .then((response) => {
                console.log(response)
                _this.DistrictList.splice(index, 1);
                this.$swal.fire('Deleted!', 'District Deleted Successfully', 'success');
              })
              .catch((error) => {
                console.log(error)
              })
          }
        })
      },
      MakeDistrictSlug: function (event, is_update = false) {
        const _this = this;
        if (is_update === true) {
          _this.EditDistrictForm.slug = this.Slugify(event);
        } else {
          _this.DistrictForm.slug = this.Slugify(event);
        }
      },
      getDivision: function () {
        const _this = this;
        this.axios.get(basePath + "address/all_division")
          .then((response) => {
            _this.DivisionList = response.data.results;
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },
    created() {
      this.Loader();
      this.getDivision();
      this.GetDistrict();
    }
  }
</script>

<style scoped>

</style>

<template>
  <div id="menu">
    <button type="button" class="modal_button btn btn-primary" data-toggle="modal"
            data-target="#demoModal">
      Create Sub District
    </button>
    <div class="modal fade" id="demoModal" tabindex="-1" role="dialog" aria-labelledby="demoModalLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="demoModalLabel">Create Sub District</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="AddSubDistrict">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">

                  <div class="form-group">
                    <label for="exampleInputDivision">Division</label>
                    <select type="text" v-model="SubDistrictForm.division_id" @change="getDistrict" class="form-control"
                            id="exampleInputDivision">
                      <option disabled selected>--Select--</option>
                      <option v-for="(division,index) in DivisionList" :value="division.id">{{division.name}}</option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.division_id" v-text="AllError.division_id[0]"></span>
                  </div>

                  <div class="form-group">
                    <label for="exampleInputDistrict">District</label>
                    <select type="text" v-model="SubDistrictForm.district_id" class="form-control"
                            id="exampleInputDistrict">
                      <option disabled selected>--Select--</option>
                      <option v-for="(district,index) in DistrictList" :value="district.id">{{district.name}}</option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.district_id" v-text="AllError.district_id[0]"></span>
                  </div>

                  <div class="form-group">
                    <label for="exampleInputName">Name</label>
                    <input type="text" v-model="SubDistrictForm.name" @keyup="MakeSubDistrictSlug" class="form-control"
                           id="exampleInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputSlug">Slug</label>
                    <input type="text" v-model="SubDistrictForm.slug" class="form-control" id="exampleInputSlug"
                           readonly>
                    <span class="mt-5 text-danger" v-if="AllError.slug" v-text="AllError.slug[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="exampleInputStatus">Is Coverage?</label>
                    <select id="exampleInputStatus" class="form-control" v-model="SubDistrictForm.is_coverage_area">
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
            <h5 class="modal-title" id="menuEditLabel">Edit Sub District</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
          </div>
          <form class="forms-sample" @submit.prevent="EditSubDistrict">
            <div class="modal-body">
              <div class="card">
                <div class="card-body">

                  <div class="form-group">
                    <label for="editInputDivision">Division</label>
                    <select type="text" v-model="EditSubDistrictForm.division_id" @change="getDistrict(true)"
                            class="form-control"
                            id="editInputDivision">
                      <option disabled selected>--Select--</option>
                      <option v-for="(division,index) in DivisionList" :value="division.id">{{division.name}}</option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.division_id" v-text="AllError.division_id[0]"></span>
                  </div>

                  <div class="form-group">
                    <label for="editInputDistrict">District</label>
                    <select type="text" v-model="EditSubDistrictForm.district_id" class="form-control"
                            id="editInputDistrict">
                      <option disabled selected>--Select--</option>
                      <option v-for="(district,index) in DistrictList" :value="district.id">{{district.name}}</option>
                    </select>
                    <span class="mt-5 text-danger" v-if="AllError.district_id" v-text="AllError.district_id[0]"></span>
                  </div>

                  <div class="form-group">
                    <label for="editInputName">Name</label>
                    <input type="text" v-model="EditSubDistrictForm.name" @keyup="MakeSubDistrictSlug($event,true)"
                           class="form-control"
                           id="editInputName">
                    <span class="mt-5 text-danger" v-if="AllError.name" v-text="AllError.name[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="editInputSlug">Slug</label>
                    <input type="text" v-model="EditSubDistrictForm.slug" class="form-control" id="editInputSlug"
                           readonly>
                    <span class="mt-5 text-danger" v-if="AllError.slug" v-text="AllError.slug[0]"></span>
                  </div>
                  <div class="form-group">
                    <label for="editInputStatus">Is Coverage?</label>
                    <select id="editInputStatus" class="form-control" v-model="EditSubDistrictForm.is_coverage_area">
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
              <th>District</th>
              <th>Name</th>
              <th>Slug</th>
              <th>Is Coverage</th>
              <th>Action</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(sub_district,index) in SubDistrictList">
              <th scope="row">{{index+1}}</th>
              <td>{{sub_district.division.name}}</td>
              <td>{{sub_district.district.name}}</td>
              <td>{{sub_district.name}}</td>
              <td>{{sub_district.slug}}</td>
              <td>
                <span v-if="sub_district.is_coverage_area === true" class="badge badge-pill badge-success mb-1">Coverage Area</span>
                <span v-else class="badge badge-pill badge-danger mb-1">Not Coverage Area</span>
              </td>
              <td>
                <button class="btn btn-danger" @click="deleteSubDistrict(index,sub_district.id)">
                  <font-awesome-icon icon="trash"/>
                </button>

                  <button @click="statusChange(sub_district.id)"
                        :class="sub_district.is_coverage_area === true ? 'btn btn-success' : 'btn btn-warning'">
                  <font-awesome-icon v-if="sub_district.is_coverage_area === true" icon="check-circle"/>
                  <font-awesome-icon v-else icon="times-circle"/>
                </button>

                <button class="btn btn-primary" data-toggle="modal"
                        data-target="#menuEditModal" @click="viewSubDistrict(sub_district.id)">
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
        SubDistrictForm: {
          division_id: '',
          district_id: '',
          name: '',
          slug: '',
          is_coverage_area: ''
        },
        EditSubDistrictForm: {
          id: '',
          division_id: '',
          district_id: '',
          name: '',
          slug: '',
          is_coverage_area: ''
        },
        AllError: [],
        DivisionList: [],
        DistrictList: [],
        SubDistrictList: [],
        total_page: 0,
        search_key: '',
        limit: 5,
        limits: limitOption
      }
    },
    watch: {
      'search_key': function () {
        this.GetSubDistrict();
      },
      'limit': function () {
        this.GetSubDistrict();
      }
    },
    methods: {
      paginate: function (pageNum) {
        const _this = this;
        _this.GetSubDistrict(pageNum)
      },
      GetSubDistrict: function (page = 1) {
        const _this = this;
        this.axios.get(basePath + "address/sub_district?limit=" + _this.limit + "&page=" + page + "&q=" + _this.search_key)
          .then((response) => {
            _this.SubDistrictList = response.data.results;
            _this.total_page = Math.ceil(response.data.count / _this.limit);
          })
          .catch((error) => {
            console.log(error)
          })
      },
      AddSubDistrict: function () {
        const _this = this;
        this.axios.post(basePath + "address/sub_district/", _this.SubDistrictForm)
          .then((response) => {
            this.$toastr.success('New Sub District Added Successfully!', 'Success');
            _this.GetSubDistrict();
            _this.Reset("demoModal", _this.SubDistrictForm);
          })
          .catch((error) => {
            _this.AllError = error.response.data.errors;
          })
      },
      EditSubDistrict: function () {
        const _this = this;
        this.axios.put(basePath + "address/sub_district/" + _this.EditSubDistrictForm.id, _this.EditSubDistrictForm)
          .then((response) => {
            console.log(response);
            this.$toastr.success('Sub District Updated Successfully!', 'Success');
            _this.GetSubDistrict();
            _this.Reset("menuEditModal", _this.EditSubDistrictForm);
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
      viewSubDistrict: function (sub_district_id) {
        const _this = this;
        this.axios.get(basePath + "address/sub_district/" + sub_district_id)
          .then((response) => {
            console.log(response)
            _this.EditSubDistrictForm = response.data;
            _this.EditSubDistrictForm.division_id = response.data.division.id;
            _this.getDistrict(true);
            _this.EditSubDistrictForm.district_id = response.data.district.id;
            _this.EditSubDistrictForm.is_coverage_area = response.data.is_coverage_area === true ? 1 : 0;
          })
          .catch((error) => {
            console.log(error)
          })
      },
      deleteSubDistrict: function (index, sub_district_id) {
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
            this.axios.delete(basePath + "address/sub_district/" + sub_district_id)
              .then((response) => {
                console.log(response)
                _this.SubDistrictList.splice(index, 1);
                this.$swal.fire('Deleted!', 'Sub District Deleted Successfully', 'success');
              })
              .catch((error) => {
                console.log(error)
              })
          }
        })
      },
      statusChange: function (sub_division_id) {
        const _this = this;
        this.axios.patch(basePath + "address/sub_district/status/" + sub_division_id)
          .then((response) => {
            _this.GetSubDistrict();
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
      MakeSubDistrictSlug: function (event, is_update = false) {
        const _this = this;
        if (is_update === true) {
          _this.EditSubDistrictForm.slug = this.Slugify(event);
        } else {
          _this.SubDistrictForm.slug = this.Slugify(event);
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
      },
      getDistrict: function (is_update = false) {
        const _this = this;
        let column = is_update === true ? _this.EditSubDistrictForm.division_id : _this.SubDistrictForm.division_id;
        this.axios.get(basePath + "address/division_wise_district/" + column)
          .then((response) => {
            _this.DistrictList = response.data.results;
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },
    created() {
      this.Loader();
      this.getDivision();
      this.GetSubDistrict();
    }
  }
</script>

<style scoped>

</style>

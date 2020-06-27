<template>
  <div id="page-head">
    <div class="page-header">
      <div class="row align-items-end">
        <div class="col-lg-8">
          <div class="page-header-title">
            <i class="ik ik-box bg-blue"></i>
            <div class="d-inline">
              <h5>{{ $route.meta.page_title }}</h5>
              <p>{{ $route.meta.page_description }}</p>
            </div>
          </div>
        </div>
        <div class="col-lg-4">
          <nav class="breadcrumb-container" aria-label="breadcrumb">
            <ol class="breadcrumb">
              <li class="breadcrumb-item">
                <router-link to="/"><i class="ik ik-home"></i></router-link>
              </li>
              <li class="breadcrumb-item">
                <a href="#">{{ $route.meta.menu }}</a>
              </li>
              <li class="breadcrumb-item active" aria-current="page">{{ $route.meta.page_title }}</li>
            </ol>
          </nav>
        </div>
      </div>
      <hr>
    </div>
  </div>
</template>
<script>
  export default {
    name: "PageHeader",
    data() {
        return {
            pageTitle : '',
            menu:''
        }
    },
    created() {
    }
  }
</script>

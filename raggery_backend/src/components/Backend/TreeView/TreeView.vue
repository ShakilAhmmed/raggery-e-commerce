<template>
  <div id="TreeView">
    <div v-for="(menu,index) in Menu">
      <p>
        <font-awesome-icon icon="cube"/> &nbsp; {{menu.name}} &nbsp;
        <span class="click" style="color: #f5d909" @click="current_category_index = index"
              v-if="current_category_index === index"><font-awesome-icon icon="folder-open"/></span>
        <span class="click" style="color: #f5d909" @click="current_category_index = index" v-else><font-awesome-icon
          icon="folder"/></span>
      </p>
      <div v-for="(category,cat_index) in Category"
           v-if="menu.id === category.menu.id && current_category_index === index" style="margin-left: 5%">
        <p>
          <font-awesome-icon icon="cube"/> &nbsp; {{category.name}} &nbsp;
          <span class="click" @click="current_sub_category_index = cat_index"
                v-if="current_sub_category_index === cat_index" style="color: #f5d909"><font-awesome-icon
            icon="folder-open"/></span>
          <span class="click" @click="current_sub_category_index = cat_index" v-else style="color: #f5d909"><font-awesome-icon
            icon="folder"/></span>
        </p>
        <div v-for="(sub_category,sub_index) in SubCategory"
             v-if="category.id === sub_category.category.id && current_sub_category_index === cat_index"
             style="margin-left: 5%">
          <p>
            <font-awesome-icon icon="cube"/> &nbsp; {{sub_category.name}}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "TreeView",
    data() {
      return {
        Menu: [],
        Category: [],
        SubCategory: [],
        current_category_index: -1,
        current_sub_category_index: -1,
      }
    },
    methods: {
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
        this.axios.get(basePath + "category/all_category")
          .then((response) => {
            _this.Category = response.data.results;
          })
          .catch((error) => {
            console.log(error)
          })
      },
      getSubCategory: function () {
        const _this = this;
        this.axios.get(basePath + "subcategory/all_sub_category")
          .then((response) => {
            _this.SubCategory = response.data.results;
          })
          .catch((error) => {
            console.log(error)
          })
      },

    },
    created() {
      this.getMenu();
      this.getCategory();
      this.getSubCategory();
    }
  }
</script>

<style scoped>
  .click {
    cursor: pointer;
  }

  #TreeView {
    background: #fffcfc;
    padding: 2%;
  }
</style>

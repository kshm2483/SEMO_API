<template>
<div>
  <Sidebar>
      <template v-slot:title>
        <h2>{{ sideBarItems[0].title }}</h2>
      </template>
      <template v-slot:list>
        <li v-for="(item, index) in sideBarItems.slice(2, sideBarItems.length)" :key="index" @click="formFilter(item.id)">{{ item.name }}</li>
      </template>
    </Sidebar>

  <div class="apiDetail">
    <div class="listDetail-content">

      <div v-show="loadSpinner" class="lds-detail">
        <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
      </div>

      <div class="listDetail">
        <APIDetailTop/>
      </div>

      <div class="listDetail">
        <APIDetailMiddle/>
      </div>

      <div class="listDetail listDetail-tall">
        <APIDetailBottom/>
      </div>

    </div>
    <div class="listDetail-ad">
    </div>
  </div>
  <div>
    <div class="btn btn-save btn-save-2 btn--primary" @click="goList">
      <fa-icon icon="angle-left" style="z-index: 2;"></fa-icon>
    </div>
  </div>
</div>
</template>

<script>
import APIDetailTop from './APIDetailTop'
import APIDetailMiddle from './APIDetailMiddle'
import APIDetailBottom from './APIDetailBottom'

import APIListCard from './APIListCard'
import Sidebar from "@/components/sidebar"

export default {
  name: 'APIDetail',
  components: {
    APIDetailTop,
    APIDetailMiddle,
    APIDetailBottom,
    APIListCard,
    Sidebar
  },
  data: () => {
    return {
      loadSpinner: true,
      apiRecommend: [1, 2, 3],
      sideBarItems : [
        {title : 'API Detail'},
        {subtitle : ''},
        {name: 'API Category', id:1},
        {name: 'API Introduce', id:2},
        {name: 'How to use', id:3},
        {name: 'Dev Guide', id:4},
        {name: 'Parameters', id:6},
        {name: 'Responses', id:7},
      ],
    }
  },
  watch: {
    loadSpinner() {
      if (this.loadSpinner) {
        document.body.style.overflowY = 'hidden'
      }
      document.body.style.overflowY = 'auto'
    }
  },
  mounted() {
    document.body.style.overflowX = 'hidden'
    document.body.style.overflowY = 'hidden'
    this.loadData()
  },
  methods: {
    goList() {
      this.$router.go(-1)
      this.$emit('goList')
    },
    loadData() {
      setTimeout(() => {
        this.loadSpinner = false
      }, 1000);
    }
  }
}
</script>

<style lang="scss" scoped>
.btn {
  &-save {
    position: fixed;
    bottom: 50px;
    right: 75px;
    font-size: 50px;
    &-1 {
      right: 150px;
    }
    &-2 {
      width: 42px;
    }
  }
}
</style>

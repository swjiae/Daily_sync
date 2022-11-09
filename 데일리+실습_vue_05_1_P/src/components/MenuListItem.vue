<template>
  <div>
    <div 
    class="menu-div-tag"
    @click="changeMenuSelected"
    :class="{ 'change-selected': menu.selected }"
    >
      <img :src=menu.image>
      <div>{{ menu.title }}</div>
      <div>{{ menu.price }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    changeMenuSelected() {
      this.$store.dispatch('changeMenuSelected', this.menu)
    }
  }
}
</script>

<style>
  .menu-div-tag > img {
    width: 100px;
    height: 100px;
    border-radius: 10px;
  }
  .change-selected {
    background-color: #42936C;
    color: white;
  }
</style>
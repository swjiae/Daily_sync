<template>
  <div>
    <div
      @click="changeSizeSelected"
      :class="{ 'change-selected': size.selected }"
    >
      {{ size.name }}
      {{ size.price }}원
    </div>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    changeSizeSelected() {
      this.$store.dispatch('changeSizeSelected', this.size)
    }
  }
}
</script>

<style>

</style>
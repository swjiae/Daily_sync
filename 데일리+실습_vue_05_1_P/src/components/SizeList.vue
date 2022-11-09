<template>
  <div>
    <h1>2. 사이즈를 고르세요.</h1>
    <SizeListItem
      v-for="(size, index) in sizeList"
      :key="index"
      :size="size"
    />
  </div>
</template>

<script>
import SizeListItem from '@/components/SizeListItem'

export default {
  name: 'SizeList',
  components: {
    SizeListItem,
  },
  computed: {
    sizeList() {
      return this.$store.state.sizeList
    },
  },
  // methods: {
  //   onSelectMenu: function () {},
  // },
}
</script>

<style>
</style>
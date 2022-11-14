<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <div>
      <MenuList class="app-list"/>
      <SizeList class="app-list"/>
      <OptionList class="app-list"/>
    </div>
    <button
      @click="cartIn"
    >장바구니 담기</button>
    <OrderList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OptionList from '@/components/OptionList'
import OrderList from '@/components/OrderList'


export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OptionList,
    OrderList,
  },
  methods: {
    cartIn() {
      this.$store.dispatch('cartIn')
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}

</style>

<template>
  <div>
    <h1>주문 내역</h1>
    <h3>총 {{totalOrderCount}}건: {{totalOrderPrice}}원</h3>
    <OrderListItem
      v-for="(order, index) in orderList"
      :key="index"
      :order="order"
    />
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'

export default {
  name: 'OrderList',
  components: {
    OrderListItem,
  },
  computed: {
    orderList() {
      return this.$store.state.orderList
    },
    totalOrderCount() {
      return this.$store.state.orderList.length
    },
    totalOrderPrice() {
      const total = this.$store.state.orderList.reduce((total, order) => {
        return total + order.totalPrice
      }, 0)
      return total
    },
  },
}
</script>

<style>
</style>
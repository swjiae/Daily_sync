<template>
  <li>
    <img :src=order.image>
    {{ order.title }}
    사이즈: {{ order.size }}
    가격: {{ order.price }}
    {{ order.option }}
  </li>

</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
}
</script>

<style>
</style>
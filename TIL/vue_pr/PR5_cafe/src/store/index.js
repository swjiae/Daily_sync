import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    menuList: [
      {
        title: 'Americano',
        price: 4000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title: 'CafeLatte',
        price: 4500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?cafelatte'
      },
      {
        title: 'MilkTea',
        price: 4000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?milktea'
      },
    ],
    sizeList: [
      {
        name: 'small',
        price: 500,
        selected: false,
      },
      {
        name: 'medium',
        price: 1000,
        selected: false,
      },
      {
        name: 'large',
        price: 1500,
        selected: false,
      },
    ],
    optionList: [
      {
        name: 'shot',
        price: 500,
        count: 0,
      },
      {
        name: 'vanilla syrup',
        price: 500,
        count: 0,
      },
      {
        name: 'caramel syrup',
        price: 500,
        count: 0,
      },
    ],
    orderList : []
  },
  getters: {
  },
  mutations: {
    INCREASE(state, option) {
      state.optionList.forEach((optionItem) => {
        if (optionItem === option) {
          optionItem.count += 1
        }
      })
    },
    DECREASE(state, option) {
      state.optionList.forEach((optionItem) => {
        if (optionItem.count > 0 && optionItem === option) {
          optionItem.count -= 1
        }
      })
    },
    CHANGE_MENU_SELECTED(state, menu) {
      state.menuList.forEach((menuItem) => {
        if (menuItem === menu) {
          menuItem.selected = !menuItem.selected
        }
      })
    },
    CHANGE_SIZE_SELECTED(state, size) {
      state.sizeList.forEach((sizeItem) => {
        if (sizeItem === size) {
          sizeItem.selected = !sizeItem.selected
        }
      })
    },
    CARTIN(state) {
      const menu = state.menuList.find((menu) => {
        if (menu.selected) {
          menu.selected = !menu.selected
          return menu
        }
      })
      const size = state.sizeList.find((size) => {
        if (size.selected) {
          size.selected = !size.selected
          return size
        }
      })
      const order = {
        title: menu.title,
        size: size.name,
        price: menu.price,
        option: `Shot ${state.optionList[0].count}회|Vanilla syrup ${state.optionList[1].count}회|Caramel syrup ${state.optionList[2].count}회`,
        totalPrice: menu.price + size.price + state.optionList[0].price*state.optionList[0].count + state.optionList[1].price*state.optionList[1].count + state.optionList[2].price*state.optionList[2].count
      }
      state.optionList.forEach((option) => {
        option.count = 0
      })
      state.orderList.push(order)
      
    }
  },
  actions: {
    increase(context, option) {
      context.commit('INCREASE', option)
    },
    decrease(context, option) {
      context.commit('DECREASE', option)
    },
    changeMenuSelected(context, menu) {
      context.commit('CHANGE_MENU_SELECTED', menu)
    },
    changeSizeSelected(context, size) {
      context.commit('CHANGE_SIZE_SELECTED', size)
    },
    cartIn(context) {
      context.commit('CARTIN')
    }
  },
  modules: {
  }
})
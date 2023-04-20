import { createStore } from 'vuex'

export default createStore({
  state: {
    tokennn: '' 
  },
  getters: {
    getTokennn(state){
      return state.tokennn
    }
  },
  mutations: {
    makeToken(state){
      function makeid(length) {
        let result = '';
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        const charactersLength = characters.length;
        let counter = 0;
        while (counter < length) {
          result += characters.charAt(Math.floor(Math.random() * charactersLength));
          counter += 1;
        }
        return result;
      }
      state.tokennn = makeid(20);
    }
  },
  actions: {
  },
  modules: {
  }
})

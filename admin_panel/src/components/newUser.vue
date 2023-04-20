<template>
    <div>
        <form @submit="register">
            <input v-model="name" type="text" placeholder="name">
            <input v-model="email" type="email" placeholder="email">
            <input v-model="password" type="password" placeholder="password">
            <input v-model="username" type="text" placeholder="username">
            <button type="submit">Sign up</button>
        </form>
    </div>

</template>

<script>
// import { newUser } from '@/api/index.js';
// import { registerUser } from '@/api/index.js'
// import 'materialize-css'
// import 'materialize-css/dist/css/materialize.css'
export default {
    data() {
        return {
            name: '',
            email: '',
            password: '',
            username: ''
        }
    },
    methods: {
        // async register(e) {
        //     e.preventDefault()
        //     // registerUser(this.name, this.email, this.password, this.username).then((res) => {
        //     //     this.$router.push('login');
        //     //     console.log(res);
        //     // })
        // }
    }
    // beforeUnmount() {
    //     e.preventDefault()
    //     register(this.name, this.email, this.password, this.username).then((res) => {
    //         this.$router.push('login');
    //         console.log(res);
    //     })
    // }
}
</script>
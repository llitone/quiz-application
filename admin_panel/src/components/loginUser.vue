<template>
    <div>
        <form @submit="login">
            <input v-model="phone" type="text" placeholder="login">
            <input v-model="password" type="password" placeholder="password">
            <button type="submit">Sign in</button>
        </form>
    </div>
</template>

<script>
// import { newUser } from '@/api/index.js';
import { mapMutations, mapGetters } from 'vuex'
import { loginUser } from '@/api/index.js'
// import 'materialize-css'
// import 'materialize-css/dist/css/materialize.css'
export default {
    data() {
        return {
            phone: '',
            password: ''
        }
    },
    computed: {
        ...mapGetters([
            'getTokennn'
        ])
    },
    beforeCreate(){
        if (window.localStorage.jwt != undefined){
            this.$router.push('/posts')
        }
    },
    methods: {
        ...mapMutations([
            'makeToken'
        ]),
        async login(e) {
            e.preventDefault()
            loginUser(this.phone).then((res) => {
                // this.$session.start()
                // this.$session.set('jwt', res.body.token)
                // Vue.http.headers.common['Authorization'] = 'Bearer ' + res.body.token
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
                console.log(res.data);
                console.log(this.password);
                if (res.data.password == this.password){
                    window.localStorage.setItem('jwt', makeid(19) + String(res.data.id))
                    console.log(localStorage);
                    this.$router.push('/posts')
                }
                
                // if (res.data.accessToken) {
                //     localStorage.setItem('user', JSON.stringify(res.data));
                // }
                // const { jwt, user } = res.data
                // window.localStorage.setItem('jwt', jwt)
                // window.localStorage.setItem('userData', JSON.stringify(user))
                // loginUser2(user.phone_number, jwt).then((res2) => {
                //     window.localStorage.setItem('articles', JSON.stringify(res2?.data?.articles || []))
                //     this.$router.push('/')
                //     console.log(res);
                //     console.log(res2);
                // })
            })
        }

    }
}
</script>
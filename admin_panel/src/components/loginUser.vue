<template>
    <div class="login-page">
        <div class="form">
            <form class="login-form" @submit="login">
                <img style="height: 200px; width: 200px; margin-bottom: -50px; margin-top: -50px;" src="https://media.discordapp.net/attachments/787001151353520140/1098749673033969694/Tele2_logo_black.png?width=612&height=612" alt="">
                <h2 class="form-signin-heading">Войдите в аккаунт</h2>
                <input class="form-control" v-model="phone" type="text" placeholder="login">
                <input class="form-control" v-model="password" type="password" placeholder="password">
                <button class="btn btn-lg btn-primary btn-block" type="submit">Войти</button>
            </form>
        </div>
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
        console.log(window.localStorage);
        if (window.localStorage.jwt != undefined){
            this.$router.push('/admin')
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
                if (res.data.password == this.password){
                    window.localStorage.setItem('jwt', makeid(19) + String(res.data.id))
                    this.$router.push('/admin')
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
<style>
@import url(https://fonts.googleapis.com/css?family=Roboto:300);

.login-page {
  width: 360px;
  padding: 8% 0 0;
  margin: auto;
}
.form {
  position: relative;
  z-index: 1;
  background: #FFFFFF;
  max-width: 360px;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
.form input {
  font-family: "Roboto", sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #969896;
  width: 100%;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}
.form button:hover,.form button:active,.form button:focus {
  background: #777977;
}
.form .message {
  margin: 15px 0 0;
  color: #b3b3b3;
  font-size: 12px;
}
.form .message a {
  color: #4CAF50;
  text-decoration: none;
}
.form .register-form {
  display: none;
}
body {
  background: #afb1ae; /* fallback for old browsers */
  background: rgb(174, 175, 174);
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;      
}

</style>
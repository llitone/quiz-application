<template>
    <div class="login-page">
        <div class="form">
            <form @submit="newsbj">
                <img style="height: 200px; width: 200px; margin-bottom: -50px; margin-top: -50px;" src="https://media.discordapp.net/attachments/787001151353520140/1098749673033969694/Tele2_logo_black.png?width=612&height=612" alt="">
                <h2 class="form-signin-heading">Добавьте предмет!</h2>
                <input v-model="subject" type="text" placeholder="предмет">
                <button type="submit">Отправить</button> <br><br>
            </form>
            <button @click="returnHome">Вернуться</button>
        </div>
    </div>

</template>

<script>
import { newSubject } from '@/api/index.js';
// import { registerUser } from '@/api/index.js'
// import 'materialize-css'
// import 'materialize-css/dist/css/materialize.css'
export default {
    data() {
        return {
            subject: ''
        }
    },
    methods: {
        returnHome(){
            this.$router.push('/admin')
        },
        async newsbj(e) {
            e.preventDefault()
            newSubject(this.subject).then((res) =>{
                console.log(res);
                this.$router.push('/admin')  
            })
        }
    },
    beforeCreate() {
        if (window.localStorage.jwt == undefined){
            this.$router.push('/')
        }
    }
}
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Roboto:300);

.login-page {
  width: 450px;
  padding: 8% 0 0;
  margin: auto;
}
.form {
  position: relative;
  z-index: 1;
  background: #FFFFFF;
  max-width: 450px;
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
.form select {
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
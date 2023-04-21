<template>
    <div class="login-page">
        <div class="form">
            <form @submit="newpost">
                <img style="height: 200px; width: 200px; margin-bottom: -50px; margin-top: -50px;" src="https://media.discordapp.net/attachments/787001151353520140/1098749673033969694/Tele2_logo_black.png?width=612&height=612" alt="">
                <h2 class="form-signin-heading">Добавьте вопрос!</h2>
                <input v-model="question" type="text" placeholder="question">
                <input v-model="age" type="text" placeholder="age from 11 to 16">
                <input v-model="explanation" type="text" placeholder="explanation">
                <input v-model="difficulty" type="text" placeholder="difficulty">
                <input v-model="value" type="text" placeholder="value">
                <input v-model="answer1" type="text" placeholder="answer 1">
                <input v-model="answer2" type="text" placeholder="answer 2">
                <input v-model="answer3" type="text" placeholder="answer 3">
                <input v-model="answer4" type="text" placeholder="answer 4">
                <input type="checkbox" id="is_correct1" style="display: block;" v-model="is_correct1"><span>{{ answer1 }}</span>
                <input type="checkbox" id="is_correct2" style="display: block;" v-model="is_correct2"><label for="is_correct2">{{ answer2 }}</label>
                <input type="checkbox" id="is_correct3" style="display: block;" v-model="is_correct3"><label for="is_correct3">{{ answer3 }}</label>
                <input type="checkbox" id="is_correct4" style="display: block;" v-model="is_correct4"><label for="is_correct4">{{ answer4 }}</label>
                <select v-model="subject" style="display: block;">
                    <option value="" selected disabled>Выберите школьный предмет</option>
                    <option value="1">История</option>
                    <option value="2">Математика</option>
                    <option value="3">Физика</option>
                </select>
                <button type="submit">Отправить</button> <br> <br>
            </form>
            <button @click="returnHome">Вернуться</button>
        </div>
    </div>
    
</template>

<script>
import { makenewQuestion, getData, putAnswerstoQuestion } from '@/api/index.js';
// import 'materialize-css'
// import 'materialize-css/dist/css/materialize.css'
export default {
    data() {
        return {
            id: '',
            age: '',
            question: '',
            explanation: '',
            difficulty: '',
            value: '',
            subject: '',
            answer1: '',
            answer2: '',
            answer3: '',
            answer4: '',
            is_correct1: false,
            is_correct2: false,
            is_correct3: false,
            is_correct4: false
        }
    },
    methods: {
        returnHome(){
            this.$router.push('/admin')
        },
        async newpost(e) {
            e.preventDefault()
            let sec = window.localStorage.jwt.slice(19)
            makenewQuestion(Number(this.age), this.question, Number(this.difficulty), Number(this.value), Number(this.subject), this.explanation, Number(sec)).then((res) => {
                console.log(res);
                getData().then((data1) => {
                    let datass = data1.data;
                    for (let i = 0; i < datass.length; i++){
                        for (let j = 0; j < datass[i]['questions'].length; j++){
                            if (datass[i]['questions'][j]['question'] == this.question){
                                this.id = datass[i]['questions'][j]['id']
                            }
                            
                        }
                    }
                    putAnswerstoQuestion(Number(this.id), this.answer1, this.is_correct1)
                    putAnswerstoQuestion(Number(this.id), this.answer2, this.is_correct2)
                    putAnswerstoQuestion(Number(this.id), this.answer3, this.is_correct3)
                    putAnswerstoQuestion(Number(this.id), this.answer4, this.is_correct4).then(() => {
                        this.$router.push('/admin')
                    })
                })
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
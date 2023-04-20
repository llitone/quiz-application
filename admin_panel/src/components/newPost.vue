<template>
    <form @submit="newpost">
        <input v-model="question" type="text" placeholder="question">
        <input v-model="age" type="text" placeholder="age from 11 to 16">
        <input v-model="explanation" type="text" placeholder="explanation">
        <input v-model="difficulty" type="text" placeholder="difficulty">
        <input v-model="value" type="text" placeholder="value">
        <input type="checkbox" style="display: block;" v-model="is_correct1">
        <input v-model="answer1" type="text" placeholder="answer 1">
        <input type="checkbox" style="display: block;" v-model="is_correct2">
        <input v-model="answer2" type="text" placeholder="answer 2">
        <input type="checkbox" style="display: block;" v-model="is_correct3">
        <input v-model="answer3" type="text" placeholder="answer 3">
        <input type="checkbox" style="display: block;" v-model="is_correct4">
        <input v-model="answer4" type="text" placeholder="answer 4">
        <select v-model="subject" style="display: block;">
            <option value="" selected disabled>Выберите школьный предмет</option>
            <option value="1">История</option>
            <option value="2">Математика</option>
            <option value="3">Физика</option>
        </select>
        <button type="submit">Отправить</button>
    </form>
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
        async newpost(e) {
            e.preventDefault()
            let sec = window.localStorage.jwt.slice(19)
            console.log(typeof Number(this.difficulty));
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
                    console.log(this.id);
                    putAnswerstoQuestion(Number(this.id), this.answer1, this.is_correct1).then((ress) => {
                        console.log(ress);
                    })
                    putAnswerstoQuestion(Number(this.id), this.answer2, this.is_correct2).then((ress) => {
                        console.log(ress);
                    })
                    putAnswerstoQuestion(Number(this.id), this.answer3, this.is_correct3).then((ress) => {
                        console.log(ress);
                    })
                    putAnswerstoQuestion(Number(this.id), this.answer4, this.is_correct4).then((ress) => {
                        console.log(ress);
                        this.$router.push('/posts')
                    })
                })
            })
        }
    }
}
</script>

<!-- <style>
div {
    display: flex;
}

.card {
    display: inline;
    width: 300px;
    height: 400px;
}
</style> -->
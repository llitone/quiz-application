<template>
    <div>
        <img style="height: 100px; width: 100px; margin-bottom: -50px; margin-top: -50px;" src="https://media.discordapp.net/attachments/787001151353520140/1098749673033969694/Tele2_logo_black.png?width=612&height=612" alt="">
        <button @click="newQuestion">Добавить вопрос</button>
        <button @click="logout">Выйти из аккаунта</button>
        <button @click="newSubject">Добавить предмет в БД</button>
        <br>
        <br>
    <!-- </div> -->
    <!-- <div> -->
        <table style="width: 95%; margin: auto; border: 1px solid black">
            <tr>
                <th>id</th>
                <th>возраст</th>
                <th>сложность</th>
                <th>очки за correct ответ</th>
                <th>вопрос</th>
                <th>ответы</th>
                <th>объяснение</th>
                <th>id предмета</th>
                <th>delete</th>
            </tr>
            <tr v-for="item in data" :key="item.id" >
                <td>{{ item.id }}</td>
                <td>{{ item.age }}</td>
                <td>{{ item.difficulty }}</td>
                <td>{{ item.value }}</td>
                <td>{{ item.question }}</td>
                <td>
                    <ul v-for="bb in item.answers" :key="bb.id">
                        <li>{{ bb.answer }} | {{ bb.is_correct }}</li>
                    </ul>
                </td>
                <td>{{ item.explanation }}</td>
                <td>{{ item.subject_id }}</td>
                <td><button @click="deleteQuestion(item.id)">Удалить</button></td>
            </tr>
        </table>
    </div>
    
    
</template>

<script>
import { getData, deleteQuestionbyId } from '@/api/index.js';
// import 'materialize-css'
// import 'materialize-css/dist/css/materialize.css'
export default {
    data() {
        return {
            data: {}
        }
    },
    methods: {
        newQuestion(){
            this.$router.push('/new')
        },
        logout(){
            delete(window.localStorage.jwt)
            this.$router.push('/')
        },
        newSubject(){
            this.$router.push('/newsbj')
        },
        deleteQuestion(id){
            deleteQuestionbyId(id).then(() => {
                this.$router.push('/')
            })
        }
    },
    beforeCreate() {
        if (window.localStorage.jwt == undefined){
            this.$router.push('/')
        }
        getData().then((data1) => {
            // let datas = JSON.stringify(data1.data)
            
            let datass = data1.data;
            console.log(datass);
            let datas = [];
            for (let i = 0; i < datass.length; i++){
                console.log(datass[i]);
                // if (data1.data[i])
                for (let j = 0; j < datass[i]['questions'].length; j++){
                    console.log(i, j);
                    // if (data1.data[i]['questions'][j] == undefined) {
                    //     break;
                    // }
                    if (datass[i]['questions'][j]['author_id'] == window.localStorage.jwt.slice(19)){
                        // console.log(datass[i]['questions'][j]);
                        datas.push(datass[i]['questions'][j])
                    }
                    
                }
                // [{"id":1,"questions":[{"age":16,"answers":[{"answer":"гитлер","id":1,"is_correct":true,"question_id":1},{"answer":"настя","id":2,"is_correct":false,"question_id":1},{"answer":"захар","id":3,"is_correct":true,"question_id":1},{"answer":"мама дификульта","id":4,"is_correct":true,"question_id":1}],"author_id":1,"difficulty":1,"explanation":"у гитлера др в этот день","id":1,"question":"у кого др 20 апреля?","subject_id":1,"value":10},{"age":4,"answers":[],"author_id":1,"difficulty":1902378,"explanation":"хз","id":2,"question":"когда родился путин?","subject_id":1,"value":120123213}],"subject":"история"}]
            }
            this.data = {
                ...datas
            }
            // console.log(this.data);
        })
    }
}
</script>

<style>
table {
    background: white;
}
.card{
    display: inline;
    width: 300px;
    height: 400px;
}

td {
    border: 1px solid black;
}

th {
    border: 1px solid black;
}
</style>
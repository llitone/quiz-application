<template>
    <div>
        <button @click="newQuestion">Добавить вопрос</button>
    </div>
    <div>
        <table>
            <tr>
                <th>id</th>
                <th>возраст??</th>
                <th>вопрос</th>
                <th>ответы лол</th>
                <th>объяснение</th>
                <th>delete</th>
            </tr>
            <tr v-for="item in data" :key="item.id" >
                <td>{{ item.id }}</td>
                <td>{{ item.age }}</td>
                <td>{{ item.question }}</td>
                <td>{{ item.answers }} </td>
                <td>{{ item.explanation }}</td>
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
        deleteQuestion(id){
            deleteQuestionbyId(id).then((data) => {
                console.log(data);
                this.$router.push('/')
            })
        }
    },
    beforeCreate() {
        if (window.localStorage.jwt == undefined){
            this.$router.push('/')
        }
        getData().then((data1) => {
            console.log(window.localStorage.jwt.slice(19));
            // let datas = JSON.stringify(data1.data)
            // console.log(datas);
            let datass = data1.data;
            let datas = [];
            for (let i = 0; i < datass.length; i++){
                // console.log(datass[i]);
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
            console.log(datas);
            this.data = {
                ...datas
            }
            // console.log(this.data);
        })
    }
}
</script>

<style>
.card{
    display: inline;
    width: 300px;
    height: 400px;
}
</style>
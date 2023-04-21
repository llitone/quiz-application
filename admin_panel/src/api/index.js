import axios from "axios";
axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';

async function getData() {
    let result = await axios.get('http://d1ffic00lt.com/app/api/v1.0/questions/');
    return result;
}

async function getDataUser(id){
    console.log(id);
    let result = await axios.get('http://localhost:1337/api/articles?populate=users_permissions_user&filters[users_permissions_user][id][$eq]=' + id);
    return result;
}

async function getSubjects(){
    let result = await axios.get('http://d1ffic00lt.com/app/api/v1.0/subjects/');
    return result;
}

// async function registerUser(namee, emaill, passwordd, usernamee){
//     await axios.post(`http://localhost:1337/api/auth/local/register`, {
//         email: emaill,
//         name: namee,
//         password: passwordd,
//         username: usernamee
//     })
//     return 1;
// }

async function loginUser(phone){
    const res = await axios.get(`http://d1ffic00lt.com/app/api/v1.0/authors/${phone}`);
    // {
    //     login: phone,
    //     password: passwordd,
    //     // headers: {
    //     //     'Access-Control-Allow-Methods': 'POST, PUT, PATCH, GET, DELETE, OPTIONS',

    //     //     'Access-Control-Allow-Headers': '*'
    //     // }
    
    return res
}

async function loginUser2(id, jwt){
    const res2 = await axios.get(`http://d1ffic00lt.com/app/api/v1.0/users/${id}`, {
        headers: {
            Authorization: `Bearer ${jwt}`,
        }
    })
    return res2
}

async function makenewQuestion(agee, questionn, difficultyy, valuee, subject, explanationn, author){
    const res = await axios.post('http://d1ffic00lt.com/app/api/v1.0/questions/', {
        age: agee,
        question: questionn,
        difficulty: difficultyy,
        value: valuee,
        subject_id: subject,
        explanation: explanationn,
        author_id: author
    })
    return res
}

async function putAnswerstoQuestion(question, answerr, is_correctt){
    const res = await axios.post('http://d1ffic00lt.com/app/api/v1.0/answers/', {
        question_id: question,
        answer: answerr,
        is_correct: is_correctt
    })
    return res
}

async function deleteQuestionbyId(idd){
    let result = await axios.delete(`http://d1ffic00lt.com/app/api/v1.0/questions/${idd}`);
    return result;
}

async function newSubject(namee){
    console.log(namee);
    const res = await axios.post('http://d1ffic00lt.com/app/api/v1.0/subjects/', {
        name: namee
    })
    return res;
}
// async function getQuestionId(){
//     const res = await axios.post('http://d1ffic00lt.com/app/api/v1.0/questions/');
//     return res
// }

export { getData, getDataUser, loginUser, makenewQuestion, loginUser2, getSubjects, putAnswerstoQuestion, deleteQuestionbyId, newSubject };

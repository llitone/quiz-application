<template>
    <div class="card" v-for="item in data.data.data" :key="item.id">
        <h2>{{ item.attributes.title }}</h2>
        <p>{{ item.attributes.description }}</p>
        <h5>{{ item.attributes.users_permissions_user.data.attributes.username }} | {{ item.attributes.users_permissions_user.data.id }}</h5>
    </div>
</template>

<script>
import {getDataUser} from '@/api';
// import 'materialize-css'
// import 'materialize-css/dist/css/materialize.css'
export default {
    data() {
        return {
            data: {},
            id: 0
        }
    },
    beforeCreate() {
        this.id = this.$route.params.id
        console.log(this.id);
        getDataUser(this.id).then((data1) => {
            this.data = {
                ...data1
            }
        })
    }
}
</script>

<style>
div {
    display: flex;
}

.card {
    display: inline;
    width: 300px;
    height: 400px;
}
</style>
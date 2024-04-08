<template>
    <ul>
        <li>
            <router-link to="/">Garagem</router-link>
        </li>
        <li>
            <router-link to="/categoria">Categorias</router-link>
        </li>
        <li>
            <router-link to="/marca">Marca</router-link>
        </li>
        <li>
            <router-link to="/cor">Cor</router-link>
        </li>
        <li>
            <router-link to="/acessorio">Acessorio</router-link>
        </li>
        <li>
            <router-link to="/veiculo">Veiculo</router-link>
        </li>
        <li v-if="isuserlog"  id="log">{{ username }}
            <ul>
                <li id="logout" @click="logout">logout</li>
            </ul>
        </li>
        <li v-else>
            <router-link to="/auth">login</router-link>
        </li>
    </ul>
</template>
<script setup>
    import { computed } from 'vue'
import { logged } from '../pinia/index'
    const store = logged()

    const isuserlog = computed(() =>{
        return store.showlog
    })
    const username = computed(() =>{
        return store.showuser
    })
    function logout(){
        store.logout()
    }
</script>
<style scoped>
    ul{
        display: flex;
        gap: 20px;
        list-style: none;
        margin-right: 50px;
        font-size: 18px;
    }
    ul li{
        color: gold;
    }
    ul li a{
        text-decoration: none;
        color: gold;
        transition: 0.5s;
    }
    ul li a:hover{
        color: yellow;
    }
    #logout{
        display: none;
        position: relative;
        background-color: gold;
        color: black;
        padding: 10px;
        cursor: pointer;
    }
    #log:hover #logout{
        position: absolute;
        display: block;
    }
</style>
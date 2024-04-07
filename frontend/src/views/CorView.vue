<script setup>
import { onMounted, ref } from "vue";
import CorAPI from '../api/cor'
    const novacor = ref(null)
    const api = new CorAPI()
    const cores = ref(null)
    const msg = ref(null)
    const errormsg = ref(null)
    
    async function enviar(){
        if(novacor.value){
            await api.CriarCor(novacor.value)
            msg.value = "cor enviada"

            setTimeout(() =>{
                msg.value = null
                location.reload()
            }, 2000)
        }
        else{
            errormsg.value = 'preencha o campo corretamente'

            setTimeout(() =>{
                errormsg.value = null
            }, 2000)
        }

    }

    async function excluir(id){
        await api.ExcluirCor(id)

        setTimeout(() =>{
            location.reload()
        }, 500)
    }

    onMounted(async() =>{
       cores.value = await api.ListarCores()
    })
</script>
<template>
<div class="container">
    <div class="msg" v-if="msg">
        <p>{{msg}}</p>
    </div>
    <div class="errormsg" v-if="errormsg">
        <p>{{ errormsg }}</p>
    </div>
    <h1>cor</h1>
    <input type="text" v-model="novacor" placeholder="nova cor"/>  
    <p>nova cor:</p>
    <div :style="{ backgroundColor: novacor }" class="color"></div>
    <button @click="enviar">enviar</button>
    <p>cores:</p>
    <div class="lista">
        <div v-for="cor in cores" :key="cor.id">
        <div :style="{backgroundColor: cor.descricao }"><button @click="excluir(cor.id)">X</button></div>
    </div>
    </div>
</div>  
</template>
<style scoped>
    .color{
        width: 300px;
        height: 50px;
    }
    .container {
        display: flex;
        flex-direction: column;
        gap: 20px;
        justify-content: center;
        align-items: center;
        width: 100%;
      }
      .lista {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
      }
      .lista div{
        border: 1px solid black;
        width: 100px;
        height: 100px;
      }
      .container input {
        width: 300px;
        padding-left: 2px;
        border: none;
        border-bottom: 1px solid black;
        outline: 0;
        padding: 5px;
        font-size: 15px;
      }
      .msg {
        background-color: rgb(1, 255, 141);
        border: 2px solid black;
        display: flex;
        justify-content: center;
        width: 300px;
        padding: 15px;
      }
      .msg p {
        color: black;
      }
      .errormsg{
          background-color: red;
          border: 2px solid black;
          display: flex;
          justify-content: center;
          width: 300px;
          padding: 15px;
        }
        .errormsg p {
          color: black;
        }
        .lista div button{
          width: 25px;
          height: 25px;
          border: none;
          border-radius: 5px ;
        }
</style>
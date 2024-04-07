<script setup>
import { onMounted, ref, watch } from 'vue'
import MarcaAPI from '../api/marca'

const api = new MarcaAPI()
const novamarca = ref(null)
const marcas = ref(null)
const nacionalidade = ref(null)
const msg = ref(null)
const errormsg = ref(null)

async function enviar() {
  if (marcas.value && nacionalidade.value) {
    await api.NovaMarca(novamarca.value, nacionalidade.value)
    msg.value = 'marca enviada com sucesso'

    setTimeout(() => {
      msg.value = null
      location.reload()
    }, 2000)
  } else {
    errormsg.value = "preencha os campos corretamente"

    setTimeout(() =>{
        errormsg.value = null
    }, 2000)
  }
}

async function excluir(id){
   await api.ExcluirMarca(id)

   setTimeout(() =>{
      location.reload()
   }, 500)
}

onMounted(async () => {
  marcas.value = await api.ListarMarcas()
})

watch(marcas, (marca) => {
  console.log(marca)
})
</script>
<template>
  <div class="container">
    <div class="msg" v-if="msg">
      <p>{{ msg }}</p>
    </div>
    <div class="errormsg" v-if="errormsg">
        <p>{{errormsg}}</p>
    </div>
    <h1>marca</h1>
    <input type="text" placeholder="nova marca" v-model="novamarca" />
    <input type="text" placeholder="nacionalidade(opcional)" v-model="nacionalidade" />
    <button @click="enviar">enviar</button>
    <ul class="lista">
      <li v-for="marca in marcas" :key="marca.id">{{ marca.nome }} - {{ marca.nacionalidade }} <button @click="excluir(marca.id)">X</button></li>
    </ul>
  </div>
</template>
<style scoped>
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
  flex-direction: column;
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
  display: flex;
  justify-content: center;
  border: 2px solid black;
  width: 300px;
  padding: 15px;
}
.msg p {
  color: black;
}
.errormsg{
    background-color: red;
    display: flex;
    justify-content: center;
    border: 2px solid black;
    width: 300px;
    padding: 15px;
  }
  .errormsg p {
    color: black;
  }
  li button{
    width: 30px;
    background-color: red;
    color: white;
    height: 30px;
    border: none;
    border-radius: 5px ;
  }
</style>

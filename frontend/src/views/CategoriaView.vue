<script setup>
  import { computed, onMounted, ref, watch } from 'vue'
  import CategoriaAPI from '../api/categoria'
import { logged } from '../pinia'
import UserAPI from '@/api/usuario';
  const categoriaAPI = new CategoriaAPI()
  const novacategoria = ref(null)
  const categorias = ref([])
  const msg = ref(null)
  const msgerror = ref(null)
  const store = logged()
  const usuarioapi = new UserAPI()



  const isuserlogged = computed(() =>{
      return store.showlog
  })
  const usuario = computed(() =>{
      return store.showuser
  })

  const userid = ref(null)

  async function enviar(){
    if(novacategoria.value){
    await categoriaAPI.CriarCategoria(novacategoria.value, userid.value)

    msg.value = "categoria enviada com sucesso"

    setTimeout(() =>{
      msg.value = null
      location.reload()
    },2000)
  }
  else if(!isuserlogged.value){
    msgerror.value = "logue-se para adicionar uma nova categoria"

    setTimeout(() =>{
      msgerror.value = null
    }, 2000)
  }
  else {
    msgerror.value = "preencha o campo "

    setTimeout(() =>{
      msgerror.value = null
    }, 2000)
  }
}
  async function excluir(id){
    await categoriaAPI.ExcluirCategoria(id)

    setTimeout(() =>{
      location.reload()
    }, 500)
  }

  onMounted(async () =>{
    categorias.value = await categoriaAPI.ListarCategoria()
    const apiusuario = await usuarioapi.ListarUsuarios()
    const iduser = apiusuario.find(user => user.username === usuario.value)
    userid.value = iduser.id
  })

  watch(novacategoria, (categoria) =>{
    console.log(categoria)
  })
</script>
<template>
<div class="container">
  <div class="msg" v-if="msg">
    <p>{{msg}}</p>
  </div>
  <div class="errormsg" v-if="msgerror">
    <p>{{msgerror}}</p>
  </div>
  <h1>categorias</h1>
  <input type="text" v-model="novacategoria" id="addcategoria" placeholder="nova categoria">
  <div>
    <button @click="enviar">enviar</button>
  </div>
  <ul class="categorias">
    <li v-for="categoria in categorias" :key="categoria.id">{{categoria.nome}} <button id="exluir" @click="excluir(categoria.id)">X</button></li>
  </ul>
</div>
</template>
<style scoped>
  .container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 20px;
    width: 100%;
    height: 50vh;
  }
  #addcategoria{
    padding-left: 2px ;
    width: 300px;
    padding: 5px;
    font-size: 15px;
    outline: 0;
    border: none;
    border-bottom: 1px solid 
  }
  .categorias{
    display: flex;
    flex-direction: column;
    list-style: none;
    gap: 20px;
    font-size: 20px;
  }
  .msg{
    background-color: rgb(1, 255, 141);
    display: flex;
    justify-content: center;
    border: 2px solid black;
    width: 300px;
    padding: 15px;
  }
  .msg p{
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
</style>

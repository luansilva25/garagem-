<script setup>
import CategoriaAPI from '../api/categoria'
import CorAPI from '../api/cor'
import MarcaAPI from '../api/marca'
import AcessoriosAPI from '../api/acessorios'
import { onMounted, reactive, ref, watch } from 'vue'
const Corapi = new CorAPI()
const Categoriaapi = new CategoriaAPI()
const Marcaapi = new MarcaAPI()
const Acessorioapi = new AcessoriosAPI()

const cores = ref(null)
const marcas = ref(null)
const acessorios = ref(null)
const categorias = ref(null)

const corselecionada = ref(null)
const marcaselecionada = ref(null)
const acessoriosselecionados = ref([])
const categoriaselecionada = ref(null)
const nome = ref(null)
const image = reactive({
    car: null
})

function alterarimagem(e){
  const target = e.target

  if(target && target.files){
    const files = target.files[0]
    image.car = URL.createObjectURL(files)
  }
}


onMounted(async () => {
  cores.value = await Corapi.ListarCores()
  marcas.value = await Marcaapi.ListarMarcas()
  acessorios.value = await Acessorioapi.ListarAcessorios()
  categorias.value = await Categoriaapi.ListarCategoria()
})
watch(acessoriosselecionados, (acessorios) => {
  console.log(acessorios)
})
</script>
<template>
  <div class="container">
    <h1>veiculos</h1>
    <div id="imagem">
        <p>imagem </p>
        <input type="file" @change="alterarimagem($event)">
        <img :src="image.car">
    <div>
        <input type="text" placeholder="nome" v-model="nome">
        <input type="number" placeholder="preco">
        <input type="number" placeholder="ano" >
    </div>
      <div id="cor">
        <select name="" id="" v-model="corselecionada">
          <option v-for="cor in cores" :key="cor.id" >{{ cor.descricao }}</option>
        </select>
        <div :style="{backgroundColor: corselecionada}"></div>
      </div>
      <div>
        <select name="" id="" v-model="marcaselecionada">
          <option v-for="marca in marcas" :key="marca.id">{{ marca.nome }}</option>
        </select>
      </div>
      <div>
        <select name="" id="" v-model="categoriaselecionada">
          <option v-for="categoria in categorias" :key="categoria.id">{{ categoria.nome }}</option>
        </select>
      </div>
      <div>
        <select name="" id="acessorios" multiple v-model="acessoriosselecionados">
          <option v-for="acessorio in acessorios" :key="acessorio.id" >
            {{ acessorio.descricao }}
          </option>
        </select>
      </div>
    </div>
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
    height: 100vh;
  }
  .container div{
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .container div select{
    width: 300px;
    outline: 0;
    font-size: 15px;
    padding: 5px;
  }
  .container div input{
    width: 300px;
    outline: 0;
    font-size: 15px;
    padding: 5px;
  }
  #acessorios{
    height: 200px;
  }
  #cor{
    display: flex;
    flex-direction: row;
  }
  #cor div{
    width: 20px;
    height: 20px;
  }
  #imagem img{
    width: 300px;
    height: 200px;
  }
</style>
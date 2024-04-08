<script setup>
import CategoriaAPI from '../api/categoria'
import CorAPI from '../api/cor'
import MarcaAPI from '../api/marca'
import AcessoriosAPI from '../api/acessorios'
import { computed, onMounted, reactive, ref, watch } from 'vue'
import { logged } from '../pinia'
import VeiculoAPI from '@/api/veiculos'
import UserAPI from '@/api/usuario'
import { useRouter } from 'vue-router'
const Corapi = new CorAPI()
const Categoriaapi = new CategoriaAPI()
const Marcaapi = new MarcaAPI()
const Acessorioapi = new AcessoriosAPI()
const veiculosapi = new VeiculoAPI()
const usuarioapi = new UserAPI()

const store = logged()
const cores = ref(null)
const marcas = ref(null)
const acessorios = ref(null)
const categorias = ref(null)

const usuario = computed(() =>{
  return store.showuser
})

const corselecionada = ref(null)
const marcaselecionada = ref(null)
const acessoriosselecionados = ref(null)
const categoriaselecionada = ref(null)
const nome = ref(null)
const image = reactive({
    car: null
})
const ano = ref(null)
const preco = ref(null)

const corid = ref(null)
const categoriaid = ref(null)
const marcaid = ref(null)
const acessoriosids = ref(null)
const userid = ref(null)

function alterarimagem(e){
  const target = e.target

  if(target && target.files){
    const files = target.files[0]
    image.car = URL.createObjectURL(files)
  }
}

watch(corselecionada, async(cor) =>{
  const cores = await Corapi.ListarCores()
  const findcores = cores.find(corid => corid.descricao === cor)
  corid.value = findcores.id
  console.log(corid.value)
})

watch(categoriaselecionada, async(categoria) =>{
  const categorias = await Categoriaapi.ListarCategoria()
  const findcategoria = categorias.find(categoriaid => categoriaid.nome === categoria)
  categoriaid.value = findcategoria.id
})

watch(marcaselecionada, async (marca) =>{
  const marcas = await Marcaapi.ListarMarcas()
  const findmarca = marcas.find(marcasid => marcasid.nome === marca)
  marcaid.value = findmarca.id
})

watch(acessoriosselecionados, async (acessorio) =>{
  const acessoriosapi = await Acessorioapi.ListarAcessorios()
  for(const acessorios of acessorio){
    const findacessorios = acessoriosapi.find(acessoriosselected => acessoriosselected.descricao === acessorios)
    acessoriosids.value = findacessorios.id
    console.log(acessoriosids.value)
  }
})

async function NovoVeiculo(){
  const veiculo = {
      usuario: userid.value,
      foto: image.car,
      nome: nome.value,
      marca: marcaid.value,
      categoria: categoriaid.value,
      cor: corid.value,
      acessorio: [acessoriosids.value],
      ano: ano.value,
      preco: preco.value
  }
  await veiculosapi.CriarVeiculo(veiculo)
  alert('veiculo criado')
  setTimeout(() =>{
    useRouter().push('/')
  }, 1000)
}


onMounted(async () => {
  cores.value = await Corapi.ListarCores()
  marcas.value = await Marcaapi.ListarMarcas()
  acessorios.value = await Acessorioapi.ListarAcessorios()
  categorias.value = await Categoriaapi.ListarCategoria()
  const apiusuario = await usuarioapi.ListarUsuarios()
  const iduser = apiusuario.find(user => user.username === usuario.value)
  userid.value = iduser.id
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
        <input type="number" placeholder="preco" v-model="preco">
        <input type="number" placeholder="ano" v-model="ano">
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
      <button @click="NovoVeiculo">enviar</button>
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
<script setup>
import VeiculoAPI from "@/api/veiculos";
import { onMounted, ref } from "vue";
const veiculosapi = new VeiculoAPI()

const garagem = ref(null)

onMounted(async () =>{
    garagem.value =  await veiculosapi.ListarVeiculos()
    console.log(garagem.value)
  })
</script>

<template>
<div class="container"> 
  <h1>Minha Garagem</h1>
<div class="container-card">
  <div class="card" v-for="carros in garagem" :key="carros.id">
    <div id="image">
      
    </div>
      <p id="titulo">{{carros.nome}}</p>
      <p>R$ {{carros.preco}}</p>
      <p>ano: {{carros.ano}}</p>
      <p>marca: {{carros.marca.nome}}</p>
      <p>categoria: {{carros.categoria.nome}}</p>
      <div :style="{backgroundColor: carros.cor.descricao}"></div>
      <div class="detalhes">
        <button>ver mais</button>
      </div>
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
  }
  .container-card{
    display: flex;
    gap: 50px;
  }
  .card{
      width: 300px;
      box-shadow: 5px 5px 5px 5px rgba(0, 0, 0, 0.1);
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
  }
  .detalhes{
    width: 100%;
    display: flex;
    justify-content: center;
  }
  #titulo{
    font-size: 25px;
    font-weight: bold;
  }
  p{
    font-size: 18px;
  }
  img{
    width: 100%;
    height: 200px;
  }
  #image{
    width: 100%;
  }
</style>

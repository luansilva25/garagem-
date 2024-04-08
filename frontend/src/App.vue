<script setup>
  import { onMounted } from "vue";
  import cabecalho from "./components/cabecalho-component.vue"
  import rodapeComponent from "./components/rodape-component.vue";
  import { logged } from "./pinia";
  const store = logged()
  
  onMounted(() =>{
      store.autologin()
  })

</script>
<template>
  <div>
  <header>
    <h1>garagem zika</h1>
    <cabecalho/>
  </header>
  <main>
      <router-view/>
  </main>
  <footer>
      <rodape-component/>
  </footer>
</div>
</template>
<style>
  *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Helvetica ;
  }
  header{
    width: 100vw;
    display: flex;
    background-color: black;
    justify-content: space-between;
    align-items: center;
    box-shadow: 3px 2px 3px 3px rgba(255, 217, 0, 0.495);
    padding: 20px;
  }
  header h1{
    margin-left: 20px;
    color: gold
  }
  main {
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: start;
    margin-top: 130px;
    align-items: center;
    height: 120vh;
  }
  footer{
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    background-color: black ;
    border-top: 3px solid gold;
    padding: 50px
  }
</style>
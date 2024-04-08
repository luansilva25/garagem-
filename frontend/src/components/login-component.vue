<script setup>
import { computed, ref, } from 'vue'
import TokenAPI from '@/api/token';
import { useRouter } from 'vue-router';


const tokenapi = new TokenAPI()
const senhauser = localStorage.getItem('senha')
const usuarioname = localStorage.getItem('usuario')
const user = ref(null)
const router = useRouter()
const senha = ref(null)
const msg = ref(null)


const errormsg = ref(null)
const emit = defineEmits(['criar'])
function mudar() {
  emit('criar')
}
const uservalidation = computed(() =>{
    if(user.value === usuarioname && senhauser === senha.value){
      return true
    }
    return false
})

async function login(){
    if(uservalidation.value){
        msg.value = "usuario logado com sucesso"

        const token = {
            username: user.value,
            password: senha.value
        }

        await tokenapi.PegarToken(token)

        setTimeout(() =>{
            router.push('/')
            msg.value = null
            
        }, 2000)
    }
    else{
        errormsg.value = "usuario ou senha incorreto"

        setTimeout(() =>{
            errormsg.value = null
        }, 2000)
    }
}

</script>
<template>
  <div class="container">
    <div class="msg" v-if="msg">
      <p>{{ msg }}</p>
    </div>
    <div class="errormsg" v-if="errormsg">
      <p>{{ errormsg }}</p>
    </div>
    <div class="card">
      <h1>Login</h1>
      <div class="campos">
        <input type="text" placeholder="username/email" v-model="user" />
        <input type="password" placeholder="senha" v-model="senha"/>
      </div>
      <div class="acoes">
        <button id="criar" @click="login">Login</button>
        <button id="possui" @click="mudar">Não possuo uma conta</button>
      </div>
    </div>
  </div>
</template> 
  <style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
.card {
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  padding: 10px;
  gap: 10px;
  box-shadow: 1px 2px 2px 1px black;
  width: 400px;
  height: 320px;
}
.campos {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
}
.campos input {
  font-size: 17px;
  padding: 5px;
  outline: 0;
  border: none;
  border-bottom: 2px solid;
  transition: 1s;
}
.campos input:focus {
  border-bottom: 2px solid gold;
}
.acoes {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 5px;
}
#criar {
  width: 150px;
  padding: 5px;
  background-color: black;
  color: gold;
  border: none;
  border-radius: 20px;
  font-size: 18px;
  height: 40px;
}
#possui {
  border: none;
  padding: 5px;
  color: gold;
  background-color: white;
  font-size: 18px;
}
.errormsg {
  background-color: red;
  border: 2px solid black;
  display: flex;
  justify-content: center;
  width: 400px;
  padding: 15px;
}
.errormsg p {
  color: black;
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
</style>
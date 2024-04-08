<script setup>
import { computed, ref, watch } from 'vue'
import UserAPI from '../api/usuario'

const userapi = new UserAPI()

const username = ref(null)
const usernamevalid = ref(true)
const email = ref(null)
const senha = ref(null)
const confirm = ref(null)
const msg = ref(null)
const errormsg = ref(null)

const emit = defineEmits(['login'])

function mudar(){
    emit('login')
}

const emailvalidation = computed(() => {
  if (!email.value) {
    return false
  }
  if (!email.value.includes('@')) {
    return false
  }
  return true
})

const senhavalidation = computed(() => {
  if (!senha.value) {
    return false
  }
  if (senha.value.length < 8 || senha.value.length > 25) {
    return false
  }
  if (!senha.value.match(/\d/)) {
    return false
  }
  return true
})

const senhaconfirmationvalidation = computed(() => {
  if (!confirm.value) {
    return false
  }
  if (confirm.value !== senha.value) {
    return false
  }
  return true
})

watch(username, async (user) => {
  const userdata = await userapi.ListarUsuarios()
  const usuarioexiste = userdata.find((usuario) => usuario.username === user)
  if (usuarioexiste) {
    usernamevalid.value = false
  } else {
    usernamevalid.value = true
  }
  console.log(usernamevalid.value)
})

async function criarconta() {
  if (
    usernamevalid.value &&
    senhaconfirmationvalidation.value &&
    senhavalidation.value &&
    emailvalidation.value
  ) {
    msg.value = 'conta criada com sucesso, faça o login'

    const user = {
      username: username.value,
      email: email.value,
      password: senha.value
    }

    localStorage.setItem('usuario', username.value)
    localStorage.setItem('senha', senha.value)
    localStorage.setItem('email', email.value)

    await userapi.CriarUsuario(user)
    
    setTimeout(() => {
      msg.value = null
      emit('login')
    }, 2000)
  }
    else {
    errormsg.value = 'ops, alguns dos campos parecem estar incorretos ou o usuario ja existe'
    setTimeout(() => {
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
      <h1>criar conta</h1>
      <div class="campos">
        <input type="text" placeholder="username" v-model="username" />
        <input type="email" placeholder="email" v-model="email" />
        <input type="password" placeholder="senha" v-model="senha" />
        <input type="password" placeholder="confirme sua senha" v-model="confirm" />
      </div>
      <div class="acoes">
        <button id="criar" @click="criarconta">criar conta</button>
        <button id="possui" @click="mudar">já possuo uma conta</button>
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
  height: 420px;
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
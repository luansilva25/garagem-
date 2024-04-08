import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
export const logged = defineStore('login', () => {
    const login = ref(false)
    const access = ref(null)
    const refresh = ref(null)
    const user = ref(null)

    const showlog = computed(() =>{
        return login.value
    })

    const showuser = computed(() =>{
        return user.value
    })

    function userlog(payload){
        login.value = true
        access.value = payload.access
        refresh.value = payload.refresh
        user.value = localStorage.getItem('usuario')
        console.log(user.value)
    }

    function autologin(){
        const accessLocal = localStorage.getItem('access')
        const refreshLocal = localStorage.getItem('refresh')
        const userLocal = localStorage.getItem('usuario')
        
        if(accessLocal && refreshLocal && userLocal){
            login.value = true
            access.value = accessLocal
            refresh.value = refreshLocal
            user.value = userLocal
        }
    }
    function logout(){
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
        login.value = false
        access.value = null
        refresh.value = null
    }

    return { userlog, showlog, showuser, autologin, logout }
})

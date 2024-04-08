import axios from 'axios'
import { logged } from '@/pinia/index'
const store = logged()


export default class TokenAPI{
    async PegarToken(token){
        const { data } = await axios.post("http://127.0.0.1:8000/token/", token)
        localStorage.setItem('access', data.access)
        localStorage.setItem('refresh', data.refresh)
        store.userlog({access: data.access, refresh: data.refresh})
        return data
    }
}
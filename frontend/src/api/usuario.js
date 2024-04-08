import axios from "axios"

export default class UserAPI {
    async ListarUsuarios() {
        const { data } = await axios.get("http://127.0.0.1:8000/usuarios/")
        return data
    }
    async CriarUsuario(user){
        const { data } = await axios.post("http://127.0.0.1:8000/usuarios/", user)
        return data
    }
}
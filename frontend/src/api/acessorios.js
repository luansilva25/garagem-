import axios from 'axios'

export default class AcessorioAPI{
    async ListarAcessorios(){
        const { data } = await axios.get("http://127.0.0.1:8000/acessorios/")
        return data
    }
    async CriarAcessorio(acessorio, userid){
        const { data } = await axios.post("http://127.0.0.1:8000/acessorios/", {usuario:userid, descricao: acessorio})
        return data
    }
    async ExcluirAcessorio(id){
        const { data } = await axios.delete(`http://127.0.0.1:8000/acessorios/${id}/`)
        return data
    }
}
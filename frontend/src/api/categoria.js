import axios from "axios"

export default class CategoriaAPI{
    async ListarCategoria(){
        const { data } = await axios.get('http://127.0.0.1:8000/categorias/')
        return data
    }
    async CriarCategoria(categoria, userid){
        const { data } = await axios.post('http://127.0.0.1:8000/categorias/', {usuario:userid,  nome: categoria})
        return data
    }
    async ExcluirCategoria(id){
        const { data } = await axios.delete(`http://127.0.0.1:8000/categorias/${id}/`)
        return data
    }
}
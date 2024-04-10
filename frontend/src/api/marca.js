import axios from "axios";

export default class MarcaAPI {
    async ListarMarcas(){
        const { data } = await axios.get("http://127.0.0.1:8000/marcas/")
        return data
    }
    async NovaMarca(marca, nacionalidade, userid){
        const { data } =  await axios.post("http://127.0.0.1:8000/marcas/", { usuario:userid, nome: marca,  nacionalidade: nacionalidade})
        return data
    }
    async ExcluirMarca(id){
        const { data } = await axios.delete(`http://127.0.0.1:8000/marcas/${id}/`)
        return data
    }
}
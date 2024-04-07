import axios from 'axios'

export default class CorAPI{
    async ListarCores(){
       const { data } =  await axios.get("http://127.0.0.1:8000/cores/")
       return data
    }
    async CriarCor(cor){
        const { data } = await axios.post("http://127.0.0.1:8000/cores/", { descricao: cor })
        return data
    }
    async ExcluirCor(id){
        const { data } = await axios.delete(`http://127.0.0.1:8000/cores/${id}/`)
        return data.results
     }
}
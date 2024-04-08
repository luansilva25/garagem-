import axios from "axios"

export default class VeiculoAPI{
    async ListarVeiculos() {
        const token = localStorage.getItem('access')
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
        const { data } = await axios.get("http://127.0.0.1:8000/veiculos/")
        return data
    }
    async CriarVeiculo(veiculo){
        const token = localStorage.getItem('access')
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
        const { data } = await axios.post("http://127.0.0.1:8000/veiculos/", veiculo)
        return data
    }
}
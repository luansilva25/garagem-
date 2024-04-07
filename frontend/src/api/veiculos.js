import axios from "axios"

export default class VeiculoAPI{
    async ListarVeiculos() {
        const { data } = await axios.get("veiculos/")
        return data.results
    }
}
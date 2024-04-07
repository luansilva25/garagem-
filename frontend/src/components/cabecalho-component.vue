<template>
    <ul>
        <li>
            <router-link to="/">Garagem</router-link>
        </li>
        <li>
            <router-link to="/categoria">Categorias</router-link>
        </li>
        <li>
            <router-link to="/marca">Marca</router-link>
        </li>
        <li>
            <router-link to="/cor">Cor</router-link>
        </li>
        <li>
            <router-link to="/acessorio">Acessorio</router-link>
        </li>
        <li>
            <router-link to="/veiculo">Veiculo</router-link>
        </li>
        <li>
            <router-link to="/auth">login</router-link>
        </li>
    </ul>
</template>
<style>
    ul{
        display: flex;
        gap: 20px;
        list-style: none;
        margin-right: 50px;
        font-size: 18px;
    }
    ul li a{
        text-decoration: none;
        color: gold;
        transition: 0.5s;
    }
    ul li a:hover{
        color: yellow;
    }
</style>
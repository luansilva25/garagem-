<script setup>
    import { ref } from "vue";
    import criarconta from "../components/criarconta-component.vue";
    import login from '../components/login-component.vue'

    const mudar = ref(true)
</script>
<template> 
<div>
    <login @criar="mudar = !mudar" v-if="mudar"/> 
    <criarconta @login="mudar = !mudar" v-else/>
</div>
</template>

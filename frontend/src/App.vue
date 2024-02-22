<script setup>

import { RouterView, RouterLink } from 'vue-router'
</script>

<template>
    <div class="app bg-gradient-to-br from-purple-500 to-pink-500">
        
        
        <header class="flex justify-center mx-40 mb-16 py-6 text-2xl
        border-b-2 border-white text-white rounded-md">
            <RouterLink class="link" :to="{ name: 'home' }">Главная</RouterLink>
            <RouterLink class="link" :to="{ name: 'add-task' }">Добавить задачу</RouterLink>
        </header>

        <main class="mx-40 mt-16">
            <RouterView />
        </main>
    </div>
</template>

<style scoped>
.link {
    padding: 0 10px;
}

.router-link-exact-active {
    color: rgb(253, 233, 7);
}

.app {
    height: 100vh;

}
</style>
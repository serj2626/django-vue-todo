<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const todos = ref([])



onMounted(async () => {
    try {
        const { data } = await axios.get('http://127.0.0.1:8000/api/todo', {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

        todos.value = data
    } catch (error) {
        console.log(error)
    }
});



</script>

<template>
    <div v-for="todo in todos" :key="todo.id" id="task"
        class="flex justify-between items-center border-b border-slate-200 py-3 px-2 border-l-4  border-l-transparent">
        <div class="inline-flex items-center space-x-2">
            <div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 text-slate-500">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
            </div>
            <div :class="{'line-through': todo.is_completed }" class="text-slate-500">{{ todo.title }}</div>
        </div>
        <div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                class="w-4 h-4 text-slate-500 hover:text-slate-700 hover:cursor-pointer">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
            </svg>
        </div>
    </div>
</template>


<style scoped></style>
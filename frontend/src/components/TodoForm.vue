<script setup>
import axios from "axios";
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";

const task = reactive({
  title: "",
  description: "",
  completed: false,
});

const url = ref('http://127.0.0.1:8000/api/todo/')


function submitForm(title, description, completed) {
  if (title === '' || description === '') {
    alert('Заполните все поля')
  } else {
    axios.post(url.value, {
      title: title,
      description: description,
      completed: completed,
      user: 1

    })
    alert('Задача добавлена')
    task.title = ''
    task.description = ''
    task.completed = false
  }
}

</script>

<template>
  <div class="mt-8 mb-10 w-7/12 mx-auto text-center text-3xl text-yellow-400">
    <p>Создание задачи</p>
  </div>

  <div class="text-xl w-8/12 mx-auto">
    <form @submit.prevent="submitForm(task.title, task.description, task.completed)">
      <label class="text-sm font-medium">Название задачи</label>
      <input v-model="task.title"
        class="mb-3 mt-1 block w-full px-2 py-1.5 border border-gray-300 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 focus:invalid:border-red-500 focus:invalid:ring-red-500"
        placeholder="Купить....." maxlength="100" />

      <label class="text-sm font-medium">Описание задачи</label>
      <textarea v-model="task.description"
        class="mb-3 mt-1 block w-full px-2 py-1.5 border border-gray-300 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 focus:invalid:border-red-500 focus:invalid:ring-red-500"
        placeholder="Напишите что-нибудь......">
      </textarea>

      <div class="mb-6 flex min-h-[1.5rem] items-center justify-center pl-[1.5rem]">
        <input v-model="task.completed"
          class="relative float-left -ml-[1.5rem] mr-[6px] h-[1.125rem] w-[1.125rem] appearance-none rounded-[0.25rem] border-[0.125rem] border-solid border-neutral-300 outline-none before:pointer-events-none before:absolute before:h-[0.875rem] before:w-[0.875rem] before:scale-0 before:rounded-full before:bg-transparent before:opacity-0 before:shadow-[0px_0px_0px_13px_transparent] before:content-[''] checked:border-primary checked:bg-primary checked:before:opacity-[0.16] checked:after:absolute checked:after:-mt-px checked:after:ml-[0.25rem] checked:after:block checked:after:h-[0.8125rem] checked:after:w-[0.375rem] checked:after:rotate-45 checked:after:border-[0.125rem] checked:after:border-l-0 checked:after:border-t-0 checked:after:border-solid checked:after:border-white checked:after:bg-transparent checked:after:content-[''] hover:cursor-pointer hover:before:opacity-[0.04] hover:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:shadow-none focus:transition-[border-color_0.2s] focus:before:scale-100 focus:before:opacity-[0.12] focus:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:before:transition-[box-shadow_0.2s,transform_0.2s] focus:after:absolute focus:after:z-[1] focus:after:block focus:after:h-[0.875rem] focus:after:w-[0.875rem] focus:after:rounded-[0.125rem] focus:after:content-[''] checked:focus:before:scale-100 checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca] checked:focus:before:transition-[box-shadow_0.2s,transform_0.2s] checked:focus:after:-mt-px checked:focus:after:ml-[0.25rem] checked:focus:after:h-[0.8125rem] checked:focus:after:w-[0.375rem] checked:focus:after:rotate-45 checked:focus:after:rounded-none checked:focus:after:border-[0.125rem] checked:focus:after:border-l-0 checked:focus:after:border-t-0 checked:focus:after:border-solid checked:focus:after:border-white checked:focus:after:bg-transparent dark:border-neutral-600 dark:checked:border-primary dark:checked:bg-primary dark:focus:before:shadow-[0px_0px_0px_13px_rgba(255,255,255,0.4)] dark:checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca]"
          type="checkbox" />
        <label class="inline-block pl-[0.15rem] hover:cursor-pointer" for="exampleCheck10">
          Задание выполнено
        </label>
      </div>



      <button class="px-4 py-1.5 rounded-md shadow-lg bg-gradient-to-r from-pink-600
         to-red-600 font-medium text-gray-100 block w-full text-center
         hover:bg-red-700" type="submit">
        <span id="login_default_state">Добавить<span id="subtotal"></span></span>
      </button>
    </form>
  </div>
</template>

<style scoped></style>

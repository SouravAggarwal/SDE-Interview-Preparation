<script setup>
    import {useRoute, useRouter, RouterView} from "vue-router"
    import { ref, onBeforeMount } from "vue"
    import cars from "../data/cars.json"

    const state = ref(true)
    const route = useRoute()
    const router = useRouter()

    const carId = parseInt(route.params.id)
    let car;

    onBeforeMount(() => {
        car = cars.find(c => {
            console.log("sada")
            return c.id === carId
        });
    })

    const showContact = () => { 
        if(carId === 4) return;
        return router.push(`/cars/${carId}/contact`)
    }
</script>

<template>
    <div v-if="car">
        <h1>Car View</h1>
        <p>{{car.name}}</p>
        <p>{{car.year}}</p>
        <p>{{car.price}}</p>
        <button @click="showContact">Click for contact</button>
        <RouterView />
        <button @click="state = !state">toggle</button>
    </div>
    <div v-else>
        <h1>Car not found</h1>
    </div>
</template>

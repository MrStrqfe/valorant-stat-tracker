<script setup>
import { ref, onMounted } from "vue"

const stats = ref(null)

onMounted(async () => {
  const res = await fetch("http://localhost:3000/api/stats")
  stats.value = await res.json()
})
</script>

<template>
  <div v-if="stats">
    <h2>Season Stats</h2>
    <p>Kills: {{ stats[0].kills }}</p>
    <p>Deaths: {{ stats[0].deaths }}</p>
    <p>K/D Ratio: {{ stats[0].kDRatio }}</p>
  </div>
</template>
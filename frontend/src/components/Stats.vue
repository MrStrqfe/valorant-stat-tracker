<script setup>
import { ref, onMounted } from 'vue'

const stats = ref(null)

onMounted(async () => {
  const res = await fetch('http://localhost:3000/api/stats')
  stats.value = await res.json()
})
</script>

<template>
  <div v-if="stats" class="p-6 max-w-sm mx-auto">
    <h2 class="font-mono text-2xl font-semibold text-white mb-1">Player Stats</h2>
    <p class="text-xs text-gray-400 uppercase tracking-widest mb-6">Season Overview</p>

    <!-- KDA Row -->
    <div class="grid grid-cols-3 gap-3 mb-4">
      <div class="bg-gray-50 rounded-xl p-4 text-center">
        <p class="text-xs text-gray-400 uppercase tracking-wide mb-1">Kills</p>
        <p class="text-2xl font-bold text-gray-900">{{ stats[0].kills }}</p>
      </div>
      <div class="bg-red-50 rounded-xl p-4 text-center">
        <p class="text-xs text-red-400 uppercase tracking-wide mb-1">Deaths</p>
        <p class="text-2xl font-bold text-red-600">{{ stats[0].deaths }}</p>
      </div>
      <div class="bg-gray-50 rounded-xl p-4 text-center">
        <p class="text-xs text-gray-400 uppercase tracking-wide mb-1">K/D</p>
        <p class="text-2xl font-bold text-gray-900">{{ stats[0].kDRatio }}</p>
      </div>
    </div>

    <!-- Headshot % -->
    <div class="bg-gray-900 rounded-xl p-4 mb-4 flex items-center justify-between">
      <div>
        <p class="text-xs text-gray-400 uppercase tracking-wide mb-1">Headshot %</p>
        <p class="text-3xl font-bold text-white">
          {{ stats[0].headshotsPercentage }}<span class="text-lg text-gray-400">%</span>
        </p>
      </div>
      <div class="w-12 h-12 rounded-full bg-white/10 flex items-center justify-center">
        <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24">
          <path
            d="M12 2a10 10 0 1 0 0 20A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 0-16 8 8 0 0 1 0 16zm0-11a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"
          />
        </svg>
      </div>
    </div>

    <!-- Win/Loss -->
    <div class="bg-gray-50 rounded-xl p-4">
      <div class="flex justify-between items-center mb-3">
        <p class="text-xs text-gray-400 uppercase tracking-wide">Win Rate</p>
        <p class="text-sm font-bold text-gray-900">{{ stats[0].matchesWinPct }}</p>
      </div>
      <div class="flex rounded-full overflow-hidden h-2 mb-3">
        <div
          class="bg-green-400 transition-all duration-500"
          :style="{ width: parseFloat(stats[0].matchesWinPct) + '%' }"
        />
        <div
          class="bg-red-300 transition-all duration-500"
          :style="{ width: 100 - parseFloat(stats[0].matchesWinPct) + '%' }"
        />
      </div>
      <div class="flex justify-between text-xs text-gray-500">
        <span>{{ stats[0].matchesWon }} <span class="text-green-500 font-medium">W</span></span>
        <span>{{ stats[0].matchesLost }} <span class="text-red-400 font-medium">L</span></span>
      </div>
    </div>
  </div>
</template>

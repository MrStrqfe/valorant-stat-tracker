# Valorant Stat Tracker

## Overview

This project is a **full-stack web application** that retrieves and displays **Valorant player statistics**.
The backend collects data using **web scraping**, and the frontend displays the information using **Vue.js**.

Current architecture:

```
Scrapy → JSON → Express API → Vue Frontend
```

The scraper gathers player stats from a tracker site and stores them in a JSON file.
An **Express server** exposes the data through an API endpoint, and the **Vue frontend** fetches and renders the stats.

---

# Project Structure

```
valorant-stat-tracker
│
├── backend
│   ├── server.js        # Express API server
│   └── stats.json       # Scraped player statistics
│
└── frontend
    ├── src
    │   ├── App.vue
    │   └── components
    │       └── Stats.vue
    ├── vite.config.js
    └── package.json
```

---

# Backend

## Technologies

- Node.js
- Express
- CORS

## Purpose

The backend serves the scraped data so the frontend can access it.

## Endpoint

```
GET /api/stats
```

Returns the contents of `stats.json`.

## Example Express Server

```javascript
const express = require('express')
const fs = require('fs')
const cors = require('cors')

const app = express()

app.use(cors())

app.get('/api/stats', (req, res) => {
  const data = JSON.parse(fs.readFileSync('stats.json'))
  res.json(data)
})

app.listen(3000, () => {
  console.log('Server running on port 3000')
})
```

## Running the Backend

```
cd backend
node server.js
```

The API will be available at:

```
http://localhost:3000/api/stats
```

---

# Frontend

## Technologies

- Vue 3
- Vite

## Purpose

The frontend fetches data from the Express API and displays the player's stats.

## Fetching Data

Example Vue logic:

```javascript
import { ref, onMounted } from 'vue'

const stats = ref(null)

onMounted(async () => {
  const res = await fetch('http://localhost:3000/api/stats')
  stats.value = await res.json()
})
```

## Example Display

```
Kills
Deaths
K/D Ratio
Win Rate
```

---

# Running the Frontend

```
cd frontend
npm install
npm run dev
```

The Vue app will start on:

```
http://localhost:5173
```

---

# How the System Works

1. Scrapy scrapes Valorant statistics from the tracker website.
2. The scraped data is saved as `stats.json`.
3. The Express backend reads the JSON file and exposes it through an API.
4. The Vue frontend requests the data from the API and displays the stats.

---

# Current Progress

✔ Implemented web scraping to collect player stats
✔ Stored scraped data in a JSON file
✔ Created an Express backend API
✔ Connected the Vue frontend to the backend using `fetch()`
✔ Displayed stats in the frontend UI

---

# Next Steps

- Add **dynamic player search**
- Run the scraper automatically from the API
- Store data in a **database**
- Improve UI styling
- Add match history and agent statistics
- Deploy the application

---

# Future Architecture (Planned)

```
Scraper
   ↓
Database
   ↓
Express API
   ↓
Vue Frontend
```

This will allow multiple players to be searched and cached efficiently.

---

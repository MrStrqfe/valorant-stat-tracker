const express = require("express")
const fs = require("fs")
const cors = require("cors")

const app = express()
app.use(cors())

app.get("/api/stats", (req, res) => {
    const data = JSON.parse(fs.readFileSync("stats.json"))
    res.json(data)
})

app.listen(3000, () => {
    console.log("Server running on port 3000")
})
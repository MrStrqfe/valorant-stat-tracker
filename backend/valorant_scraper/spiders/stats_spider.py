import scrapy

class StatsSpider(scrapy.Spider):
    name = "stats"

    async def start(self):
        url = "https://api.tracker.gg/api/v2/valorant/standard/profile/riot/MrStrqfe%230900"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json",
        }
        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        data = response.json()
        segments = data["data"]["segments"]

        for segment in segments:
            stats = segment["stats"]
            item = {"segment_type": segment.get("type")}

            # Safely extract whatever keys exist
            for key, value in stats.items():
                item[key] = value.get("displayValue")

            yield item  # ← this is what actually writes to stats.json
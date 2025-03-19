from fastapi import FastAPI, Request
import requests

app = FastAPI()

# Static Headers (Same as Provided in Request)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "Te": "trailers"
}

# Static Cookie (Preserve User Session)
COOKIES = {
    "user_id": "4yITazW6EFZzujFmePqCkw:1742289365162:040073106b3004ea563a46d22946effade0bc3cd"
}

@app.get("/vehicle")
async def get_vehicle(id: str):
    """
    This API proxies requests to ACKO and returns vehicle details.
    """
    external_api_url = f"https://www.acko.com/asset_service/api/assets/search/vehicle/{id}?validate=false&source=rto"

    try:
        response = requests.get(external_api_url, headers=HEADERS, cookies=COOKIES)

        # If successful response
        if response.status_code == 200:
            return {"status": "success", "data": response.json()}
        else:
            return {"status": "error", "message": "Vehicle data not found!", "code": response.status_code}

    except Exception as e:
        return {"status": "error", "message": str(e)}


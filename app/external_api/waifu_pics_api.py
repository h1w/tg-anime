from app.external_api.base_api import BaseAPIClient


class WaifuPicsAPIClient(BaseAPIClient):
    def __init__(self):
        super().__init__(base_url="https://api.waifu.pics")

    async def random_art(self, type: str, category: str) -> str:
        endpoint = f"{type}/{category}"
        response = await self.request(endpoint=endpoint, method="GET")
        return response["url"]

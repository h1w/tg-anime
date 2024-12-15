import logging

import aiohttp


class BaseAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def request(self, endpoint, method="GET", **kwargs) -> str | None:
        async with aiohttp.ClientSession() as session:
            try:
                url = f"{self.base_url}/{endpoint}"
                async with session.request(method, url, **kwargs) as response:
                    response.raise_for_status()
                    return await response.json()
            except aiohttp.ClientError as e:
                logging.exception(
                    f"Error occureed with request: {e}",
                    f"URL that caused the error: {url}",
                )
                return None

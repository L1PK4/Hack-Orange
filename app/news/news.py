from api.api import API


class News:
    def __init__(self, api: API) -> None:
        self.api: API = api

    async def get_news(self) -> dict:
        return await self.api.send_request(
            path='/news/LatestNews5Minutes',
            method='GET'
        )

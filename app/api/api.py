from typing import Literal
import aiohttp as aio


class API:
    def __init__(
            self,
            base_url: str = 'https://datsorange.devteam.games',
            headers: dict[str, str] | None = None,
    ) -> None:
        self.base_url = base_url
        self.headers = headers

    async def send_request(
            self,
            path: str,
            method: Literal["GET", "POST"],
            body: dict | None = None,
    ):
        async with aio.ClientSession() as session:
            async with session.request(
                method,
                self.base_url + path,
                headers=self.headers,
                data=body
            ) as response:
                return await response.json()

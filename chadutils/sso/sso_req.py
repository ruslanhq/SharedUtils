from urllib.parse import urljoin


class GetUser:
    def __init__(self, url, user_id, project_name, http_client):
        self.user_id = user_id
        self.url = urljoin(url, self.user_id)
        self.headers = {'X-Internal-API': project_name}
        self.http_client = http_client

    async def request_to_sso(self):
        return await self.http_client(
            uri=self.url, headers=self.headers
        ).do_request()

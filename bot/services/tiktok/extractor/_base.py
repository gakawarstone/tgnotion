from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

from services.http import HttpService, HttpRequestError
from .exceptions import SourceInfoExtractFailed
from ..types import InfoVideoTikTok


class BaseExtractor(ABC):
    @abstractmethod
    async def get_video_info(cls, url: str) -> InfoVideoTikTok:
        pass

    @abstractmethod
    async def get_video_file_url(cls, url: str) -> InfoVideoTikTok:
        pass

    async def _get_soup(self, url: str) -> BeautifulSoup:
        try:
            return BeautifulSoup(await HttpService.get(url), "html.parser")
        except HttpRequestError:
            raise SourceInfoExtractFailed(self)

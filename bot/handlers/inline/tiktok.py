from aiogram import Router
from aiogram.types import InlineQuery

from services.tiktok import TikTokService
from utils.serializers import url_to_video_query_result
from filters.tiktok import TikTokVideoLink


async def send_tiktok(query: InlineQuery):
    return await query.answer(
        results=[
            url_to_video_query_result(
                video_url=await TikTokService.get_video_url(query.query),
                title='TikTok',
                description='tap to send'
            )
        ],
        cache_time=60,
        is_personal=True
    )


def setup(router: Router):
    router.inline_query(
        send_tiktok,
        TikTokVideoLink()
    )

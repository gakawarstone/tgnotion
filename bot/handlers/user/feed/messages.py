from typing import Any


from extensions.handlers.message.base import BaseHandler as BaseMessageHandler
from ._base import BaseHandler
from ._item_processor import GkfeedItemProcessorExtention


class GetFeedItemHandler(GkfeedItemProcessorExtention, BaseHandler, BaseMessageHandler):
    _items_limit = 10

    async def handle(self) -> Any:
        await self.event.delete()

        items_cnt = 0
        async for item in self._gkfeed.get_all_user_items():
            if items_cnt >= self._items_limit:
                break

            await self._process_item(item)

            items_cnt += 1

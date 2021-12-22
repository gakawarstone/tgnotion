from notion.client import NotionClient
from notion.block import TextBlock
from notion.block import PageBlock
import config

client = NotionClient(config.TOKEN)


class Page(object):
    def __init__(self, URL):
        self.URL = URL
        self.view = self.__get()

    def get_URL(self):
        return self.URL

    def __get(self, client=client):
        """get NotionClient object"""
        return client.get_block(self.URL)

    def write(self, text):
        self.view.children.add_new(TextBlock, title=text)


class Database(Page):
    def __get(self, client=client):
        """get NotionClient object"""
        return client.get_collection_view(self.URL)

    def add_row(self):
        row = self.view.collection.add_row()
        return row

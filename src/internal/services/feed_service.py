"""Feed service"""

from typing import TYPE_CHECKING
from src.internal.domain import Feed

if TYPE_CHECKING:
    from src.internal.interfaces import FeedRepository


class FeedService:
    """Feed service"""

    def __init__(self, feed_repository: "FeedRepository"):
        self.feed_repository = feed_repository

    def create(self, feed: Feed):
        """Create feed"""
        self.feed_repository.create(feed)

    def get_by_id(self, feed_id: str) -> Feed:
        """Get feed by id"""
        return self.feed_repository.get_by_id(feed_id)

    def get(self) -> list[Feed]:
        """Get feeds"""
        return self.feed_repository.get()

    def update(self, feed: Feed):
        """Update feed"""
        self.feed_repository.update(feed)

    def delete(self, feed_id: str):
        """Delete feed"""
        self.feed_repository.delete(feed_id)

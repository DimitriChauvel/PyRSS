"""Feed repository interface"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from internal.domain import Feed


class FeedRepository(ABC):
    """Feed repository interface"""

    @abstractmethod
    def create(self, feed: "Feed"):
        """Create feed"""

    @abstractmethod
    def get_by_id(self, feed_id: str) -> "Feed":
        """Get feed by id"""

    @abstractmethod
    def get(self) -> list["Feed"]:
        """Get feeds"""

    @abstractmethod
    def update(self, feed: "Feed"):
        """Update feed"""

    @abstractmethod
    def delete(self, feed_id: str):
        """Delete feed"""

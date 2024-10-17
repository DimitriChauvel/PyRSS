"""Feed"""

from dataclasses import dataclass


@dataclass
class Feed:
    """Feed definition"""

    feed_id: str
    feed_name: str
    feed_url: str

"""SQLite feed repository"""

import sqlite3
from src.internal.domain import Feed
from src.internal.interfaces import FeedRepository


class SQLiteFeedRepository(FeedRepository):
    """SQLite feed repository"""

    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create table"""
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS feed (
                    feed_id TEXT UNIQUE PRIMARY KEY,
                    feed_name TEXT UNIQUE NOT NULL,
                    feed_url TEXT UNIQUE NOT NULL,
                )
                """
            )

    def create(self, feed: Feed):
        """Create feed"""
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO feed (feed_id, feed_name, feed_url)
                VALUES (?, ?, ?)
                """,
                (feed.feed_id, feed.feed_name, feed.feed_url),
            )

    def get_by_id(self, feed_id: str) -> Feed:
        """Get feed by id"""
        feed = self.conn.execute(
            """
            SELECT feed_id, feed_name, feed_url
            FROM feed
            WHERE feed_id = ?
            """,
            (feed_id),
        )
        return Feed(*feed.fetchone())

    def get(self) -> list[Feed]:
        """Get feeds"""
        feeds = self.conn.execute(
            """
            SELECT feed_id, feed_name, feed_url
            FROM feed
            """
        )
        return [Feed(*feed) for feed in feeds.fetchall()]

    def update(self, feed: Feed):
        """Update feed"""
        with self.conn:
            self.conn.execute(
                """
                UPDATE feed
                SET feed_name = ?, feed_url = ?
                WHERE feed_id = ?
                """,
                (feed.feed_name, feed.feed_url, feed.feed_id),
            )

    def delete(self, feed_id: str):
        """Delete feed"""
        with self.conn:
            self.conn.execute(
                """
                DELETE FROM feed
                WHERE feed_id = ?
                """,
                (feed_id,),
            )

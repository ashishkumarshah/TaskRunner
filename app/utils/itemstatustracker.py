import sqlite3

class ItemStatusTracker:
    CASIO_SKU = "casio"
    DB_FILE = "../db/itemstatus.db"

    @staticmethod
    def add_item_status(item_type, item_id, status):
        """Insert or update an item status."""
        with sqlite3.connect(ItemStatusTracker.DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO itemstatus (item_type, item_id, status)
                VALUES (?, ?, ?)
                ON CONFLICT(item_type, item_id)
                DO UPDATE SET status = excluded.status;
            """, (item_type, item_id, status))
            conn.commit()

    @staticmethod
    def get_item_status(item_type, item_id):
        """Retrieve the status for a given item."""
        with sqlite3.connect(ItemStatusTracker.DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT status FROM itemstatus
                WHERE item_type = ? AND item_id = ?;
            """, (item_type, item_id))
            row = cursor.fetchone()
            return row[0] if row else None

    @staticmethod
    def is_status_changed(item_type: str, item_id: str, status: str):
        prev_status = ItemStatusTracker.get_item_status(item_type, item_id)
        if prev_status is None:
            return True
        return prev_status != status

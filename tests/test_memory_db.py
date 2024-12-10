import unittest
from memory_db import MemoryDB

class TestMemoryDB(unittest.TestCase):

    def setUp(self):
        """Set up a new MemoryDB instance before each test."""
        self.db = MemoryDB()

    def test_get_non_existent_key(self):
        """Test getting a non-existent key returns None."""
        self.assertIsNone(self.db.get("A"))

    def test_put_without_transaction(self):
        """Test putting a value without a transaction raises an error."""
        with self.assertRaises(Exception):  # Replace Exception with the specific error type if known
            self.db.put("A", 5)

    def test_transaction_commit(self):
        """Test that committing a transaction saves the value."""
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.db.commit()
        self.assertEqual(self.db.get("A"), 5)

    def test_transaction_rollback(self):
        """Test that rolling back a transaction reverts changes."""
        self.db.begin_transaction()
        self.db.put("B", 10)
        self.db.rollback()
        self.assertIsNone(self.db.get("B"))

    def test_commit_without_transaction(self):
        """Test that committing without an open transaction raises an error."""
        with self.assertRaises(Exception):  # Replace Exception with the specific error type if known
            self.db.commit()

    def test_rollback_without_transaction(self):
        """Test that rolling back without an open transaction raises an error."""
        with self.assertRaises(Exception):  # Replace Exception with the specific error type if known
            self.db.rollback()

    def test_multiple_transactions(self):
        """Test that multiple transactions work independently."""
        self.db.begin_transaction()
        self.db.put("C", 15)
        self.db.commit()

        self.db.begin_transaction()
        self.db.put("C", 20)
        self.db.rollback()

        self.assertEqual(self.db.get("C"), 15)  # Should still be 15 after rollback

    def test_commit_after_rollback(self):
        """Test that committing after a rollback works correctly."""
        self.db.begin_transaction()
        self.db.put("D", 25)
        self.db.rollback()

        self.db.begin_transaction()
        self.db.put("D", 30)
        self.db.commit()

        self.assertEqual(self.db.get("D"), 30)  # Should be 30 after commit

    def test_get_after_rollback(self):
        """Test that getting a value after rollback returns None."""
        self.db.begin_transaction()
        self.db.put("E", 35)
        self.db.rollback()

        self.assertIsNone(self.db.get("E"))  # Should return None after rollback

    def test_invalid_key_handling(self):
        """Test behavior with invalid keys."""
        with self.assertRaises(Exception):  # Replace Exception with the specific error type if known
            self.db.put(None, 5)  # Invalid key
        with self.assertRaises(Exception):  # Replace Exception with the specific error type if known
            self.db.get(None)  # Invalid key

if __name__ == '__main__':
    unittest.main()
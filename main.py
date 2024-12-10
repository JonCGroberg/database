from memory_db import MemoryDB

if __name__ == '__main__':
    db = MemoryDB()

    # should return None, because A doesn’t exist in the DB yet
    db.get("A")

    # should throw an error because a transaction is not in progress
    db.put("A", 5)

    # starts a new transaction
    db.begin_transaction()

    # set’s value of A to 5, but it's not committed yet
    db.put("A", 5)

    # should return None, because updates to A are not committed yet
    db.get("A")

    # update A’s value to 6 within the transaction
    db.put("A", 6)

    # commits the open transaction
    db.commit()

    # should return 6, that was the last value of A to be committed
    db.get("A")

    # throws an error, because there is no open transaction
    db.commit()

    # throws an error because there is no ongoing transaction
    db.rollback()

    # should return None because B does not exist in the database
    db.get("B")

    # starts a new transaction
    db.begin_transaction()

    # Set key B’s value to 10 within the transaction
    db.put("B", 10)

    # Rollback the transaction - revert any changes made to B
    db.rollback()

    # Should return None because changes to B were rolled back
    db.get("B")

class MemoryDB:
    def __init__(self) -> None:
        # kv pairs are of type string:int
        self.temp_values: dict[str, int] = dict()
        self.values: dict[str, int] = dict()
        self.transaction_in_progress: bool = False

    # only 1 transaction at a time may exist
    def begin_transaction(self):
        if self.transaction_in_progress:
            raise Exception("Transaction already in process")

        self.transaction_in_progress = True

    # create key if DNE, else create new. Throw exception if no current transaction
    def put(self, key: str, value: int) -> None:
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        elif key is None or not isinstance(key, str):
            raise Exception("Invalid key. Key must be a non-empty string.")

        self.temp_values[key] = value

    # Value or null. Only shows committed data
    def get(self, key: str) -> int | None:
        if key is None or not isinstance(key, str):
            raise Exception("Invalid key. Key must be a non-empty string.")

        if key in self.values:
            return self.values[key]
        else:
            return None

    # ends transaction and updates data
    def commit(self) -> None:
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")

        # update values with temp_values
        self.values.update(self.temp_values)
        self.temp_values.clear()
        self.transaction_in_progress = False

    # ends transaction and cancels
    def rollback(self) -> None:
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")

        self.temp_values.clear()
        self.transaction_in_progress = False

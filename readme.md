# In-Memory Key-Value Database

## Overview

This project implements an in-memory key-value database in Python, supporting basic operations such as `put`, `get`, `begin_transaction`, `commit`, and `rollback`. The database is designed to handle transactions, ensuring that changes are only visible after a commit and can be reverted with a rollback.

## Features

- Supports string keys and integer values.
- Allows for multiple transactions, ensuring data integrity.
- Provides error handling for invalid operations.

## Requirements

- Python 3.6 or higher
- `unittest` module (included in the standard library)

## Setup Instructions

1. **Clone the repository** to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure you have Python installed**. You can check your Python version with:

   ```bash
   python --version
   ```

3. **Run the tests** to ensure everything is working correctly:

   ```bash
   python -m unittest discover -s tests
   ```

4. **To run the main program**, execute:

   ```bash
   python main.py
   ```

## Usage

```python
from memory_db import MemoryDB

if __name__ == '__main__':
    db = MemoryDB()

    db.begin_transaction() # start a transaction
    db.put("A", 5) # add key value pair to staging
    db.commit() # move staging to database

    db.get("A") # returns 5
```

## Suggestions for future assignments

To enhance this assignment for future use, consider the following modifications:

- **Clarifications in Instructions**: Provide more detailed examples of expected input and output for each method, especially for edge cases. Additionally, clarify if any specific data structures may are expected or if students can solve for the requirments in any way.
- **Grading Improvements**: Implement automated grading scripts that can run the tests and check for specific outputs, making it easier to evaluate submissions consistently. Ideally the tests are prewritten, or are written by students included as part of the grade.
- **Documentation**: Include expectations for project struture, including documentation, tests, if main is needed or just the class, if using a class is the expected, etc...
- **Other** Do not include a writeup in the readme as this may not appear professional. Allows students to provide feedback in canvas or through form submission.

# 2025-1 S/W Engineering Project

## Testing with unittest

This project uses the `unittest` framework for testing. To run the tests, follow these steps:

### Prerequisites
Make sure you have Python installed along with the necessary dependencies. You can install the required packages using:

```bash
pip install -r requirements.txt
```

### Running Tests
To run the tests, navigate to the `src` directory in your terminal and use the following command:

```bash
python -m unittest discover -s test
```

- `-s test`: This specifies the starting directory for the test discovery. It will look for test files in the `test` directory.
- The test files should be named starting with `test` (e.g., `test_short_answer_quiz.py`).

### Important Note
When running the tests for the `ClozeQuizModel`, make sure to modify the `"dummy"` API key in `test_cloze_quiz.py` to your own API key for testing purposes.

### Test Structure
Each test file should contain classes that inherit from `unittest.TestCase`. Test methods should start with the word `test`. For example:

```python
import unittest
from quiz_generation.short_answer_quiz import ShortAnswerQuizModel

class TestShortAnswerQuizModel(unittest.TestCase):
    def test_pairs_creation(self):
        # Your test code here
```

### Example Test Command
To run all tests in the `test` directory, use:

```bash
python -m unittest discover -s test
```

This command will automatically find and execute all test cases defined in the test files.
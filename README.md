# SLAM-training-exercises
## About:
This repo contains python exercises used to help train new members of the FSAI SLAM team at the University of Bristol.
There are various exercises that will have users will have implement files directly in the src folder. The goal of the 
programme is to have the user build a basic functioning SLAM system in Python by the end of it, developing both their 
basic knowledge of SLAM and their programming skills.

## 1. Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.11 or newer**

Check your Python version by running:

```bash
python3 --version
```

If Python is not installed or your version is older than 3.11, download a compatible version from [python.org](https://www.python.org/downloads/).

## 2. Clone the Repository

Open a terminal and clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd slam-training
```

Replace `<repository-url>` with the URL provided by your team lead.

## 3. Create a Virtual Environment

A virtual environment isolates the project's Python packages from the rest of your computer.

This ensures everyone uses a consistent environment without interfering with other Python projects.

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

After activation, you should see `(.venv)` at the beginning of your terminal prompt.

Verify the Python version:

```bash
python --version
```

It should report Python 3.11 or newer.

> **Note:** You will need to activate the virtual environment each time you open a new terminal to work on the project.

## 4. Install Dependencies

With your virtual environment activated, run:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

This installs:

- The SLAM training package
- NumPy and SciPy for numerical computations
- pytest for running unit tests

The `-e` flag installs the project in *editable mode*, meaning changes to your source code are reflected immediately without reinstalling it.

All dependencies are configured in `pyproject.toml`.

## 5. Project Structure

```text
slam-training/
├── src/
│   └── slam/
│       ├── models.py
│       ├── estimation.py
│       └── ...
├── exercises/
│   ├── 01_states_and_sensors.md
│   └── ...
├── tests/
│   ├── test_models.py
│   ├── test_estimation.py
│   └── ...
├── pyproject.toml
└── README.md
```

- **`src/slam/`** — Contains the Python code you will implement.
- **`exercises/`** — Contains instructions for each exercise.
- **`tests/`** — Contains automated tests to check your implementations.
- **`pyproject.toml`** — Defines project dependencies and configuration.

## 6. Running Tests

We use **pytest** to automatically check whether your implementations are correct.

To run all tests:

```bash
python -m pytest
```

To run the tests for a specific exercise:

```bash
python -m pytest tests/test_models.py -v
```

The `-v` flag enables verbose output, showing the result of each individual test.

### Understanding Test Results

- **PASSED** — Your implementation satisfies the test.
- **FAILED** — Your implementation produced an incorrect result or raised an unexpected error.
- **ERROR** — pytest encountered a problem, such as an import error, while preparing or running the tests.

Tests for exercises you have not completed are expected to fail.

> Passing all provided tests is a useful correctness check, but does not necessarily guarantee your implementation is correct in every possible situation.

## 7. Completing the Exercises

Each exercise builds upon the previous exercises.

For each exercise:

1. Read the instructions in the corresponding Markdown file inside `exercises/`.
2. Locate the relevant Python files in `src/slam/`.
3. Complete the sections marked `TODO`.
4. Run the corresponding unit tests.
5. Debug your implementation until the tests pass.
6. Proceed to the next exercise.

Do not modify the provided tests to make your implementation pass.

You are encouraged to create additional tests to verify your own edge cases.

## 8. Troubleshooting

**Python version is incompatible**

Check that you are using Python 3.11 or newer:

```bash
python --version
```

If necessary, recreate the virtual environment using an explicitly installed compatible interpreter, such as `python3.11`.

**ModuleNotFoundError: No module named 'slam'**

Ensure the virtual environment is activated and the project has been installed:

```bash
python -m pip install -e ".[dev]"
```

**pytest command not found**

Run pytest through Python:

```bash
python -m pytest
```

**Tests fail immediately**

Check whether the relevant classes or functions are still unimplemented. Some tests will fail until you complete the corresponding exercise.

---

## Getting Started

Once you've completed the setup, begin with **Exercise 1: State and Sensor Readings** in the `exercises/` directory.

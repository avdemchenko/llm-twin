# Project Setup and Execution Guide

## Prerequisites

Before you begin, ensure you have [`uv`](https://github.com/astral-sh/uv) installed on your system.  
`uv` is an extremely fast Python package installer and resolver.

### Example installation on macOS/Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
````

---

## Getting Started

Follow these steps to set up the project and run the pipeline.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

---

### 2. Set Up the Environment

We'll use `uv` to create an isolated virtual environment.

```bash
# Create a virtual environment named .venv
uv venv

# Activate the environment
source .venv/bin/activate
```

---

### 3. Install Dependencies

Install the required Python packages using `uv`.

```bash
uv pip install zenml pandas pip
```

---

### 4. Configure and Run ZenML

#### a. (macOS Only) Set Environment Variable

If you are on macOS, run:

```bash
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```

> 💡 *Tip*: Add this line to your `~/.zshrc` or `~/.bash_profile` to apply it automatically in future terminal sessions.

#### b. Initialize ZenML Repository

```bash
zenml init
```

#### c. Start the ZenML Server

```bash
zenml up
```

> The ZenML dashboard will be available at [http://127.0.0.1:8237](http://127.0.0.1:8237).
> Keep this terminal running in the background.

---

### 5. Execute the Pipeline

Open a new terminal window, activate the virtual environment again, and run the pipeline script:

```bash
# Activate the environment
source .venv/bin/activate

# Run the pipeline
python run.py
```

---

## Verify the Pipeline Run

After executing `run.py`, you can view the results:

* Open the ZenML dashboard in your browser.
* Navigate to **Pipelines → Runs**.
* Locate the `my_first_pipeline` entry.
* Click on it to explore the run graph, inputs, and outputs of each step.


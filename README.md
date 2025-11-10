Deep Learning Course Projects

This repository contains my coursework, notes, and projects as I learn deep learning. The primary focus is on building and training neural networks using TensorFlow and Keras on an Apple Silicon Mac.

---

## 🛠️ Tech Stack

* **Python:** Specifically locked to `v3.11.x` for compatibility.
* **Deep Learning:** TensorFlow & Keras
* **GPU Acceleration:** `tensorflow-metal` (for Mac GPU)
* **Environment Management:** `uv`
* **Data Science Stack:** Jupyter, NumPy, Pandas, Matplotlib, Scikit-learn

---

## 🚀 How to Run This Project

This project requires a **very specific** setup to get TensorFlow, the Mac GPU, and `numpy` to work together correctly. Follow these steps exactly.

### 1. Clone the Repository

```bash
git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
cd YourRepoName
(Replace YourUsername and YourRepoName with your info)

2. Set Up the Python 3.11 Environment
This project must be run on Python 3.11. These commands will create the environment, lock the Python version in the project file, and install all packages in the correct, non-conflicting order.

Bash

# 1. Initialize the project
uv init

# 2. IMPORTANT: Open the 'pyproject.toml' file and
#    change the 'requires-python' line to:
#    requires-python = "==3.11.*"
#    ... then save the file.

# 3. Create a virtual environment using Python 3.11
# (uv will download it if you don't have it)
uv venv -p python3.11

# 4. Activate the new environment
source .venv/bin/activate

# 5. Install all packages in one command.
# This combination is a known-good, stable setup.
uv add tensorflow==2.16.1 tensorflow-metal==1.1.0 "numpy<2.0" jupyter pandas matplotlib scikit-learn

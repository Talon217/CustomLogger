<div align="center">

# 🪵 CustomLogger
### Zero-Dependency Python Logging Engine • Color-Coded Console • Rotating File Handlers

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Git Standards](https://img.shields.io/badge/Commits-Conventional_Commits-F05032?style=for-the-badge&logo=git&logoColor=white)](https://www.conventionalcommits.org/)

<br/>

> *A lightweight, drop-in Python logging setup designed for fast visual debugging and automated log rotation. Zero external dependencies—powered entirely by Python's standard library.*

</div>

---

## ✨ Features

* 🎨 **ANSI Color-Coded Console Output:** Clean visual hierarchy across `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` log levels.
* 🔄 **Automated File Rotation:** Built-in rotating file handler manages disk footprint without external tools.
* 📦 **Zero External Dependencies:** Built 100% on Python's native `logging` module—no third-party package overhead.
* 🔌 **Drop-In Integration:** Call `setup_logger()` once at application startup; all modular sub-loggers inherit configuration automatically.

---

## 📸 Visual Showcase

### Console Output
![Terminal Color Example](assets/terminal_example.png)

### File Output & Retention
![File Output Example](assets/file_example.png)

* **Disk Allocation:** Configured for `5 MB` per file with a default `3-file` backup pool.
* **Auto-Pruning:** Oldest records loop and purge automatically when size thresholds are reached.

---

## 📦 Installation

Install directly into any virtual environment or project using `pip`:

```bash
pip install git+[https://github.com/Talon217/CustomLogger.git](https://github.com/Talon217/CustomLogger.git)

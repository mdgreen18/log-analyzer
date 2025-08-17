# 📊 Log Analyzer CLI App

A simple command-line tool to read and analyze `.log` or `.txt` files.  
It provides useful statistics such as the number of lines processed, error counts, and the most common error message.  
Results can be exported as `.txt` or `.json`.

---

## ✨ Features
- Read from `.log` or `.txt` files
- Count:
  - Total lines processed
  - Lines containing `"ERROR"`
  - Most common error message
- Export summary as `.txt` or `.json`
- Simple CLI interface with arguments for:
  - `--file` → Path to the log file
  - `--format` → Export format (`txt` or `json`)
  - `--output` → Path to save summary

---

## 📦 Installation
1. **Clone the repository**
```bash
git clone https://github.com/mdgreen18/log-analyzer.git
cd log-analyzer
```

---

## 📂 Project Structure
```bash
log-analyzer/
│
├── logs/                     # Sample log files
│   └── sample.log
│
├── output/                   # Exported summaries
│
├── log_analyzer.py            # Main CLI app
├── requirements.txt           # Optional dependencies list
└── README.md
```

---

## 🛠 Development Notes

* This project is part of my Python learning journey focused on:

    * File I/O
    * Error handling
    * CLI formatting
    * Git branching + PR workflow

* The summary-feature branch was used to add CLI argument support via argparse.

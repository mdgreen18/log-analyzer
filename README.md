# 🔍 Log Analyzer – Coding Challenge

## 🧠 Problem Statement
You are tasked with building a **command-line log analyzer** in Python. The app should read from a `.txt` or `.log` file and generate a summary of the contents, particularly focusing on lines containing error messages.

This challenge is designed to help you practice **file handling**, **string parsing**, **exception control**, and **Git branching**.

---

## 📥 Input
You will be working with a text file that looks something like this:
```
INFO 2023-07-19 10:00:00 Server started
ERROR 2023-07-19 10:02:14 Failed to connect to database
WARNING 2023-07-19 10:03:10 High memory usage
ERROR 2023-07-19 10:04:12 Failed to connect to database
INFO 2023-07-19 10:05:00 Task complete
```

---

## 🎯 Requirements
1. Prompt the user for a file path (`input("Enter log file path: ")`)
2. Open the file and read all lines
3. Analyze the log and return the following:
   - ✅ Total number of lines
   - ✅ Number of lines that contain `"ERROR"`
   - ✅ Most common error message
4. Export the summary into a new file called `summary.txt` (or `.json` for bonus)

---

## ✅ Example Output (printed)
```
Analyzing log file...
Total lines: 5
Errors found: 2
Most common error: 'Failed to connect to database'
Summary written to summary.txt
```

---

## 💾 File Output Example (`summary.txt`)
```
Summary Report - Log Analyzer
------------------------------
Total Lines: 5
Error Count: 2
Most Common Error: Failed to connect to database
```

---

## ⚠️ Constraints
- Use `try/except` to handle:
  - File not found
  - Empty file
  - File encoding issues (optional)
- Modularize your code

---

## 🚀 Bonus Challenges
- Export the summary as `summary.json`
- Use `argparse` for CLI support
- Print script execution time

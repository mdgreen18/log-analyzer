import os
import json
from collections import Counter

def read_log_file(file_path):
    """Reads a log file and returns a list of lines."""
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return []

def analyze_logs(lines):
    """Analyzes log lines and returns summary stats."""
    total_lines = len(lines)
    error_lines = [line for line in lines if "ERROR" in line]
    error_count = len(error_lines)

    # Extract just the error messages (after "ERROR ")
    error_messages = [
        line.split("ERROR")[1].strip()
        for line in error_lines
        if "ERROR" in line
    ]

    most_common_error = None
    if error_messages:
        most_common_error, _ = Counter(error_messages).most_common(1)[0]

    return {
        "total_lines": total_lines,
        "error_count": error_count,
        "most_common_error": most_common_error
    }

def export_summary(summary, output_path, format="txt"):
    """Exports summary to a .txt or .json file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        if format == "json":
            with open(output_path, "w") as f:
                json.dump(summary, f, indent=4)
        else:  # default to txt
            with open(output_path, "w") as f:
                for key, value in summary.items():
                    f.write(f"{key}: {value}\n")
        print(f"✅ Summary exported to {output_path}")
    except Exception as e:
        print(f"❌ Error exporting summary: {e}")

def main():
    log_file_path = "logs/sample.log"  # Change if needed
    output_file_path = "output/summary.txt"  # Default output

    # Step 1: Read log file
    lines = read_log_file(log_file_path)
    if not lines:
        return

    # Step 2: Analyze logs
    summary = analyze_logs(lines)

    # Step 3: Export results
    export_summary(summary, output_file_path, format="txt")

if __name__ == "__main__":
    main()


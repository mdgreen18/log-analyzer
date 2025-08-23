import os
import json
import argparse
from collections import Counter

def read_log_file(file_path):
    """Reads a log file and returns a list of lines."""
    try:
        with open(file_path, "r", encoding="utf-16") as file:
            lines = [line.strip() for line in file if line.strip()] # remove blank lines
        return lines
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []
    except UnicodeError:
        # fallback if not UTF-16
        with open(file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return []

def analyze_logs(lines, top_n=None):
    """Analyzes log lines and returns summary stats."""
    total_lines = len(lines) 
    error_lines = [line for line in lines if "ERROR" in line]
    error_count = len(error_lines)

    # Extract just the error messages (after "ERROR ")
    error_messages = [
        line.split("ERROR", 1)[1].strip()
        for line in error_lines
        if "ERROR" in line
    ]

    # Count errors
    error_counts = Counter(error_messages)

    # Apply top N if argument is provided
    if top_n:
        error_counts = dict(error_counts.most_common(top_n)
    else:
        error_counts = dict(error_counts)

    most_common_error = None
    if error_messages:
        most_common_error, _ = Counter(error_messages).most_common(1)[0]

    return {
        "total_lines": total_lines,
        "error_count": error_count,
        "most_common_error": most_common_error,
        "error_counts": error_counts
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
    parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")
    parser.add_argument(
        "--file",
        type=str,
        default="logs/sample.log",
        help="Path to the log file to analyze"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["txt", "json"],
        default="txt",
        help="Export format for the summary"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output/summary.txt",
        help="Path to export the summary"
    )
    parser.add_argument(
        "--top",
        type=int,
        default=None,
        help="Show only the top N most common errors"
    )

    args = parser.parse_args()

    # Step 1: Read log file
    lines = read_log_file(args.file)
    if not lines:
        return
    
    # Step 2: Analyze logs
    summary = analyze_logs(lines, top_n=args.top)

    # Step 3: Export results
    export_summary(summary, args.output, args.format) 

if __name__ == "__main__":
    main()


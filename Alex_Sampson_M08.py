import os
import re
import argparse
import logging
from datetime import datetime

"""
Configure logging
"""
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

"""
Define regex patterns for secrets
"""
SECRET_PATTERNS = {
    "API Key": r"(?i)(api[_-]?key)[\"'\s:=]+[\"']?[A-Za-z0-9_\-]{16,}[\"']?",
    "Password": r"(?i)(password|passwd|pwd)[\"'\s:=]+[\"']?.{6,}[\"']?",
    "Token": r"(?i)(token|auth)[\"'\s:=]+[\"']?[A-Za-z0-9_\-]{16,}[\"']?",
    "Private Key": r"-----BEGIN PRIVATE KEY-----"
}

"""
Here are all the needed functions
"""
def scan_file(file_path):
    findings = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f, 1):
                for label, pattern in SECRET_PATTERNS.items():
                    match = re.search(pattern, line)
                    if match:
                        findings.append((label, file_path, i, match.group().strip()))
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
    return findings

def scan_directory(directory):
    all_findings = []
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            all_findings.extend(scan_file(path))
    return all_findings

def save_report(findings):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(desktop, f"secret_scan_report_{timestamp}.txt")

    try:
        with open(report_path, "w", encoding="utf-8") as report:
            for label, path, line_num, match in findings:
                report.write(f"[{label}] {path}:{line_num} → {match}\n")
        logging.info(f"Report saved to: {report_path}")
    except Exception as e:
        logging.error(f"Failed to save report: {e}")

def main():
    parser = argparse.ArgumentParser(description="Scan files for hardcoded secrets.")
    parser.add_argument("path", help="Path to file or directory to scan")
    args = parser.parse_args()

    target = args.path
    logging.info(f"Scanning target: {target}")

    if os.path.isfile(target):
        results = scan_file(target)
    elif os.path.isdir(target):
        results = scan_directory(target)
    else:
        logging.error("Invalid path provided.")
        return

    if results:
        print("\n🔍 Secrets Found:")
        for label, path, line_num, match in results:
            print(f"[{label}] {path}:{line_num} → {match}")
        save_report(results)
    else:
        print("✅ No secrets found.")

if __name__ == "__main__":
    main()

Secret Scanner CLI Tool 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This tool scans files or directories for hardcoded secrets using regular expressions. It detects patterns like API keys, passwords, tokens, and private keys, and saves a report to your desktop.


Features:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * Accepts a file or directory path as input
 * Uses regex to detect common secret patterns
 * Outputs findings with filename, line number, and matched string
 * Saves a .txt report to your desktop
 * Includes logging for traceability

Requirements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * Python 3.6 or higher
 * No external packages required

How to Run:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 1. Open your terminal or command prompt.
 2. Navigate to the folder containing secret_scanner.py.
 3. Run the script using the following command: python secret_scanner.py "C:\Path\To\Your\FileOrDirectory"

{Example: python secret_scanner.py "C:\Users\YourName\Documents\my_project"}

After running, the results will be printed to the terminal and saved to a file on your desktop named like:

{secret_scan_report_2025-10-19_18-25-00.txt}
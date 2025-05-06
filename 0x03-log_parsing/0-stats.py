#!/usr/bin/python3
"""Log parsing script"""
import sys
import signal

# Dictionary to store the count of status codes
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

total_size = 0
line_count = 0

def print_stats():
    """Prints the metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code]:
            print(f"{code}: {status_counts[code]}")

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()

        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = parts[-1]

            # Validate and update file size
            try:
                total_size += int(file_size)
            except Exception:
                pass

            # Validate and update status code count
            if status_code in status_counts:
                status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
finally:
    print_stats()


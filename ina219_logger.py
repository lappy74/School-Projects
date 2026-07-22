#!/usr/bin/env python3

import serial
from datetime import datetime
from pathlib import Path

PORT = "/dev/ttyACM0"
BAUD = 9600
OUTPUT_FILE = Path.home() / "ina219_log.txt"

with serial.Serial(PORT, BAUD, timeout=2) as ser:
    with OUTPUT_FILE.open("a", buffering=1) as file:
        if OUTPUT_FILE.stat().st_size == 0:
            file.write("computer_time,arduino_time_ms,voltage_V,current_mA\n")

        print(f"Logging from {PORT} at {BAUD} baud")
        print(f"Saving to: {OUTPUT_FILE}")
        print("Press Ctrl+C to stop.\n")

        while True:
            line = ser.readline().decode("utf-8", errors="replace").strip()

            if not line:
                continue

            timestamp = datetime.now().isoformat(timespec="seconds")
            output_line = f"{timestamp},{line}"

            print(output_line)
            file.write(output_line + "\n")

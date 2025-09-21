# Purpose: Develop a Python program that displays high-level CPU and memory information. This includes: CPU usage percentage, CPU count
# total memory available, and memory usage.

# Expected Result: The program should display CPU usage percentage, CPU count, total memory available, and memory usage

# References: 
# - https://psutil.readthedocs.io/en/latest/
# - https://docs.python.org/3/library/sys.html
# - https://www.juniper.net/documentation/us/en/software/junos/automation-scripting/topics/task/junos-python-modules-psutil-module.html
# - https://www.geeksforgeeks.org/python/how-to-catch-a-keyboardinterrupt-in-python/
# - https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

# Version   Author      Date            Description
# 1         Duke Pham   2025-09-19      Display high-level CPU and memory information

import psutil
import sys

def displayCpuRamInfo(value, total_width=50):

    # Generates a bar string based on a percentage value
    numChar = int(value / (100 / total_width))
    return "|" * numChar

try:
    print("-" * 100)
    print("Real-time CPU & Memory Usage (Press Ctrl+C to stop):")
    print("-" * 100)

    # Get CPU count and memory total  
    cpuCount = psutil.cpu_count(logical=True)
    memoryTotal = psutil.virtual_memory()
    memoryTitle = memoryTotal.total / (1024**3)

    # Print CPU count and memory total
    print(f"Total CPU Cores: {cpuCount}\nTotal RAM: {memoryTitle:5.5f} GB")
    
    print("-" * 100)
    
    print("\n")
    
    while True:
        # Get CPU usage over a second interval
        cpuUsage = psutil.cpu_percent(interval=1)
        
        # Get memory usage percentage
        memory = psutil.virtual_memory()
        memUsage = memory.percent
        
        # Create visual bars for metrics
        cpuBar = displayCpuRamInfo(cpuUsage)
        memoryBar = displayCpuRamInfo(memUsage)
        
        # Create the full output strings
        cpuLine = f"CPU: [{cpuBar:<50}] {cpuUsage:5.1f}%"
        memoryLine = f"RAM: [{memoryBar:<50}] {memUsage:5.1f}%"
        
        # Move cursor up two lines and print the new data
        sys.stdout.write(f"\033[F\033[F{cpuLine}\n{memoryLine}\n")
        sys.stdout.flush()
        
except KeyboardInterrupt:
    # Handle exit on Ctrl+C
    print("\n\nMonitoring stopped.")


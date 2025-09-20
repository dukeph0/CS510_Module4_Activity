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


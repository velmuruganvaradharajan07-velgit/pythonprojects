import matplotlib.pyplot as plt
import psutil
import time
from collections import deque

# Initialize data storage for CPU usage and time
cpu_percentages = deque(maxlen=60)  # Stores last 60 CPU percentages
timestamps = deque(maxlen=60)  # Stores corresponding timestamps

# Set up the plot for interactive mode
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-')  # Initialize an empty plot line

# Set plot labels and limits
ax.set_xlabel('Time (seconds ago)')
ax.set_ylabel('CPU Usage (%)')
ax.set_title('Real-time CPU Usage')
ax.set_ylim(0, 100)


def update_plot():
    """Updates the plot with new CPU data."""
    cpu = psutil.cpu_percent(interval=1)  # Get CPU percentage over 1 second
    current_time = time.time()

    cpu_percentages.append(cpu)
    timestamps.append(current_time)

    # Adjust x-axis to show relative time (seconds ago)
    relative_timestamps = [(current_time - ts) for ts in timestamps]

    line.set_data(relative_timestamps, cpu_percentages)
    ax.set_xlim(min(relative_timestamps), max(relative_timestamps))  # Adjust x-axis dynamically

    fig.canvas.draw()
    fig.canvas.flush_events()


# Main loop to continuously update the plot
while True:
    try:
        update_plot()
    except KeyboardInterrupt:
        print("Plotting stopped.")
        break
    time.sleep(0.1)  # Control update frequency
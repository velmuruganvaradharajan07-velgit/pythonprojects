import matplotlib.pyplot as plt

# Data for the x and y axes
x = [1, 2, 3, 4, 5]
y = [2, 5, 8, 12, 17]

# Create the plot
plt.plot(x, y)

# Add labels and a title for clarity
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Graph")

# Display the plot
plt.show()
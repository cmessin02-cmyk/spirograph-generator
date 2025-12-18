import numpy as np
import matplotlib.pyplot as plt
import colorsys

# Canvas setup
plt.figure(figsize=(8, 8))
plt.axis('off')
plt.gca().set_facecolor('black')

# Spirograph parameters
R = 180
r = 65
d = 100

theta = np.linspace(0, 20 * np.pi, 6000)

x = (R - r) * np.cos(theta) + d * np.cos(((R - r) / r) * theta)
y = (R - r) * np.sin(theta) - d * np.sin(((R - r) / r) * theta)

# Rainbow color gradient
colors = [colorsys.hsv_to_rgb(i / len(x), 1, 1) for i in range(len(x))]

for i in range(len(x) - 1):
    plt.plot(x[i:i+2], y[i:i+2], color=colors[i], linewidth=0.8)

# Save artwork
plt.savefig("spirograph.png", dpi=300, facecolor='black')
plt.close()

print("🎨 Generative art saved as spirograph.png")

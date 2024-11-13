import numpy as np
import matplotlib.pyplot as plt
print("Чтение файла ...")
data = np.loadtxt('../test.xyz')
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

print("Происходит конвертирование данных ...")
plt.figure(figsize=(10, 8))
plt.scatter(x, y, c=z, cmap='viridis')
plt.axis('off')
plt.savefig('output.jpeg', format='jpeg', dpi=300, bbox_inches='tight', pad_inches=0)  # Замените 'output.jpeg' на желаемое имя файла
plt.close()
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30)
plt.title('Histogram')
plt.xlabel("Wartość")
plt.ylabel("Częśtość")

plt.savefig('wykres.png')
plt.savefig('wykres.pdf')

plt.show()

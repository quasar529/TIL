import matplotlib.pyplot as plt

plt.title('plotting')
plt.plot([10, 20, 30, 40])
plt.show()

plt.title('legend')
plt.plot([10, 20, 30, 40], label='asc')
plt.plot([40, 30, 20, 10], label='desc')
plt.legend()
plt.show()

plt.title('color')
plt.plot([10, 30, 50, 70], 'pink', label='p')
plt.plot([80, 60, 40, 20], 'r', label='b')
plt.legend()
plt.show()

plt.title('linestyle')
plt.plot([10, 20, 30, 40], 'r--', label='dashed')
plt.plot([40, 30, 20, 10], 'b', linestyle=':', label='dotted')
plt.legend()
plt.show()

plt.title('marker')
plt.plot([10, 20, 30, 40], 'r.', label='circle')
plt.plot([40, 30, 20, 10], 'g^--', label='triangle up')
plt.legend(loc=7)
plt.show()

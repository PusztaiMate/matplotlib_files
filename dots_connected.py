import matplotlib.pyplot as plt
import numpy as np


FILENAME = '/home/pusztai/Documents/test_image.jpg'

x = [1, 2, 3]
y = [10, 17, 8]
err = [0.3, 1.2, 0.4]

x2 = [1, 2, 3]
y2 = [1, .3, 1.3]
err2 = [0.03, 0.01, 0.04]

names = ['250 bar', '450 bar', '650 bar']

fig, ax_left = plt.subplots(figsize=(8, 4))
ax_right = ax_left.twinx()

plt.ylim(0, 20)
ax_left.errorbar(x, y,
                 yerr=err,
                 linestyle=(1, (7, 14)),
                 marker='s',
                 color='black')
ax_left.set_ylabel('Szakítószilárdság')

plt.ylim(0, 2)
ax_right.errorbar(x2, y2,
                 yerr=err2,
                 linestyle=(1, (5, 10)),
                 marker='D',
                 color='black')
ax_right.set_ylabel('Nyomás a szerszámüregben')

locs, labels = plt.xticks()
ax_left.tick_params(axis='x', which='both',
                labelbottom=True, bottom=False)
plt.xticks(x, names)

print(f'saving to {FILENAME}')
plt.savefig(FILENAME, dpi=fig.dpi)
plt.show()
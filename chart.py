#簡単な五角形チャートを完成させるプログラム

import matplotlib.pyplot as plt
import numpy as np

PARAMETER_LIST = ['Attack', 'Defence', 'Speed', 'Luck', 'Intelligence', 'Skill']

values = np.array([4.5, 5, 3, 3, 2, 2])
LABELS = [ i for i in PARAMETER_LIST ]

rader_values = np.concatenate([values, [values[0]]])

angles = np.linspace(0, 2 * np.pi, len(LABELS) + 1, endpoint=True)
rgrids = [x for x in range(6)]

fig = plt.figure(facecolor='w')

ax = fig.add_subplot(1, 1, 1, polar=True)
ax.plot(angles, rader_values)
ax.fill(angles, rader_values, alpha=0.2)
ax.set_thetagrids(angles[:-1] * 180 / np.pi, LABELS)
ax.set_rgrids([])
ax.spines['polar'].set_visible(False)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

for grid_value in rgrids:
    grid_values = [grid_value] * (len(LABELS)+1)
    ax.plot(angles, grid_values, color='gray', linewidth=0.5)

for t in rgrids:
    ax.text(x=0, y=t, s=t)

ax.set_rlim([min(rgrids), max(rgrids)])

plt.savefig('Tetsutestu\'s_parameter.png')
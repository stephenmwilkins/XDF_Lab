

import numpy as np


import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from FLARE import filters
from FLARE import surveys
from FLARE import plt as fplt

fig = plt.figure(figsize = (5, 2))

left  = 0.15
bottom = 0.25
height = 0.7
width = 0.8

ax = fig.add_axes((left, bottom, width, height))




cmap = mpl.cm.rainbow
norm = mpl.colors.Normalize(vmin=3.5, vmax=4.2) # \AA


survey = 'XDF'
field = 'dXDF'

s = surveys.surveys[survey].fields[field]

print(s.filters)

filters_short = [f.split('.')[-1] for f in s.filters]

print(filters_short)

F = filters.add_filters(s.filters)



nJy_to_es = {f.split('.')[2]: F[f].nJy_to_es for f in F['filters']}
print(nJy_to_es)


for i,f in enumerate(F['filters']):

    pivwv = F[f].pivwv()
    c = cmap(norm(np.log10(pivwv)))
    ax.plot(np.log10(F[f].lam)-1, F[f].T, lw = 1, zorder = 1, c=c) # --- plot filter transmission curve
    ax.text(np.log10(pivwv)-1, np.max(F[f].T)+0.1, f.split('.')[-1], fontsize = 8, color = c, ha = 'center')
    ax.set_ylim([0,1.1])

ax.set_xlabel(r'$\rm log_{10}(\lambda/nm) $')
ax.set_ylabel(r'$\rm Transmission $')

fig.savefig(f'filters.pdf')
fig.savefig(f'filters.png')

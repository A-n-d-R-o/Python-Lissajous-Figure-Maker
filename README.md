<table align="center">
  <tr>
    <td><img src="Images/SL-1-1.25-1-1-0.png" width="250" /></td>
    <td><img src="Images/AL-1-1-1-1-1.5707963267948966-False-True-False-200-20.gif" width="250" /></td>
    <td><img src="Images/LW-1-1.5-1-1-0-True-True-True-200-20.gif" width="250" /></td>
  </tr>
</table>

# Python Lissajous Figure Maker
Python code for plotting Lissajous figures as either PNGs or GIFs through Matplotlib.

The code constructs Lissajous figures from the parametric equations $x = A_x \sin (\omega_x t)$ and $y = A_y \sin (\omega_y t + \phi)$. Where the values $A_x$, $\omega_x$, $A_y$, $\omega_y$ and $\phi$ can all be specified by the user. To achieve the animated figures, set `vary_phase` to True, which ignores any phase input, and automatically cycles $\phi$ through $0$ to $2 \pi$.

This code isn't designed to be efficient, and depending on the system this code is run on, it could take upwards of 2 minutes for high-resolution GIFs to be created. However, it is designed to be easily edited &mdash; figure sizes, number of samples, colours, etc. can all be tweaked to produce personalised figures.



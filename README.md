<table align="center">
  <tr>
    <td><img src="Images/SL-1-1.25-1-1-0.png" width="200" /></td>
    <td><img src="Images/AL-1-1-1-1-1.5707963267948966-False-True-False-200-20.gif" width="200" /></td>
    <td><img src="Images/LW-1-1.5-1-1-0-True-True-True-200-20.gif" width="200" /></td>
  </tr>
</table>

# Python Lissajous Figure Maker
Python code for plotting Lissajous figures as either PNGs or GIFs through Matplotlib.

The code constructs Lissajous figures from the parametric equations $x = A_x \sin (\omega_x t)$ and $y = A_y \sin (\omega_y t + \phi)$. Where the values $A_x$, $\omega_x$, $A_y$, $\omega_y$ and $\phi$ are all specified by the user. For the animated figures, setting `vary_phase=True` ignored any phase input, and automatically cycles $\phi$ through $0$ to $2 \pi$.

This code isn't designed to be efficient, and depending on the system this code is run on, it could take upwards of 2 minutes for high-resolution GIFs to be created.



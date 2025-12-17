## Contents

* [Required Packages](#required-packages)
* [Auxiliary Functions](#auxiliary-functions)
* [PNG Lissajous](#png-lissajous)
* [GIF Lissajous Without Waves](#gif-lissajous-without-waves)
* [GIF Lissajous With Waves](#gif-lissajous-with-waves)

<br>

---

## Required Packages
* `numpy`: for vast majority of mathematical functions used.
* `Fraction`: used once in the `joint_period` auxiliary function.
* `matplotlib.pyplot`: for plotting.
* `FuncAnimation`: for making the animations frame-by-frame.
* `PillowWriter`: to save the result as a GIF.
* `GridSpec`: for creating the 5-plot layout used in the `liss_and_waves` function.
* `IPython.display`, `HTML`: for immediately displaying GIFs, useful in Jupyter Notebook files.

<br>

---

## Auxiliary Functions

```python
def joint_period(omega_x, omega_y):
```
Given two angular frequencies, `omega_x` and `omega_y`, this function calculates the $x$ distance of the "overlapping period" of two sine waves with such angular frequencies &mdash; used to calculate the minimum interval for which to sample over to produce the Lissajous figures.

* `omega_x` (float): angular frequency of th $x$ wave.
* `omega_y` (float): angular frequency of the $y$ wave.

<br>

```python
def format_coeff(num):
```
A function for cleaning the coefficients of the plot's axes titles, for example, turning $1\sin 1x$ into $\sin x$.

* `num` (float): the coefficient in question, any one of: $A_x$, $\omega_x$, $A_y$, $\omega_y$.

<br>

```python
def format_phase(phi):
```
A function for cleaning the phase parameter.

* `phi` (float or str): the phase for the $y$ wave. If `phi='phi(t)'` is passed, the function will return `' + \phi(t)'` but only if `vary_phase=True`.

<br>

```python
def one_plot(A_x, omega_x, A_y, omega_y, phi):
```

Creates the single matplotlib plot used in the `still_liss` and `anim_liss` functions.

* `A_x` (float): amplitude of the $x$ wave.
* `omega_x` (float): angular frequency of the $x$ wave.
* `A_y` (float): amplitude of the $y$ wave.
* `omega_y` (float): angular frequency of the $y$ wave.
* `phi` (float): phase of the $y$ wave.

<br>

---

## PNG Lissajous

```python
def still_liss(A_x=1, omega_x=1, A_y=1, omega_y=1, phi=0, save=False):
```
The function that plots a still image of a Lissojous figure on a single plot.

* `A_x` (float): amplitude of the $x$ wave. Automatically set to 1.
* `omega_x` (float): angular frequency of the $x$ wave. Automatically set to 1.
* `A_y` (float): amplitude of the $y$ wave. Automatically set to 1.
* `omega_y` (float): angular frequency of the $y$ wave. Automatically set to 1.
* `phi` (float): phase of the $y$ wave. Automatically set to 0.
* `save` (bool): whether or not to save the image, defaulted to False.

Below is an example call and output to the function: 

`still_liss(omega_y=2.5, phi=np.pi/2, save=True)`

<p align="center">
  <img src="Images/SL_1_1_1_2.5_1.571.png" width="500"/>
</p>

<br>

---

## GIF Lissajous Without Waves

```python
def anim_liss(
    A_x=1, omega_x=1, A_y=1, omega_y=1, phi=0, draw=False, vary_phase=True, 
    show_dot=False, frames=200, fps=20, save=False, display=False
):
```

The function that plots a moving Lissajous figure, with any or none of: a varying phase, a white dot to trace the path, and a parameter to draw and erase the figure.

* `A_x` (float): amplitude of the $x$ wave. Automatically set to 1.
* `omega_x` (float): angular frequency of the $x$ wave. Automatically set to 1.
* `A_y` (float): amplitude of the $y$ wave. Automatically set to 1.
* `omega_y` (float): angular frequency of the $y$ wave. Automatically set to 1.
* `phi` (float): phase of the $y$ wave. Automatically set to 0.
* `draw` (bool): whether or not to *draw and erase* the Lissajous figure, defaulted to False.
* `vary_phase` (bool): varies the phase $\phi$ of the $y$ wave from $0$ to $2 \pi$ &mdash; this causes the Lissajous figure to "rotate". Defaulted to True.
* `show_dot` (bool): shows a white dot that traces the path of the Lissajous figure with time starting from $0$ and ending at the end of the cycle (`frames/fps`). Automically set to False.
* `frames` (int): the number of frames to show in the GIF, set to 200 by default.
* `fps` (int): the frames per second of the GIF, defualted to 20. Note: due to limitations of Matplotlib, the fps of the GIF has to be relativiely low (20 is recommended), else it will not produce a valid GIF file.
* `save` (bool): saves the created file when set to True, automatically set to False.
* `display` (bool): displays the figure as a HTML display object when set to True. Defaulted to False.

Note: setting all the above Boolean parameters to False produces a GIF with no movement &mdash; using `still_liss` would be more efficient if that effect is desired.

Example call and output:

`anim_liss(amp1=0.5, af1=0.9, draw=True, show_dot=False, vary_phase=True, frames=200, fps=20)`

<p align="center">
  <img src="Images/AL_0.5_0.9_1_1_0_True_True_False_200_20.gif" width="500"/>
</p>

<br>

---

## GIF Lissajous With Waves

```python
def liss_and_waves(
    A_x=1, omega_x=1, A_y=1, omega_y=1, phi=0, draw=False, vary_phase=True, 
    show_dot=False, frames=200, fps=20, save=False, display=False
):
```

Plots the standard Lissajous figure, with the same parameters as `anim_liss`, but instead surrounded by the the $x$ and $y$ waves to provide an intuition of the formation of the Lissajous figure.

* `A_x` (float): amplitude of the $x$ wave. Automatically set to 1.
* `omega_x` (float): angular frequency of the $x$ wave. Automatically set to 1.
* `A_y` (float): amplitude of the $y$ wave. Automatically set to 1.
* `omega_y` (float): angular frequency of the $y$ wave. Automatically set to 1.
* `phi` (float): phase of the $y$ wave. Automatically set to 0.
* `draw` (bool): whether or not to *draw and erase* the Lissajous figure, defaulted to False.
* `vary_phase` (bool): varies the phase $\phi$ of the $y$ wave from $0$ to $2 \pi$ &mdash; this causes the Lissajous figure to "rotate". Defaulted to True.
* `show_dot` (bool): shows a white dot that traces the path of the Lissajous figure with time starting from $0$ and ending at the end of the cycle (`frames/fps`). Automically set to False.
* `frames` (int): the number of frames to show in the GIF, set to 200 by default.
* `fps` (int): the frames per second of the GIF, defualted to 20. Note: due to limitations of Matplotlib, the fps of the GIF has to be relativiely low (20 is recommended), else it will not produce a valid GIF file.
* `save` (bool): saves the created file when set to True, automatically set to False.
* `display` (bool): displays the figure as a HTML display object when set to True. Defaulted to False.

Example call and output:

`liss_and_waves(A_y=0.25, omega_y=3, show_dot=True, save=True)`

<p align="center">
  <img src="Images/LW_1_1_0.25_3_0_False_True_True_200_20.gif" width="700"/>
</p>

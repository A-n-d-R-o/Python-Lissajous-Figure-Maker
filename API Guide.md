## Contents

* [Required Packages](#required-packages)
* [Auxiliary Functions](#auxiliary-functions)

<br>

---

## Required Packages
* `numpy`: for vast majority of mathematical functions used.
* `Fraction`: used once in the `joint_period` auxiliary function.
* `matplotlib`: for plotting the Lissajous figures and creating the PNGs and GIFs.

<br>

---

## Auxiliary Functions

```python
def joint_period(af1, af2):
```
Given two angular frequencies, `af1` and `af2`, this function calculates the $x$ distance of the "overlapping period" of two sine waves with those angular frequencies &mdash; used to calculate the minimum interval for which to sample over to produce the Lissajous figures.

* `af` (float): angular frequency of th $x$ wave.
* `af2` (float): angular frequency of the $y$ wave.

<br>

```python
def format_coeff(num):
```
A function for cleaning the coefficients of the plot axes' titles, for example, turning $1\sin 1x$ into $\sin x$.

* `num` (float): the coefficient in question, any on of: $A_x$, $\omega_x$, $A_y$, $\omega_y$.

<br>

```python
def format_phase(phi):
```
A function for cleaning the phase parameter.

* `phi` (float or str): the phase for the $y$ wave. If `phi='phi(t)'` is passed, the function will return `' + \phi(t)'` but only if `vary_phase=True`.

<br>

```python
def one_plot(amp1, af1, amp2, af2, phi):
```

Creates the single matplotlib plot used in the `still_liss` and `anim_liss` functions.

* `amp1` (float): amplitude of the $x$ wave.
* `af1` (float): angular frequency of the $x$ wave.
* `amp2` (float): amplitude of the $y$ wave.
* `af2` (float): angular frequency of the $y$ wave.
* `phi` (float): phase of the $y$ wave.

<br>

---

## PNG Lissagous

```python
def still_liss(amp1=1, af1=1, amp2=1, af2=1, phi=0):
```
The function that plots a still image of a Lissojous figure on a single plot.

* `amp1` (float): amplitude of the $x$ wave. Automatically set to 1.
* `af1` (float): angular frequency of the $x$ wave. Automatically set to 1.
* `amp2` (float): amplitude of the $y$ wave. Automatically set to 1.
* `af2` (float): angular frequency of the $y$ wave. Automatically set to 1.
* `phi` (float): phase of the $y$ wave. Automatically set to 0.

Below is an example call and output to the function:

`still_liss(af2=2.5, phi=np.pi/2)`

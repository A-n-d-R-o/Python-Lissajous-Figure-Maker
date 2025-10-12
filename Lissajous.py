import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.gridspec import GridSpec

'''auxilliary functions'''

def joint_period(af1, af2):

    if af1 == 0 or af2 == 0:
        return 2 * np.pi

    ratio = Fraction(af1 / af2).limit_denominator(1000)
    numerator = ratio.numerator

    joint_period = 2 * np.pi * numerator / af1

    return joint_period

def format_coeff(num):

    if num == 1:
        return ''
    if num == -1:
        return '-'

    return f'{round(num, 3)}'

def format_phase(phi):

    if phi == 'phi(t)':
        return ' + \phi(t)'
    
    if phi < 0:
        return f'{round(phi, 3)}'
    elif phi == 0:
        return ''
    elif phi > 0:
        return f' + {round(phi, 3)}'

def one_plot(amp1, af1, amp2, af2, phi):

    max_amp = max(amp1, amp2)
    scale = 1.2 * max_amp
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(-scale, scale)
    ax.set_ylim(-scale, scale)

    ax.set_xlabel(rf'$x = {format_coeff(amp1)}\sin({format_coeff(af1)}t)$')
    ax.set_ylabel(rf'$y = {format_coeff(amp2)}\sin({format_coeff(af2)}t{format_phase(phi)})$')

    ax.grid(True, color='grey', linestyle='-', linewidth=0.5, alpha=0.5)
    ax.set_aspect('equal')

    return fig, ax

'''PNG Lissagous'''

def still_liss(amp1=1, af1=1, amp2=1, af2=1, phi=0):

    interval = 2 * joint_period(af1, af2)
    t = np.linspace(0, interval, 1000)

    x = amp1 * np.sin(af1 * t)
    y = amp2 * np.sin(af2 * t + phi)

    fig, ax = one_plot(amp1, af1, amp2, af2, phi)
    
    plt.plot(x, y, color='orange', linewidth=2)
    plt.savefig(f'SL-{amp1}-{af1}-{amp1}-{af2}-{phi}.png')

'''GIF Lissagous without waves'''

def anim_liss(amp1=1, af1=1, amp2=1, af2=1, phi=0, draw=False, vary_phase=True, show_dot=False, frames=200, fps=20):

    interval = 2 * joint_period(af1, af2)
    t = np.linspace(0, interval, 1000)
    t_norm = t / (t[-1] - t[0]) * (frames / fps)
    
    if vary_phase:
        phases = np.linspace(0, 2*np.pi, frames)
        fig, ax = one_plot(amp1, af1, amp2, af2, 'phi(t)')
    else:
        fig, ax = one_plot(amp1, af1, amp2, af2, phi)
    
    liss_wave, = ax.plot([], [], color='orange', linewidth=2)
    liss_dot, = ax.plot([], [], color='white', marker='o')

    artists = [liss_wave, liss_dot]

    if draw:
        half_frames = frames // 2
    
    def init():

        for artist in artists:
            artist.set_data([], [])
    
        return artists
    
    def update(frame):

        if vary_phase:
            phase = phases[frame]
        else:
            phase = phi
        
        x = amp1 * np.sin(af1 * t)
        y = amp2 * np.sin(af2 * t + phase)

        index = int(frame / frames * (len(t)))
        x_point = x[index]
        y_point = y[index]
        t_point = t_norm[index]

        if draw:
            if frame < half_frames:
                liss_wave.set_data(x[:index+1], y[:index+1])
            else:
                liss_wave.set_data(x[index:], y[index:])
        else:
            liss_wave.set_data(x, y)
            
        if show_dot:
            liss_dot.set_data([x_point], [y_point])
        
        return artists
    
    anim = FuncAnimation(fig, update, frames=frames, init_func=init, interval=1000/fps, blit=True, repeat=True)
    
    anim.save(
        f'AL-{amp1}-{af1}-{amp2}-{af2}-{phi}-{draw}-{vary_phase}-{show_dot}-{frames}-{fps}.gif', 
        writer=PillowWriter(fps=fps)
             )

'''GIF Lissagous figure with waves'''

def liss_and_waves(amp1=1, af1=1, amp2=1, af2=1, phi=0, draw=False, vary_phase=True, show_dot=False, frames=200, fps=20):

    interval = 2 * joint_period(af1, af2)
    t = np.linspace(0, interval, 1000)
    t_norm = t / (t[-1] - t[0]) * (frames / fps)
    half_t = frames/fps/2

    if vary_phase:
        phases = np.linspace(0, 2*np.pi, frames)
    
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 10))
    gs = GridSpec(3, 3, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1], hspace=0.25, wspace=0.25)

    ax_liss = fig.add_subplot(gs[1, 1])
    ax_top = fig.add_subplot(gs[0, 1])
    ax_bottom = fig.add_subplot(gs[2, 1])
    ax_left = fig.add_subplot(gs[1, 0])
    ax_right = fig.add_subplot(gs[1, 2])

    max_amp = max(amp1, amp2)
    scale = 1.2 * max_amp
    
    ax_liss.set_xlim(-scale, scale)
    ax_liss.set_ylim(-scale, scale)
    ax_liss.set_aspect('equal')

    for ax in (ax_left, ax_right):
        ax.set_xlim(0, half_t)
        ax.set_ylim(-scale, scale)
        
    for ax in (ax_top, ax_bottom):
        ax.set_xlim(-scale, scale)
        ax.set_ylim(0, half_t)

    ax_liss.set_title('Lissajous Figure', fontsize=14)

    for ax in [ax_top, ax_bottom]:
        ax.set_title(rf'$x = {format_coeff(amp1)}\sin({format_coeff(af1)}t)$', fontsize=12)

    for ax in [ax_left, ax_right]:
        if vary_phase:
            ax.set_title(rf'$y = {format_coeff(amp2)}\sin({format_coeff(af2)}t + \phi(t))$', fontsize=12)
        else:
            ax.set_title(rf'$y = {format_coeff(amp2)}\sin({format_coeff(af2)}t{format_phase(phi)})$', fontsize=12)

    for ax in [ax_liss, ax_top, ax_bottom, ax_left, ax_right]:
        ax.grid(True, color='grey', linestyle='-', linewidth=0.5, alpha=0.5)

    liss_wave, = ax_liss.plot([], [], color='orange', linewidth=2)
    liss_dot, = ax_liss.plot([], [], color='white', marker='o')

    top_wave, = ax_top.plot([], [], color='blue', linewidth=2)
    top_dot, = ax_top.plot([], [], color='white', marker='o')
    bottom_wave, = ax_bottom.plot([], [], color='blue', linewidth=2)
    bottom_dot, = ax_bottom.plot([], [], color='white', marker='o')

    left_wave, = ax_left.plot([], [], color='red', linewidth=2)
    left_dot, = ax_left.plot([], [], color='white', marker='o')
    right_wave, = ax_right.plot([], [], color='red', linewidth=2)
    right_dot, = ax_right.plot([], [], color='white', marker='o')
    
    artists = [liss_wave, liss_dot, 
               top_wave, top_dot, 
               bottom_wave, bottom_dot, 
               left_wave, left_dot, 
               right_wave, right_dot]
    
    if draw:
        half_frames = frames // 2
        
    def init():
        
        for artist in artists:
            artist.set_data([], [])
            
        return artists

    def update(frame):
        
        if vary_phase:
            phase = phases[frame]
        else:
            phase = phi
        
        x = amp1 * np.sin(af1 * t)
        y = amp2 * np.sin(af2 * t + phase)

        index = int(frame / frames * len(t))
        x_point = x[index]
        y_point = y[index]
        t_point = t_norm[index]

        if draw:
            
            x_draw = x[:index+1]
            y_draw = y[:index+1]
            t_draw = t_norm[:index+1]
            
            x_erase = x[index:]
            y_erase = y[index:]
            t_erase = t_norm[index:]
            
            if frame < half_frames:
                liss_wave.set_data(x_draw, y_draw)
                
                t_draw_wrap = t_draw % half_t
                top_wave.set_data(x_draw, t_draw_wrap)
                bottom_wave.set_data(x_draw, t_draw_wrap)
                left_wave.set_data(t_draw_wrap, y_draw)
                right_wave.set_data(t_draw_wrap, y_draw)
            else:
                liss_wave.set_data(x_erase, y_erase)
                
                t_erase_wrap = t_erase % half_t
                t_erase_wrap[np.diff(np.r_[t_erase_wrap[0], t_erase_wrap]) < 0] = np.nan            
                top_wave.set_data(x_erase, t_erase_wrap)
                bottom_wave.set_data(x_erase, t_erase_wrap)
                left_wave.set_data(t_erase_wrap, y_erase)
                right_wave.set_data(t_erase_wrap, y_erase)
        else:
            liss_wave.set_data(x, y)
            top_wave.set_data(x, t_norm)
            bottom_wave.set_data(x, t_norm)
            left_wave.set_data(t_norm, y)
            right_wave.set_data(t_norm, y)
        
        if show_dot:
            liss_dot.set_data([x_point], [y_point])
        
            t_wrap = t_point % half_t
            top_dot.set_data([x_point], [t_wrap])
            bottom_dot.set_data([x_point], [t_wrap])
            left_dot.set_data([t_wrap], [y_point])
            right_dot.set_data([t_wrap], [y_point])

        return artists

    anim = FuncAnimation(fig, update, frames=frames, init_func=init, interval=1000/fps, blit=True, repeat=True)
    
    anim.save(
        f'LW-{amp1}-{af1}-{amp2}-{af2}-{phi}-{draw}-{vary_phase}-{show_dot}-{frames}-{fps}.gif', 
        writer=PillowWriter(fps=fps)
             )
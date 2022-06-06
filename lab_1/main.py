from my_var import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

init_number = 10

#creating a variation series
def generate_samps(n):
    samps = [Y() for i in range(n)]
    samps.sort()
    return samps


#generating empiciral func
def generate_data_for_F(n):
    samps = [L - 1, L] + generate_samps(n) + [R, R + 1]
    empiric = [0, 0] + [(i + 1) / n for i in range(n)] + [1, 1]
    return samps, empiric


if __name__ == "__main__":

    init_data = generate_data_for_F(init_number)

    #print()
    #print(f"n = {init_number}")
    #print("   y   |  F(y)")

    xdots, ydots = init_data
    '''
    for i in range(2, len(xdots) - 2):
        print("{:+.3f} | {:.3f}".format(xdots[i], ydots[i]))
    '''
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.25)

    my_x_plot = np.linspace(L - 1, R + 1, plot_dots)
    my_y_plot = [F(x) for x in my_x_plot]

    real_line, = plt.plot(my_x_plot, my_y_plot, linewidth=2, color='green')
    #check_line, = plt.plot(*init_data, linewidth=2, color='red')
    step_line, = plt.step(*init_data, where='post', linewidth=2, color='blue')


    #slider to change number
    my_slider = Slider(plt.axes([0.3, 0.12, 0.5, 0.03]), label='изменить количество = ', valmin=0, valmax=2000, valinit=10)


    def update(val):
        n = int(my_slider.val)
        data = generate_data_for_F(n)
        #theoretical_line.set_data(*data)
        step_line.set_data(*data)
        fig.canvas.draw_idle()


    my_slider.on_changed(update)

    button = Button(plt.axes([0.4, 0.04, 0.3, 0.05]), 'Новые значения')

    #generate new randomized value
    def new_paint(event):
        update(None)


    button.on_clicked(new_paint)

    plt.show()

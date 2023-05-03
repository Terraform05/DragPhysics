
def deriv(fxn, time_list, h=0.001):
    return (fxn(time_list + h) - fxn(time_list))/h

import numpy as np
def terminalvel(mass_kg, cross_section_area, drag_coeff, time_window, altitude_meters):
    rho = 1.225            
    g = 9.81
    time_list = np.linspace(0.01, time_window, 1000)

    def pos(time_list):
        return (mass_kg / (0.5*rho*cross_section_area*drag_coeff) ) * np.log( np.cosh( (np.sqrt(0.5*rho*cross_section_area*drag_coeff)*np.sqrt(g) * time_list)/np.sqrt(mass_kg) ) )

    #vel = d/dx of pos
    vel = deriv(fxn = pos, time_list = time_list)

    #F=mg−(.5(p v(time_list)^2 cross_section_area drag_coeff(d))
    #g – Gravitational acc; ρ – Density of fluid; v – vel of object; cross_section_area – Cross-sectional area; C_dC - Coefficient of drag
    acc = g - (0.5*rho*cross_section_area*drag_coeff / mass_kg)*vel**2

    import matplotlib.pyplot as plt
    plt.style.use("ggplot")
    #plot for terminal vel or for dropping from certain altitude
    def plot(time_list, vel, acc, altitude_meters = 0):
        plt.plot(time_list, pos(time_list), label = 'pos m')
        plt.plot(time_list, vel, label = 'vel m/s')
        plt.plot(time_list, acc, label = 'acc m/s^2', color = 'green')
        plt.xlim([time_list[0], time_list[-1]])
        plt.xlabel("Time (seconds)")
        plt.legend()
        vmax = vel[-1]
        t_vmax =time_list[np.where(vel==vmax)[0][0]]
        if altitude_meters != 0:
            title = "From %s m @ %0.02f sec: %0.02f m/s (%0.02f km/h)" %(altitude_meters, t_vmax, vel[-1], vel[-1]*3.6)
            plt.title(title)
            plt.savefig('altitude_meters.png')
        else: 
            title = "Over %s sec: Vmax @ %0.02f sec: %0.02f m/s (%0.02f km/h)" %(time_list[-1],t_vmax, vel[-1], vel[-1]*3.6)
            plt.title(title)
            plt.annotate('Terminal Velocity: (%s s, %0.02f m/s)'%(round(t_vmax,2),vel[-1]),
            xy=(t_vmax,vel[-1]), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='center')
            plt.savefig('terminal_velocity.png')

        plt.show()

    #plot to terminal vel
    plot(time_list, vel, acc)

    #plot to specified altitude_meters
    i_ground = 0
    for i, time in enumerate(time_list):
        if abs(pos(time) - altitude_meters)<=.1:
            i_ground = i
            break
    print(i_ground)

    plot(time_list[:i_ground], vel[:i_ground], acc[:i_ground], altitude_meters=5)

#drag coefficients
bellyhuman = 1
headhuman = 0.7
Sphere = 0.47
Cone = 0.50
Cube = 1.05

cubesidelengthCm = 15 #cm
cube_cross_section_area = (cubesidelengthCm/100)**2

terminalvel(0.110, cube_cross_section_area, Cube, 16, 5)
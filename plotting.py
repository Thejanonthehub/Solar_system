class Plot:
    def plt():

        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation
        import config
        o=config.Init


        fig = plt.figure()
        ax = plt.axes(projection='3d')

        object2_x = o.positions2[:,0]
        object2_y = o.positions2[:,1]
        object2_z = o.positions2[:,2]

        object1_x = o.positions1[:,0]
        object1_y = o.positions1[:,1]
        object1_z = o.positions1[:,2]

        object3_x = o.positions3[:,0]
        object3_y = o.positions3[:,1]
        object3_z = o.positions3[:,2]

        object4_x = o.positions4[:,0]
        object4_y = o.positions4[:,1]
        object4_z = o.positions4[:,2]

        object5_x = o.positions5[:,0]
        object5_y = o.positions5[:,1]
        object5_z = o.positions5[:,2]

        object6_x = o.positions6[:,0]
        object6_y = o.positions6[:,1]
        object6_z = o.positions6[:,2]

        object7_x = o.positions7[:,0]
        object7_y = o.positions7[:,1]
        object7_z = o.positions7[:,2]

        object8_x = o.positions8[:,0]
        object8_y = o.positions8[:,1]
        object8_z = o.positions8[:,2]

        object9_x = o.positions9[:,0]
        object9_y = o.positions9[:,1]
        object9_z = o.positions9[:,2]

# Create a figure and 3D axis
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': '3d'})


# Initialize empty lines
        object1_line, = ax.plot([], [], 'k.-', label='Sun', color='black',linewidth=0.5, markersize=11, markevery=[-1],markeredgecolor='magenta', markerfacecolor='Violet')
        object2_line, = ax.plot([], [], 'k.-', label='Earth', color='indigo',linewidth=0.5, markersize=10, markevery=[-1],markeredgecolor='Blue', markerfacecolor='Blue')
        object3_line, = ax.plot([], [], 'k.-', label='Venus', color='black',linewidth=0.5, markersize=8, markevery=[-1],markeredgecolor='green', markerfacecolor='green')
        object4_line, = ax.plot([], [], 'k.-', label='Mars', color='indigo',linewidth=0.5, markersize=5, markevery=[-1],markeredgecolor='purple', markerfacecolor='purple')
        object5_line, = ax.plot([], [], 'k.-', label='Jupiter', color='black',linewidth=0.5, markersize=20, markevery=[-1],markeredgecolor='white', markerfacecolor='brown')
        object6_line, = ax.plot([], [], 'k.-', label='Saturn', color='indigo',linewidth=0.5, markersize=16, markevery=[-1],markeredgecolor='Brown', markerfacecolor='brown')
        object7_line, = ax.plot([], [], 'k.-', label='Uranus', color='black',linewidth=0.5, markersize=14, markevery=[-1],markeredgecolor='grey', markerfacecolor='grey')
        object8_line, = ax.plot([], [], 'k.-', label='Neptune', color='indigo',linewidth=0.5, markersize=12, markevery=[-1],markeredgecolor='yellow', markerfacecolor='yellow')
        object9_line, = ax.plot([], [], 'k.-', label='Pluto', color='indigo',linewidth=0.5, markersize=10, markevery=[-1],markeredgecolor='red', markerfacecolor='red')


# Set axis limits
#ax.auto_scale_xyz(object1_x,object1_y,object1_z)
#ax.auto_scale_xyz(object2_x,object2_y,object2_z)
#ax.auto_scale_xyz(object3_x,object3_y,object3_z)
        ax.set_xlim3d([-2e11,50e11])
        ax.set_ylim3d([-2e11,50e11])
        ax.set_zlim3d([-2e11,2e4])
# Animation update function
        def update(frame):
    
    # Update the data of each line
            object1_line.set_data(object1_x[:frame+1], object1_y[:frame+1])
            object1_line.set_3d_properties(object1_z[:frame+1])

            object2_line.set_data(object2_x[:frame+1], object2_y[:frame+1])
            object2_line.set_3d_properties(object2_z[:frame+1])

            object3_line.set_data(object3_x[:frame+1], object3_y[:frame+1])
            object3_line.set_3d_properties(object3_z[:frame+1])

            object4_line.set_data(object4_x[:frame+1], object4_y[:frame+1])
            object4_line.set_3d_properties(object4_z[:frame+1])

            object5_line.set_data(object5_x[:frame+1], object5_y[:frame+1])
            object5_line.set_3d_properties(object5_z[:frame+1])

            object6_line.set_data(object6_x[:frame+1], object6_y[:frame+1])
            object6_line.set_3d_properties(object6_z[:frame+1])

            object7_line.set_data(object7_x[:frame+1], object7_y[:frame+1])
            object7_line.set_3d_properties(object7_z[:frame+1])

            object8_line.set_data(object8_x[:frame+1], object8_y[:frame+1])
            object8_line.set_3d_properties(object8_z[:frame+1])

            object9_line.set_data(object9_x[:frame+1], object9_y[:frame+1])
            object9_line.set_3d_properties(object9_z[:frame+1])


# Animate the plot
        anim = FuncAnimation(fig, update, frames=len(object1_x), interval=1, repeat=True)

# Set plot properties
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.set_title('Two Objects Animation')
        ax.legend()
        fig_manager = plt.get_current_fig_manager()
        fig_manager.full_screen_toggle()
        #anim.save('Solar_system.gif', writer='pillow')  # in order to save the animation to your computer...
# Display the animation
        plt.show()
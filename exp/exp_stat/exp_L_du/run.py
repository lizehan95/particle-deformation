from exp.exp_stat.experiment import run

### change parameters here
# number of particles
nums = 10

# time_step
delta_t = 0.0001

# how many steps (i.e. lines) in the grad file
steps = 40000

# calculate the deformation parameters or not
calc_para = False

# plot the trajectory in the screen or not
plot_traj = True

# save the trajectory in the desk "./img/" or not
save_traj = False

# shape
shape = 'l'

### end

if __name__ == '__main__':
    run(nums=nums, delta_t=delta_t, steps=steps, calc_para=calc_para, plot_traj=plot_traj, save_traj=save_traj, shape=shape)

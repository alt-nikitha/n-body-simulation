import numpy as np
import rebound
import matplotlib.pyplot as plt

sim = rebound.Simulation()
sim.units = ['mearth', 'day', 'AU']
# print(sim.units)
sim.add(m=40000)
sim.add(m=0.25, P=5, e=0.04)
sim.add(m=1.6, P=11)

# sim.integrate(100)
#simple plots
# change the interval size over which to integrate to get better plots
x_pos = np.empty((3,100))
y_pos = np.empty((3,100))
times = np.linspace(0,100,num=100)
for i,t in enumerate(times):
    sim.integrate(t)
    x_pos[0,i] = sim.particles[0].x
    y_pos[0,i] = sim.particles[0].y

    x_pos[1,i] = sim.particles[1].x
    y_pos[1,i] = sim.particles[1].y

    x_pos[2,i] = sim.particles[2].x
    y_pos[2,i] = sim.particles[2].y

# uncomment to plot x and y positions over time
# plt.scatter(x_pos,y_pos)
# plt.show()

#plot with time on x axis instead for above for loop
plt.plot(times, x_pos.T)
plt.plot(times,y_pos.T, '-')
plt.show()

#use rebound inbuilt plots, uncomment below and comment plots above

# rebound.OrbitPlot(sim)
# plt.show()
sim.status()
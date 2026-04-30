import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt("consolidated_300NMX4_new.csv", delimiter = ",", skip_header = 1)
time = data[:, 0]
R = data[:, 1]
dR_by_R = data[:, 2]
R_normalised = []
t_normalised = []
R_avg = []
N = 100000

len_R = len(R)
print(len_R)
window_size = int(0.025*len_R)
for i in range(len_R-window_size):
    R_avg.append(0.5*(max(R[i:i+window_size])+min(R[i:i+window_size])))
    R_normalised.append(R[i]/R_avg[i]-1)  
    t_normalised.append(time[i])

fig = plt.figure(figsize = (4,3))
ax = fig.add_subplot(111)
ax.plot(t_normalised, R_normalised)
# ax.plot(time[:window_size], R[:window_size])
ax.set_xlabel("Time (s)")
ax.set_ylabel(r"$\Delta R/R$")

plt.tight_layout()
plt.savefig("removed_slope_300NMX4.svg", format = "svg")
plt.savefig("removed_slope_300NMX4.png", format = "png")



fig2 = plt.figure(figsize = (4,3))
ax2 = fig2.add_subplot(111)
ax2.plot(time, R)
ax2.plot(t_normalised, R_avg)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel(r"$\Delta R / R$")

# ax.plot(time[:window_size], R[:window_size])
plt.tight_layout()
plt.savefig("with_slope_300NMX4.svg", format = "svg")
plt.savefig("with_slope_300NMX4.png", format = "png")

plt.show()
    
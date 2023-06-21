# import lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import csv file
csv_data = "Taipei_temp_record.csv"
temp_record = np.asarray(pd.read_csv(csv_data, sep=','))

# define function
def DFT(arr):
    N     = len(arr)                    # length of the time-dimension array
    arr   = arr.reshape((N, 1))
    omega = np.exp((0+1j)*(-2*np.pi/N)) # operator that needed in DFT

    n     = np.linspace(0, N-1, N).reshape((N, 1))
    k     = np.linspace(0, N-1, N).reshape((1, N))
    power = n*k
    lo    = omega**power

    arr_trans = np.matmul(lo, arr).reshape(N)           # DFT
    return arr_trans

def IDFT(arr):
    N     = np.size(arr)                # length of frequency-dimension array
    arr   = arr.reshape((N, 1))
    omega = np.exp((0+1j)*(-2*np.pi/N)) # operator that needed in DFT

    n     = np.linspace(0, N-1, N).reshape((N, 1))
    k     = np.linspace(0, N-1, N).reshape((1, N))
    power = n*k
    lo    = omega**power

    lo            = np.linalg.inv(lo)                     # do inverse process to linear operator
    arr_inv_trans = np.matmul(lo, arr).reshape(N)         # IDFT

    return arr_inv_trans

# plot the original figure of temperature record
fig = plt.figure(figsize = (8, 6))
plt.plot(temp_record[:, 1], color = 'blue')
plt.xlim([0, 144])
plt.ylim([13, 31])
plt.xticks(np.linspace(0, 144, 13))
plt.yticks(np.linspace(13, 31, 10))
plt.xlabel('Time series [Suppose Jan-09 as 0]', fontsize = 12, family = 'serif')
plt.ylabel(r'Temperature [$ ^\circ C$]', fontsize = 12, family = 'serif')
plt.title('Temperature (Taipei) as time series', fontsize = 15, family = 'serif')
plt.grid()
plt.savefig('Original_record.png', dpi = 500)
plt.show()


# Using DFT function to make frequency-domain profile
temp_DFT = DFT(temp_record[:, 1])         # conducting DFT on temp_record array

temp_DFT_real = np.empty_like(temp_DFT)   # ask for real part of complex value
for i in range(len(temp_DFT_real)):
    temp_DFT_real[i] = np.real(temp_DFT[i])
    print(temp_DFT_real[i])

# plot temperature on frequency-domain
fig = plt.figure(figsize = (8, 6))
plt.plot(temp_DFT_real, color = 'blue')
plt.xlim([0, 144])
plt.ylim([-500, 3500])
plt.xticks(np.linspace(0, 144, 13))
plt.yticks(np.linspace(-500, 3500, 9))
plt.xlabel('Time Series', fontsize = 12, family = 'serif')
plt.ylabel('Frequency Intensity', fontsize = 12, family = 'serif')
plt.title('Frequency Intensity as Time Series', fontsize = 15, family = 'serif')
plt.grid()
plt.savefig('Frequency_Intensity.png', dpi = 500)
plt.show()


# Using IDFT function to transform frequency-domain into time-domain
temp_IDFT = IDFT(temp_DFT)                  # conducting IDFT on temp_DFT array

temp_IDFT_real = np.empty_like(temp_DFT)    # ask for real part of complex value
for i in range(len(temp_DFT_real)):
    temp_IDFT_real[i] = np.real(temp_IDFT[i])

# plot temperature on time-domain
fig = plt.figure(figsize = (8, 6))
plt.plot(temp_IDFT_real, color = 'blue')
plt.xlim([0, 144])
plt.ylim([13, 31])
plt.xticks(np.linspace(0, 144, 13))
plt.yticks(np.linspace(13, 31, 10))
plt.xlabel('Time Series', fontsize = 12, family = 'serif')
plt.ylabel(r'Temperature [$ ^\circ C$]', fontsize = 12, family = 'serif')
plt.title('Temperature as Time Series', fontsize = 15, family = 'serif')
plt.grid()
plt.savefig('Temperature_trans.png', dpi = 500)
plt.show()



# plot power spectrum of the temperature record
power_spec = temp_DFT*np.conjugate(temp_DFT)/len(temp_DFT)**2

fig = plt.figure(figsize = (8, 6))
plt.plot(power_spec[:21])
plt.xlim([0, 20])
plt.ylim([0, 600])
plt.xticks(np.linspace(0, 20, 6))
plt.yticks(np.linspace(0, 600, 13))
plt.xlabel('Time Series', fontsize = 12, family = 'serif')
plt.ylabel('Power Spectrum', fontsize = 12, family = 'serif')
plt.title('Power Spectrum as Time Series', fontsize = 15, family = 'serif')
plt.grid()
plt.savefig('Power_Spectrum.png', dpi = 500)
plt.show()



# highlight the lower value area

fig = plt.figure(figsize = (8, 6))
plt.plot(power_spec[:21])
plt.xlim([0, 20])
plt.ylim([0, 50])
plt.xticks(np.linspace(0, 20, 6))
plt.yticks(np.linspace(0, 50, 6))
plt.xlabel('Time Series', fontsize = 12, family = 'serif')
plt.ylabel('Power Spectrum', fontsize = 12, family = 'serif')
plt.title('Power Spectrum as Time Series', fontsize = 15, family = 'serif')
plt.grid()
plt.savefig('Power_Spectrum_lower.png', dpi = 500)
plt.show()
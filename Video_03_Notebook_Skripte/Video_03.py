import numpy as np
import matplotlib.pyplot as plt

# load data (expects CSV mit Header: date,value)
data = np.genfromtxt('data.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')
dates = np.array(data['date'], dtype='datetime64[D]')
values = data['value'].astype(float)

# function to compute moving average
def moving_average_np(x, window):
    w = np.ones(window, dtype=float)
    num = np.convolve(x, w, mode='same')
    den = np.convolve(np.ones_like(x), w, mode='same')
 
    return num / den

# plot and explore your data 
# (test different window sizes for MA etc.)
window = 7
sm = moving_average_np(values, window)

plt.figure(figsize=(8,4))
plt.plot(dates[window:-window], 
         values[window:-window], "o", label='Rohdaten', alpha=0.4)
plt.plot(dates[window:-window], 
         sm[window:-window], 
         label=f'{window}er gleitender Mittelwert', color='C1', linewidth=2)
plt.legend()
plt.tight_layout()
plt.show()

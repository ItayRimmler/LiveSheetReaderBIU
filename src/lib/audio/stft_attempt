import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft
import sounddevice as sd

# Parameters
sample_rate = 11025  # Sample rate in Hz
duration = 5        # Total duration for recording in seconds

# Record audio for the specified duration
print("Recording for 5 second...")
recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
sd.wait()  # Wait until the recording is finished
print("Recording finished.")

# Perform STFT
f, t, Zxx = stft(recording.flatten(), fs=sample_rate, nperseg=256)

# Plot spectrogram
plt.figure(figsize=(10, 8))
plt.pcolormesh(t, f, 20 * np.log10(np.abs(Zxx)), shading='gouraud', cmap='jet')  # Spectrogram in dB scale
plt.title('Spectrogram', fontsize=16)
plt.ylabel('Frequency [Hz]', fontsize=14)
plt.xlabel('Time [sec]', fontsize=14)
plt.colorbar(label='Magnitude [dB]')
plt.tight_layout()
plt.show()

# Access the first segment of time (for example):
first_time_segment = Zxx[:, 0]  # Complex values for all frequencies
first_time_segment_magnitude = np.abs(first_time_segment)  # Magnitude for all frequencies

# We can look for the highest absolute value among the frequencies in the first time segment:

max_magnitude = np.max(first_time_segment_magnitude)

# and for all the time segments we shall get:
amount_of_time_segments=Zxx.shape[1]
array_of_the_most_dominant_frequencies=np.zeros(amount_of_time_segments)
for i in range(amount_of_time_segments):
    array_of_the_most_dominant_frequencies[i] = np.max(np.abs(Zxx[:, i]))

plt.figure()
plt.plot(array_of_the_most_dominant_frequencies)
plt.show()

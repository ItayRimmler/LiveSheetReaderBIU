#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>

// Assuming FFTW is used for the FFT computation
#include <fftw3.h>  // FFTW library for fast Fourier transform

using namespace std;

// Example Hamming window function
vector<double> hamming_window(int N) {
    vector<double> window(N);
    for (int n = 0; n < N; ++n) {
        window[n] = 0.54 - 0.46 * cos((2 * M_PI * n) / (N - 1));
    }
    return window;
}

// Perform STFT on the input signal
vector<vector<complex<double>>> stft(const vector<double>& signal, int window_size, int hop_size) {
    vector<vector<complex<double>>> result;
    vector<double> window = hamming_window(window_size);  // Apply Hamming window

    int num_windows = (signal.size() - window_size) / hop_size + 1;

    // FFTW setup
    fftw_complex *in, *out;
    fftw_plan p;

    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * window_size);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * window_size);
    p = fftw_plan_dft_1d(window_size, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    // Iterate over the signal in steps of hop_size
    for (int i = 0; i < num_windows; ++i) {
        // Apply window to the current frame
        vector<complex<double>> frame(window_size);
        for (int j = 0; j < window_size; ++j) {
            frame[j] = signal[i * hop_size + j] * window[j];
            in[j][0] = frame[j].real();  // Real part
            in[j][1] = 0.0;  // Imaginary part (0 for real signal)
        }

        // Perform FFT
        fftw_execute(p);

        // Store the FFT result (complex numbers)
        vector<complex<double>> fft_result(window_size);
        for (int k = 0; k < window_size; ++k) {
            fft_result[k] = complex<double>(out[k][0], out[k][1]);
        }

        // Append result to the output
        result.push_back(fft_result);
    }

    // Clean up FFTW resources
    fftw_destroy_plan(p);
    fftw_free(in);
    fftw_free(out);

    return result;
}
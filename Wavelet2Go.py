import numpy as np
import pywt


class Wavelet2Go:
    def __init__(self, f_n: int, f_min: float, f_max: float, dt: float) -> None:
        self.number_of_frequences: np.ndarray = np.array(int(f_n))
        self.frequency_range: np.ndarray = np.array((f_min, f_max))
        self.dt: np.ndarray = np.array(dt)

        self.s_spacing: np.ndarray = (1.0 / (self.number_of_frequences - 1)) * np.log2(
            self.frequency_range.max() / self.frequency_range.min()
        )

        self.scale: np.ndarray = np.power(
            2, np.arange(0, self.number_of_frequences) * self.s_spacing
        )

        self.frequency_axis: np.ndarray = self.frequency_range.min() * np.flip(
            self.scale
        )
        self.wave_scales: np.ndarray = 1.0 / (self.frequency_axis * self.dt)

        self.frequency_axis = (
            pywt.scale2frequency("cmor1.5-1.0", self.wave_scales) / self.dt
        )

        self.mother = pywt.ContinuousWavelet("cmor1.5-1.0")

        self.cone_of_influence: np.ndarray = np.ceil(
            np.sqrt(2) * self.wave_scales
        ).astype(np.int64)

    def get_frequency_axis(self) -> np.ndarray:
        return self.frequency_axis

    def get_time_axis(self, data: np.ndarray) -> np.ndarray:
        time_axis = np.linspace(0.0, data.shape[0] * self.dt, data.shape[0])
        return time_axis

    def perform_transform(self, data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        complex_spectrum, frequency_axis = pywt.cwt(
            data, self.wave_scales, self.mother, self.dt
        )
        return complex_spectrum, frequency_axis
        
    def mask_invalid_data(
        self, complex_spectrum: np.ndarray, fill_value: float = 0
    ) -> np.ndarray:
        assert complex_spectrum.shape[0] == self.cone_of_influence.shape[0]

        for frequency_id in range(0, self.cone_of_influence.shape[0]):
            # Front side
            start_id: int = 0
            end_id: int = int(
                np.min(
                    (self.cone_of_influence[frequency_id], complex_spectrum.shape[1])
                )
            )
            complex_spectrum[frequency_id, start_id:end_id] = fill_value
    
            start_id = np.max(
                (
                    complex_spectrum.shape[1]
                    - self.cone_of_influence[frequency_id]
                    - 1,
                    0,
                )
            )
            end_id = complex_spectrum.shape[1]
            complex_spectrum[frequency_id, start_id:end_id] = fill_value
    
        return complex_spectrum
            
    def get_y_ticks(self, reduction_to: int) -> tuple[np.ndarray, np.ndarray]:
        output_ticks = np.arange(
            0,
            self.frequency_axis.shape[0],
            int(np.floor(self.frequency_axis.shape[0] / reduction_to)),
        )
        output_freq = self.frequency_axis[output_ticks]
        
        return output_ticks, output_freq
    
    def get_x_ticks(self, reduction_to: int, data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        time_axis = self.get_time_axis(data)
        output_ticks = np.arange(
            0, time_axis.shape[0], int(np.floor(time_axis.shape[0] / reduction_to))
        )
        output_time_axis = time_axis[output_ticks]
    
        return output_ticks, output_time_axis


if __name__ == "__main__":
    pass
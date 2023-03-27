from torchaudio.prototype.functional import adsr_envelope
from dataclasses import dataclass


@dataclass
class ADSR:
    attack: float = 0.2
    hold: float = 0.2
    decay: float = 0.2
    sustain: float = 0.5
    release: float = 0.2
    n_decay: int = 1

    def __init__(self):
        pass

    def __call__(self, x):
        env = adsr_envelope(
            num_frames=len(x),
            attack=self.attack,
            hold=self.hold,
            decay=self.decay,
            sustain=self.sustain,
            release=self.release,
            n_decay=self.n_decay,
        )
        return env * x

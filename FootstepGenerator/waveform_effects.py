import os
from pedalboard import Gain, LowpassFilter, Pedalboard, PitchShift, Reverb
from pedalboard.io import AudioFile
import random

effect_chain = Pedalboard()


def apply_pitch_shift(pitch_shift=None):
    global effect_chain

    if pitch_shift is None:
        pitch_shift = _random_pitch_shift()

    pitch_effect = PitchShift(pitch_shift)
    effect_chain.append(pitch_effect)


def _random_pitch_shift():
    mean = 0
    std_dev = 2.5

    while True:
        pitch_shift = random.gauss(mean, std_dev)

        if abs(pitch_shift) <= std_dev:
            break

    return pitch_shift


def apply_low_pass_filter(frequency=750):
    global effect_chain
    effect_chain.append(LowpassFilter(frequency))


def apply_reverb(room_size=0.8, damping=0.5, wet_level=0.5, dry_level=0.3):
    global effect_chain
    width = 1.0
    freeze_mode = 0
    effect_chain.append(Reverb(room_size, damping, wet_level, dry_level, width, freeze_mode))


def apply_gain(bias=0, variation=0.3):
    global effect_chain
    offset = random.uniform(variation * -1.0, variation)
    print("Offset: " + offset)
    effect_chain.append(Gain(bias + offset))
        

def apply_effects_chain():
    samplerate = 44100.0

    with AudioFile("media/stitched_pairs/stitched_pair.wav").resampled_to(samplerate) as f:
        audio = f.read(f.frames)

    output = effect_chain(audio, samplerate)

    filename = "output.wav"
    destination_directory = "media/output/"
    output_filepath = os.path.join(destination_directory, filename)

    with AudioFile((output_filepath), 'w', samplerate, output.shape[0]) as f:
        f.write(output)

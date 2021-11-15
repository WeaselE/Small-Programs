#

import librosa as lb

file = lb.example('nutcracker')

waveform, sample_rate = lb.load(file)

tempo, beat_frames = lb.beat.beat_track(y=waveform, sr=sample_rate)

print('Estimated Tempo: {:.2f} bpm'.format(tempo))

beat_times = lb.frames_to_time(beat_frames, sr=sample_rate)
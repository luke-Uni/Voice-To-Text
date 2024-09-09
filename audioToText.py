import pydub

# Original audio file path
audio = pydub.AudioSegment.from_file(original_audio_path)

wav_audio_path = "C:\Users\cefar\Downloads\WhatsApp_Audio.wav"
audio.export(wav_audio_path, format="wav")

# Load the .wav audio file
audio = pydub.AudioSegment.from_file(wav_audio_path)

# Determine the length of each segment (in milliseconds)
segment_length = len(audio) // 4

# Create 4 smaller segments
segments = [audio[i*segment_length:(i+1)*segment_length] for i in range(4)]

# Export the segments as separate files
segment_paths = []
for i, segment in enumerate(segments):
    segment_path = f"/mnt/data/audio_segment_{i+1}.wav"
    segment.export(segment_path, format="wav")
    segment_paths.append(segment_path)

segment_paths

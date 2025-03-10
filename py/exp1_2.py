import sounddevice as sd
import soundfile as sf
import numpy as np

# 1. 读取音频文件
input_file = "D:/py/data/music.wav"
output_file = "D:/py/data/music_modified.wav"

data, sample_rate = sf.read(input_file)

# 2. 计算每秒的样本数
samples_per_sec = sample_rate

# 3. 计算音频总时长（秒）
duration_sec = len(data) // samples_per_sec

# 4. 分割音频并移除偶数秒
segments = []
for i in range(duration_sec):
    start_sample = i * samples_per_sec
    end_sample = (i + 1) * samples_per_sec

    # 只保留奇数秒（索引为偶数）
    if i % 2 == 0:
        segment = data[start_sample:end_sample]
        segments.append(segment)

# 5. 拼接所有保留的片段
if segments:
    modified_data = np.concatenate(segments, axis=0)
else:
    modified_data = np.array([], dtype=data.dtype)

# 6. 播放修改后的音频
sd.play(modified_data, sample_rate)
sd.wait()  # 等待播放完成

# 7. 保存修改后的音频文件
sf.write(output_file, modified_data, sample_rate)

print(f"已保存修改后的音频到 {output_file}")

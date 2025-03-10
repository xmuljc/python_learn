from collections import Counter
import matplotlib.pyplot as plt
import string
import random
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# 1. 生成随机英文段落
print("生成随机英文段落")


def generate_random_text(length=500):
    words = ["".join(random.choices(string.ascii_letters + " ",
                     k=random.randint(3, 10))) for _ in range(length)]
    return " ".join(words)


# 生成并写入文件
file_path = "alphatwice.txt"
text = generate_random_text()
with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

# 2. 统计字母出现次数（区分大小写）
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    letter_counts = Counter(c for c in content if c in string.ascii_letters)

# 3. 选取出现次数最高的 10 个字母
top_letters = letter_counts.most_common(10)
letters, counts = zip(*top_letters)

# 4. 绘制直方图
plt.figure(figsize=(10, 5))
plt.bar(letters, counts, color='skyblue')
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.title("Top 10 Most Frequent Letters")
plt.savefig("D:/py/data/letter_top.png")  # 保存图片
plt.show()

print(f"已生成 {file_path} 并统计字母频率，直方图已保存为 letter_histogram.png")

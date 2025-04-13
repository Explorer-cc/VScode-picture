import re
from pathlib import Path

# 定义支持的图片扩展名
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}

# 获取当前文件夹路径
current_folder = Path('.')
image_files = [f for f in current_folder.iterdir() if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS]

# 正则表达式匹配 vsc-bg-数字 格式的文件名
pattern = re.compile(r'^vsc-bg-(\d+)$')
existing_numbers = []
non_vsc_files = []

for img_file in image_files:
    stem = img_file.stem
    match = pattern.match(stem)
    if match:
        # 提取数字部分并保存
        num = int(match.group(1))
        existing_numbers.append(num)
    else:
        # 记录需要重命名的文件
        non_vsc_files.append(img_file)

# 确定起始序号
max_number = max(existing_numbers) if existing_numbers else 0
start_number = max_number + 1

# 重命名不符合规则的文件
for index, img_file in enumerate(non_vsc_files, start=start_number):
    new_name = f"vsc-bg-{index}{img_file.suffix}"
    new_path = img_file.with_name(new_name)
    img_file.rename(new_path)
    print(f"Renamed: {img_file.name} -> {new_name}")

print("重命名完成！")
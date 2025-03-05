import os
from pathlib import Path

# 定义支持的图片扩展名
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}

# 获取当前文件夹路径
current_folder = Path('.')

# 获取当前文件夹下所有文件
files = list(current_folder.iterdir())

# 过滤出图片文件
image_files = [f for f in files if f.suffix.lower() in IMAGE_EXTENSIONS]

# 按遍历顺序重命名
for index, image_file in enumerate(image_files, start=1):
    new_name = f"vsc-bg-{index}{image_file.suffix}"
    new_path = image_file.with_name(new_name)
    
    # 重命名文件
    image_file.rename(new_path)
    print(f"Renamed: {image_file.name} -> {new_name}")

print("重命名完成！")
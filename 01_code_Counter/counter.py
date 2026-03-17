import os

def count_code(root_dir):
    # 定义我们要统计的文件后缀
    target_exts = {'.cpp', '.py', '.c', '.h'}
    stats = {ext: 0 for ext in target_exts}
    total_lines = 0

    print(f"\n🚀 正在扫描目录: {os.path.abspath(root_dir)}")
    print("-" * 40)

    for root, dirs, files in os.walk(root_dir):
        # 排除掉不需要扫描的隐藏文件夹（如 .git）
        if '.git' in root: continue
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in target_exts:
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = len(f.readlines())
                        stats[ext] += lines
                        total_lines += lines
                        print(f"📄 Found: {file:<20} | {lines:>5} lines")
                except Exception as e:
                    print(f"❌ Error reading {file}: {e}")

    print("-" * 40)
    print("📊 统计报告 (Stats Report):")
    for ext, count in stats.items():
        if count > 0:
            print(f"  {ext}: {count} lines")
    print(f"\n✨ 总代码量: {total_lines} 行")
    print("💡 Motto: There is nothing I cannot learn.")
    print("-" * 40)

if __name__ == "__main__":
    # 统计当前仓库及父级目录下的代码量
    count_code('E:\yan-lab') 

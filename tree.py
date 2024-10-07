import os


def print_directory_structure(startpath, output_file="tree.txt"):
    with open(output_file, "w") as f:
        for root, dirs, files in os.walk(startpath):
            if "venv" in root:
                continue
            if ".git" in root:
                continue

            level = root.replace(startpath, "").count(os.sep)
            indent = " " * 4 * level
            f.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = " " * 4 * (level + 1)
            for file in files:
                f.write(f"{subindent}{file}\n")


# 사용 예시:
print_directory_structure(".")

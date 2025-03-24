import os

def generate_inno_files_section(output_file="inno_files.txt"):
    base_dir = os.getcwd()
    files_section = "[Files]\n"
    
    for root, dirs, files in os.walk(base_dir):
        if root == base_dir:
            for dir_name in dirs:
                source_path = os.path.join(root, dir_name)
                files_section += f'Source: "{source_path}\\*"; DestDir: "{{app}}\\{dir_name}"; Flags: ignoreversion recursesubdirs createallsubdirs\n'
            
            for file_name in files:
                source_path = os.path.join(root, file_name)
                files_section += f'Source: "{source_path}"; DestDir: "{{app}}"; Flags: ignoreversion\n'
            break  # Only process the top-level items
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(files_section)
    
    print(f"Generated Inno Setup files section in {output_file}")

if __name__ == "__main__":
    generate_inno_files_section()

import subprocess
import os
import shutil

def package_to_exe(code_str, file_name):
    # Write the code string to a .py file
    with open(file_name, 'w') as file:
        file.write(code_str)
    
    # Use pyinstaller to package the .py file into an .exe
    subprocess.run(['pyinstaller', '--onefile', file_name])
    
    # Move the generated .exe file from ./dist to the current directory
    exe_file = os.path.splitext(file_name)[0] + '.exe'
    dist_path = os.path.join('dist', exe_file)
    if os.path.exists(dist_path):
        shutil.move(dist_path, exe_file)
    
    # Clean up build directories and files
    shutil.rmtree('build')
    shutil.rmtree('dist')
    spec_file = os.path.splitext(file_name)[0] + '.spec'
    if os.path.exists(spec_file):
        os.remove(spec_file)
    if os.path.exists(file_name):
        os.remove(file_name)

# Example usage
if __name__ == "__main__":
    code = """
    print("Hello, World!")
    """
    package_to_exe(code, 'hello.py')
import os
import random
import subprocess
p = '/home/ellie/Engineering/Machine Learning/Python webinar'

os.chdir(p)

# print(os.listdir(p))

folder_name = random.choice(os.listdir(p))
folder_path = str(os.path.realpath(folder_name))
os.chdir(folder_path)
file_name = random.choice(os.listdir(folder_path))

print("Enjoy!")

# Play the file

subprocess.run(["xdg-open", file_name], check=True)

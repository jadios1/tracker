import os

# Uruchom swój generator HTML
os.system("python3 main.py")

# Zrób commit i push do GitHuba
os.system("git add index.html")
os.system("git commit -m 'auto update'")
os.system("git push")

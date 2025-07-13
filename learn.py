import sys


new_path = "./users/mening_papkam"
sys.path.append(new_path)

print("Import yo'llari:")
for path in sys.path:
    print(path)

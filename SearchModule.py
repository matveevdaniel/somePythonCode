import sys
for pth in sys.path:
    print(pth)
    
sys.path.append("lib.py")
print(sys.path)
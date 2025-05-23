print("Celebal Technologies Assessment -> Week 1")
print("Atharva Rahate")


def reversetri():
    print("\nReverse Triangle")
    for i in range(rows):
        print("*" * (rows - i))

def triangle():
    print("\nTriangle")
    for i in range(rows):
        print("*" * (i + 1))

def center_tri():
    print("\nCenter Aligned Right Triangle")
    for i in range(rows):
        print(' ' * (rows - 1 - i) + '*' * (i + 1))

def right_rev():
    print("\nRight-Aligned Reverse Triangle")
    for i in range(rows):
        print(" " * i + '*' * (rows - i))

def center():
    print("\nInverted Centered Triangle")
    for i in range((rows + 1) // 2):
        print(" " * i + '*' * (rows - 2 * i))

def centered_triangle():
    print("\nCentered Triangle")
    for i in range((rows + 1) // 2):
        print(" " * (rows // 2 - i) + '*' * (2 * i + 1))

def trie():
    triangle()
    reversetri()
    center_tri()
    right_rev()
    center()
    centered_triangle()


rows = int(input("Enter the number of rows: "))
if rows < 2:
    print("It will just print simple * !")
else:
    trie()


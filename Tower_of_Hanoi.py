class Rod:
    def __init__(self, name = "", num_disk = 0):
        self.name = name
        self.stack = []
        for i in range(num_disk, 0, -1):
            self.stack.append(i)

    def push(self, disk):
        self.stack.append(disk)

    def pop(sefl):
        return sefl.stack.pop()

    def __str__(self):
        return self.name + ": " + self.stack.__str__()

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod) # move top n-1 disks to aux rod
    
    to_rod.push(from_rod.pop()) # move the biggest disk from source rod to destination rod

    print("Move disk", n, "from rod", from_rod.name, "to rod", to_rod.name)
    print_rods()
    
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod) # move n-1 disks from aux rod to destination rod

def print_rods():
    print(rod_A)
    print(rod_B)
    print(rod_C)
    print()

n = int(input("Enter nums of disk:"))

rod_A = Rod("A", n)
rod_B = Rod("B")
rod_C = Rod("C")

print("Initialize state")
print_rods()

TowerOfHanoi(n, rod_A, rod_C, rod_B)


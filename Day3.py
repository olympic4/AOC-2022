input = open("input.txt","r").read()
rucksacks = input.splitlines()

alphabet_priority_order = [chr(v) for v in range(ord("a"), ord("z")+1)]+([chr(v) for v in range(ord("A"), ord("Z")+1)])

def search1(rucksack):
    firstCompartment = rucksack[:len(rucksack)//2]
    secondCompartment = rucksack[len(rucksack)//2:]
    for item in firstCompartment:
        if item in secondCompartment:
            return alphabet_priority_order.index(item)+1

def search2(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return alphabet_priority_order.index(item)+1

groups = [
    rucksacks[rucksacks.index(rucksack)-2:rucksacks.index(rucksack)+1] 
    for rucksack in rucksacks
    if (rucksacks.index(rucksack)+1)%3 == 0
]

print("PART 1:",sum(search1(rucksack) for rucksack in rucksacks))
print("PART 2:",sum(search2(group) for group in groups))

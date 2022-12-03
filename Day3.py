input = open("input.txt","r").read()

alphabet_priority_order = [chr(v) for v in range(ord("a"), ord("z")+1)]+([chr(v) for v in range(ord("A"), ord("Z")+1)])

def search(rucksack):
    firstCompartment = rucksack[:len(rucksack)//2]
    secondCompartment = rucksack[len(rucksack)//2:]
    for item in firstCompartment:
        if item in secondCompartment:
            return alphabet_priority_order.index(item)+1

print("PART 1:",sum(search(rucksack) for rucksack in input.splitlines()))

input = open("input.txt","r").read()

elvesTotals = sorted(map(sum,[map(int,elf.splitlines()) for elf in input.split("\n\n")]),reverse=True)

print("PART 1:",elvesTotals[0])
print("PART 2:",sum(elvesTotals[0:3]))

input = open("input.txt","r").read()

rules = {
    "A X": "D",
    "A Y": "W",
    "A Z": "L",
    "B X": "L",
    "B Y": "D",
    "B Z": "W",
    "C X": "W",
    "C Y": "L",
    "C Z": "D"
}

scores = {
    "W": 6,
    "D": 3,
    "L": 0,
    "X": 1,
    "Y": 2,
    "Z": 3
}

def score1(game):
    return scores[rules[game]] + scores[game[2]]

def score2(game):
    if game[2] == "X": outcome = "L"
    if game[2] == "Y": outcome = "D"
    if game[2] == "Z": outcome = "W"
    played = [rule[2] for rule in rules.keys() if rules[rule] == outcome and rule[0] == game[0]][0]
    return scores[outcome] + scores[played]

print("PART 1:",sum(score1(game) for game in input.splitlines()))
print("PART 2:",sum(score2(game) for game in input.splitlines()))

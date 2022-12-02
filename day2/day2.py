def part1():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        lines = [line.replace(" ", "") for line in lines]
        
        totalScore = 0
        for round in lines:
            print(round, eval(round))
            totalScore += eval(round) + getScoreForChoice(round[1])
        print(totalScore)

def eval(round):
    p1 = round[0]
    p2 = round[1]

    p1Rock = "A"
    p1Paper = "B"
    p1Scissors = "C"

    p2Rock = "X"
    p2Paper = "Y"
    p2Scissors = "Z"

    if p1 == p1Rock and p2 == p2Rock:
        return 3
    elif p1 == p1Paper and p2 == p2Paper:
        return 3
    elif p1 == p1Scissors and p2 == p2Scissors:
        return 3
    elif p1 == p1Rock:
        if p2 == p2Paper:
            return 6
        elif p2 == p2Scissors:
            return 0
    elif p1 == p1Paper:
        if p2 == p2Rock:
            return 0
        elif p2 == p2Scissors:
            return 6
    elif p1 == p1Scissors:
        if p2 == p2Rock:
            return 6
        elif p2 == p2Paper:
            return 0

def getScoreForChoice(choice):
    if choice == "X":
        return 1
    elif choice == "Y":
        return 2
    elif choice == "Z":
        return 3
    

def part2():
     with open("input.txt") as f:
        lines = f.read().splitlines()
        lines = [line.replace(" ", "") for line in lines]
        
        totalScore = 0
        for round in lines:
            totalScore += eval2(round)
        print(totalScore)

def eval2GAME(round):
    p1 = round[0]
    p2 = round[1]

    p1Rock = "R"
    p1Paper = "P"
    p1Scissors = "S"

    p2Rock = "R"
    p2Paper = "P"
    p2Scissors = "S"

    if p1 == p1Rock and p2 == p2Rock:
        return 3
    elif p1 == p1Paper and p2 == p2Paper:
        return 3
    elif p1 == p1Scissors and p2 == p2Scissors:
        return 3
    elif p1 == p1Rock:
        if p2 == p2Paper:
            return 6
        elif p2 == p2Scissors:
            return 0
    elif p1 == p1Paper:
        if p2 == p2Rock:
            return 0
        elif p2 == p2Scissors:
            return 6
    elif p1 == p1Scissors:
        if p2 == p2Rock:
            return 6
        elif p2 == p2Paper:
            return 0

def eval2(round):
    opp = round[0]
    res = round[1]

    convert = {
        "A": "R",
        "B": "P",
        "C": "S"
    }

    opp = convert[opp]
    me = ""

    if opp == "R":
        if res == "X":
            me = "S"
        elif res == "Y":
            me = "R"
        elif res == "Z":
            me = "P"
    elif opp == "P":
        if res == "X":
            me = "R"
        elif res == "Y":
            me = "P"
        elif res == "Z":
            me = "S"
    elif opp == "S":
        if res == "X":
            me = "P"
        elif res == "Y":
            me = "S"
        elif res == "Z":
            me = "R"
    
    return eval2GAME(opp + me) + getScoreForChoice2(me)

def getScoreForChoice2(choice):
    if choice == "R":
        return 1
    elif choice == "P":
        return 2
    elif choice == "S":
        return 3
            

    

if __name__ == "__main__":
    part2()
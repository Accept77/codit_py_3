with open('vocabulary.txt', 'r', encoding="UTF-8") as f:
    for line in f :
        line = line.strip()
        line_split = line.split(": ")
        anser = input(f"{line_split[1]}: ")
        if anser == line_split[0] :
            print("맞았습니다!\n")
        else :
            print(f"아쉽습니다. 정답은 {line_split[0]}입니다.\n")
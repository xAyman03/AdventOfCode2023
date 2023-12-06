data = []
bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sumOfId = 0

def extract_num_from_string(text):
    num = ""
    for c in text:
        if c.isdigit():
            num = num + c
    return num

def get_string_without_numbers(text):
    text_with_no_nums = ""
    for c in text:
        if not c.isdigit():
            text_with_no_nums = text_with_no_nums + c
    return text_with_no_nums   

def check_if_single_color_possible(color, cnt):
    return cnt <= bag[color]

def check_if_pull_possible(pull):
    isPossible = True
    colorsText = pull.split(",")
    for colorText in colorsText:
        color = get_string_without_numbers(colorText)
        colorCnt = extract_num_from_string(colorText)
        if not check_if_single_color_possible(color.strip(), int(colorCnt.strip())):
            isPossible = False
    return isPossible

with open('data.txt') as f:
    data = f.readlines()

for line in data:
    game_parts = line.split(":")
    gameName = game_parts[0]
    game = game_parts[1]
    gameID = extract_num_from_string(gameName)
    
    pulls = game.split(";")
    
    #check if every pull in pulls is checked True
    if all(check_if_pull_possible(pull) for pull in pulls):
        sumOfId += int(gameID)

print(sumOfId)

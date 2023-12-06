data = []
bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sumOfId = 0
sumOfPower = 0

maxOfGame = {
    "red": 0,
    "green": 0,
    "blue": 0
}

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
        
        if maxOfGame[color.strip()] <= int(colorCnt):
            maxOfGame[color.strip()] = int(colorCnt)
        
        if not check_if_single_color_possible(color.strip(), int(colorCnt.strip())):
            isPossible = False

    return isPossible

def reset_power_and_add_sum():
    global maxOfGame, sumOfPower
    
    power = int(maxOfGame["red"]) * int(maxOfGame["green"]) * int(maxOfGame["blue"])
    sumOfPower += power
    
    maxOfGame = {
    "red": 0,
    "green": 0,
    "blue": 0
    }
    

with open('data.txt') as f:
    data = f.readlines()

for line in data:
    game_parts = line.split(":")
    gameName = game_parts[0]
    game = game_parts[1]
    gameID = extract_num_from_string(gameName)
    
    pulls = game.split(";")
    
    #check if every pull in pulls is checked True
    pulls_bool = True
    for pull in pulls:
        if not check_if_pull_possible(pull):
            pulls_bool = False
            
    if pulls_bool:
        sumOfId += int(gameID)
        
    reset_power_and_add_sum()


print(sumOfId)
print(sumOfPower)

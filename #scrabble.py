#scrabble

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letters_to_points = dict(zip(letters, points))

def score_word(word):
    point_total = 0
    for char in word:
        if char in letters_to_points:
            point_total += letters_to_points[char]
            
    return point_total

player_to_word = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": [ "ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

def player_points(play_word):
    for player, words in player_to_word.items():
        player_point = 0
        for word in words:
            player_point += score_word(word)
            player_to_points[player] = player_point
    print(player_to_points)

def play_word(player):
    word = input("Give word: ").upper()
    if player in player_to_word:
        player_to_word[player].append(word)
    elif player not in player_to_word:
        player_to_word[player] = [word]

player_points(play_word("jose"))
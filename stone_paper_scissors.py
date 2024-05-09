import random


def get_choices():
    options=['paper','stone','scissors']
    computer_choice=random.choice(options)
    player_choice=input('enter your choice (scissors,paper,stone): ')
    choices={'computer' : computer_choice, 'player' : player_choice}
    return choices


def check_win(player,computer):
    print(f'you chose {player}, computer chose {computer}')
    if player==computer:
        return 'it is a tie'
    elif player=='scissors':
        if computer=='stone':
            return'you lose, stone smashes scissors'
        else:
            return'you win, scissors cuts paper'
    elif player=='stone':
        if computer=='paper':
            return'you lose, paper covers stone'
        else:
            return'you win, stone smashes scissors'
    elif player=='paper':
        if computer=='scissors':
            return'you lose, scissors cuts paper'
        else:
            return'you win, paper covers stone'
    else:
        # print("Wrong choice has been chosen:", player)
        raise Exception("Wrong choice has been chosen: " + player)


while True:
    try:
        choices = get_choices()
        result = check_win(choices['player'],choices['computer'])
        print(result)
        break
    except Exception as error:
        print("BŁĄD:", error)


# import random 
# def get_choices():
#     options=['paper','stone','scissors']
#     computer_choice=random.choice(options) 
#     player_choice=input('enter your choice (Scissors,Paper,Stone): ')
#     choicess={'computer' : computer_choice, 'player' : player_choice}
#     return choicess

# def check_win(player,computer):
#     print(f'you chose {player}, computer chose {computer}')
#     if player==computer:
#         return 'it is a tie'
#     elif player=='scissors':
#         if computer=='stone':
#             return'you lose, stone smashes scissors'
#         else:
#             return'you win, scissors cuts paper'
#     elif player=='stone':
#         if computer=='paper':
#             return'you lose, paper covers stone'
#         else:
#             return'you win, stone smashes scissors'
#     elif player=='paper':
#         if computer=='scissors':
#             return'you lose, scissors cuts paper'
#         else:
#             return'you win, paper covers stone'
    

# choices=get_choices()
# result=check_win(choices['player'],choices['computer'])
# print(result)

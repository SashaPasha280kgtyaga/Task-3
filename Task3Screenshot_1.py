def determine_winner(player1, player2):
    if player1 == player2:
        return "Ничья"
    elif (player1 == "камень" and player2 == "ножницы") or \
         (player1 == "ножницы" and player2 == "бумага") or \
         (player1 == "бумага" and player2 == "камень"):
        return "Победа первого игрока"
    else:
        return "Победа второго игрока"
player1_choice = "камень"
player2_choice = "ножницы"
result = determine_winner(player1_choice, player2_choice)
print(result)
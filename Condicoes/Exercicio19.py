player1 = input( " Escolha Sua Opção Entre Pedra, Papel e Tesoura: ")

player2 = input( " Escolha Sua Opção Entre Pedra, Papel e Tesoura: ")

if player1 == player2:
    print( " Empate! ")

elif (player1 == "Pedra" and player2 == "Tesoura") or (player1 == "Papel" and player2 == "Pedra") or (player1 == "Tesoura" and player2 == "Papel"):
    print(f" player 1 Venceu! {player1} Vence de {player2}. ")

else:
    print(f" player 2 Venceu! {player2} Vence de {player1}. ")



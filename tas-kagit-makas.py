import random

player_score, computer_score = 0, 0
computer_choice = 1

def print_result(computer_choice, winner="Bilgisayar"):
    print(f'Bilgisayarın Seçimi: {computer_choice}\nKazanan: {winner}')
    global computer_score, player_score
    if winner == "Bilgisayar":
        computer_score += 100
    else:
        player_score += 100

print("Taş Kağıt Makas Oyunumuza Hoş Geldiniz!\n" + ("-" * 39))

while True:
    print("\n 1 -> Taş\n 2 -> Kağıt\n 3 -> Makas\n Oyundan çıkmak isterseniz bu değerler dışında bir değer giriniz")
    player_choice = int(input("Seçiminizi Yapınız: "))
    computer_choice = random.choice([1, 2, 3])

    if player_choice == computer_choice:
        print("Berabere, yeniden oynayınız")
    elif player_choice == 1:
        if computer_choice == 2:
            print_result(computer_choice)
        else:
            print_result(computer_choice, "Kullanıcı")
    elif player_choice == 2:
        if computer_choice == 1:
            print_result(computer_choice, "Kullanıcı")
        else:
            print_result(computer_choice)
    elif player_choice == 3:
        if computer_choice == 1:
            print_result(computer_choice)
        else:
            print_result(computer_choice, "Kullanıcı")
    else:
        break

print(f'\nKullanıcı skoru: {player_score}\nBilgisayarın skoru: {computer_score}')
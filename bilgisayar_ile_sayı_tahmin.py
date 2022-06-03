import random

def computer_guess(num):
    start, end = 1, 100
    back = ''
    while back != "d":
        if start <= end:
           guess = random.randint(start, end)
        else:
            guess = start

        back = input(f"Tahminde bulunduğum değer {guess}, aklından tuttuğun değerden büyükse b ,küçükse k, eşitse d ifadesini gir. ").lower()
        if back == 'b' :
            end = guess - 1
        elif back == 'k':
            start = guess + 1
        elif back != 'd':
            print("Yanlış ifade kullandınız.")
            break
    print(f"Doğru tahmin: {guess}")
computer_guess(9) 
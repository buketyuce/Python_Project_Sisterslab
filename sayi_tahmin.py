import random

def guess(num):
    count = 1
    random_number = int(input("Sayı nedir? "))

    while num != random_number:
        print(f"Sayı tahmin oyunu için bir tahminde bulundunuz: {random_number} ")
        count += 1
        if num < random_number:
            print("Bu çok büyük, daha küçük sayı tahmininde bulunmalısın.")
        else:
            print("Bu çok küçük, daha büyük bir sayı tahmininde bulunmalısın. ")
        random_number = int(input("Sayı tahmin oyunu için bir tahminde bulunun "))

        print(f"Tebrikler, {count}. denemede doğru tahminde bulundunuz!!")


guess(random.randint(1, 100))
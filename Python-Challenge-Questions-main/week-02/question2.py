# Reads number of 1TL, 5TL, 10TL and 20TL.
# Computes and prints total amount money.
# Displays the total amount of money in terms of number of 20TLs and the remaining number of 1TLs.

one = int(input("Number of 1TL: "))
five = int(input("Number of 5TL: "))
ten = int(input("Number of 10TL: "))
twenty = int(input("Number of 20TL: "))

total_money = twenty * 20 + ten * 10 + five * 5 + one

number_of_twenty = int(total_money / 20)
number_of_one = total_money % 20

print(f"Total money: {total_money}")
print(f"Total money has {number_of_twenty}x20TLs and {number_of_one}x1TLs.")
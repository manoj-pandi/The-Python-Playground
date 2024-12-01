# python credit card validator program
#
# 1.Remove any "-" or  " "
# 2.Add all digits in the odd places from right to left
# 3.Double every second digit from right to left.
#
#             (if result is two-digit number,
#              add the two-digit number together to get a single digit.)
# 4.sum the totals of steps 2 & 3
# 5.if sum is divisible by 10,the credit card  is Valid

sum_odd_digits = 0
sum_even_digits= 0
total = 0

#step 1
card_number = input("Enter a credit card number : ")
card_number = card_number.replace("-","")
# print(card_number)
card_number = card_number.replace(" ", "")

#we going to read a card from right to left so reverse the card_number
card_number = card_number[::-1]

#step 2
#sum odd digits:
for x in card_number[::2]:
    sum_odd_digits +=int(x)


#step 3 Double every second digit from right to left.
for x in card_number[1::2]:
    x = int(x)*2
    if x >=10:
        sum_even_digits +=(1 + (x % 10))
    else:
        sum_even_digits +=x


#step 4
total = sum_odd_digits + sum_even_digits


#step 5
if total % 10 ==0:
    print("VALID")
else:
    print("Invalid")




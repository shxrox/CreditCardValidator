sum_odd_digits = 0
sum_event_digit = 0
totel = 0

# step 1
card_number = input("Enter a credit card # : ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

#step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)

#step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_event_digit += (1 + (x % 10))
    else:
        sum_event_digit += x


#step 4
totel = sum_odd_digits + sum_event_digit

#step 5
if totel % 10 == 0:
    print("VALID")
else:
    print("INVALID") 


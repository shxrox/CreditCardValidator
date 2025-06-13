# Credit Card Validator 💳

This Python script checks if a credit card number is valid using the **Luhn algorithm**.

## How it works

The program:
1️⃣ Asks the user to enter a credit card number (spaces or dashes allowed).  
2️⃣ Reverses the number.  
3️⃣ Sums all digits in odd positions (from the right).  
4️⃣ Doubles all digits in even positions (from the right). If doubling results in a two-digit number, its digits are summed (or add 1 + remainder of dividing by 10).  
5️⃣ Adds both sums.  
6️⃣ If the total modulo 10 is 0, the card is **VALID**. Otherwise, it is **INVALID**.

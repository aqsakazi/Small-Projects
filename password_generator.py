import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "()*;/[]{}-_,"

everything = lower + upper + number + symbols
length = 15
password = "".join(random.sample(everything , length))
   print(password)

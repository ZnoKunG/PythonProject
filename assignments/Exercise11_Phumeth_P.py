number = int(input("Input number of stages of pyramid :"))
for a in range(number):
  number -= 1
  print(" " * number + (2 * a + 1) * "*")
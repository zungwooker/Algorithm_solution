change = 1000-int(input())
coins = 0

coins += change//500
change %= 500
coins += change//100
change %= 100
coins += change//50
change %= 50
coins += change//10
change %= 10
coins += change//5
change %= 5
coins += change

print(coins)
# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


# Specifying which position will be the column and row

column = int(position[0])  # first digit
row = int(position[1])  # second digit

map[column-1][row-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

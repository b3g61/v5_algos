'''
taka inn input notanda
bera saman við max_int, pre = 0
ef talan er neikvæð ... break 
ef tala er stærri en fyrri tala -> max_int verður að stærri tölunni
prentar út max tölu
'''

max_int = 0
while True:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int < 0:
        break
    elif num_int > max_int:
        max_int = num_int
# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line

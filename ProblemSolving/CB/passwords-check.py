import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)



# with open('passwords.txt', "r") as file:
#     # Read the lines of the file and split them into an array
#     lines = [line.strip() for line in file.readlines()]

# counter = 0
# for l in lines:
#     splitted_array = l.split(':')
#     policy = splitted_array[0].split(' ')
#     letter = policy[1]
#     times = policy[0].split('-')
#     minimum = times[0]
#     maximum = times[1]

#     if splitted_array[1].count(letter) >= int(minimum) and splitted_array[1].count(letter) <= int(maximum):
#         counter+=1

# print(counter)

counter = 0

with open('passwords.txt', "r") as file:
    for line in file.readlines():
        l = line.strip() 
        splitted_array = l.split(':')
        policy = splitted_array[0].split(' ')
        letter = policy[1]
        times = policy[0].split('-')
        minimum = times[0]
        maximum = times[1]
        if splitted_array[1].count(letter) >= int(minimum) and splitted_array[1].count(letter) <= int(maximum):
            counter+=1

print(counter)

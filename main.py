#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = '[name]'

def create_letter(inv_name):
    with open('./Input/Letters/starting_letter.txt', 'r') as new_letter:
        line = new_letter.readlines()
        line[0] = line[0].replace(PLACEHOLDER, inv_name)
        print(line)

    with open(f"./Output/ReadyToSend/send_to_{inv_name}.txt", 'x') as new_file:
        full_letter = ''.join(line)
        new_file.write(full_letter)

with open("./Input/Names/invited_names.txt", 'r') as inv_names:
    name_list = inv_names.readlines()

for name in range(len(name_list)):
    name_list[name] = name_list[name].strip('\n')
    create_letter(name_list[name])
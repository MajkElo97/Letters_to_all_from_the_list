# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


with open(file="Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open(file="./Input/Letters/starting_letter.txt") as basic_letter:
    letter_string = basic_letter.read()

for name in name_list:
    new_name = name.strip("\n")
    letter_string_with_name = letter_string.replace("[name]", new_name)
    with open(file=f"Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as file:
        file.write(letter_string_with_name)

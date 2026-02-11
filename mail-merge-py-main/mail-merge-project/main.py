PLACEHOLDER = "[name]"

with open("invited_names.txt") as names_file:
    names = names_file.readlines()


with open("letter.txt") as letter:
    content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_latter:
            completed_latter.write(new_letter)
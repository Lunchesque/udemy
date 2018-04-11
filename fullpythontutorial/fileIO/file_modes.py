# with open("haiku.txt", "a") as file:
#     file.write("opened file with 'a' flag\n")


# with open("haiku.txt", "r+") as file:
#     file.write(":)\n")
#     file.seek(10)
#     file.write(":(\n")

def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()

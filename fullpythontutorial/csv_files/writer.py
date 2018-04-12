from csv import writer, DictWriter
# with open("cats.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue", 4])
#     csv_writer.writerow(["Kitty", 7])

with open("cats.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Blue",
        "Breed": "lemon",
        "Age": 10
    })

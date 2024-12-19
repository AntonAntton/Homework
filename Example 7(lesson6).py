library = {
    "Taras": ["Taras 1", "Taras 2"],
    "Lesia": ["Lesia 1", "Lesia 2"],
    "Ivan": ["Ivan 1", "Ivan 2"],
}
for author, books in library.items():
    print("Author:", author, "\nBook:")
    for book in books:
        print(book, sep=", ")

    print()

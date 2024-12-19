authors = {
    "Taras": ["Taras 1", "Taras 2"],
    "Lesia": ["Lesia 1", "Lesia 2"],
    "Ivan": ["Ivan 1", "Ivan 2"],
}
print(f"{authors}")
for author, works in authors.items():
    print(f"{author}: {works}")
for author in authors:
    print(f"author: {author}")
print(authors.keys())
print(authors.values()) 
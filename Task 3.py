names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    cleaned = name.strip().lower()
    cleaned_names.append(cleaned)

print("Cleaned Names:", cleaned_names)
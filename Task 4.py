messages = ["Hi", "Welcome to the platform", "OK"]

for mess in messages:
    length = len(mess)
    print(f"Message: '{mess}' | Length: {length}")
    
    if length > 10:
        print("⚠ This message is longer than 10 characters")

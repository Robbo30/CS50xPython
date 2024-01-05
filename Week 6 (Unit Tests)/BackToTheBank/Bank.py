def main():
    greeting = input("Greeting: ")
    print(f"${money(greeting)}")

def money(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
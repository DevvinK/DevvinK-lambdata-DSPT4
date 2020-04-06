# my_lambdata/my_mod.py

def enlarge(n):
    return n * 100

if __name__ == "__main__":
        print("Junk")
        print("Global scope")

        y = float(input("Please input a number to enlarge: "))
        print(enlarge(y))
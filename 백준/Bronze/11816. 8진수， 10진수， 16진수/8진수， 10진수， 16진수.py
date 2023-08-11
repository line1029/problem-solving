def main():
    x = input()
    if x[:2] == "0x":
        x = int(x, 16)
    elif x[0] == "0":
        x = int(x, 8)
    else:
        x = int(x)
    print(x)
main()

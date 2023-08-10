def main():
    name = input()
    if not (name and name[0].isalpha() and name[0] == name[0].lower()):
        print("Error!")
        exit()
    if "_" in name:
        if name != name.lower():
            print("Error!")
            exit()
        words = name.split("_")
        if "" in words:
            print("Error!")
            exit()
        for i in range(1, len(words)):
            words[i] = words[i].title()
        print("".join(words))
    elif name != name.lower():
        words = []
        i = 0
        for j in range(1, len(name)):
            if name[j] != name[j].lower():
                words.append(name[i:j].lower())
                i = j
        words.append(name[i:].lower())
        print('_'.join(words))
    else:
        print(name)
main()

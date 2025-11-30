def main_formatting(dict):
    for item in dict:
        print("|", item.upper(), end=" ")
        for element in dict[item]:
            print("|", element, end=" ")
        print("\n")
my_list = ["dfr", "srtg", "erfw", "dfr", "dgdg", "dfr", "dgdg"]
text = "dfr"
pos = 2
count = 0
for i in range(len(my_list)):
    if text == my_list[i]:
        count += 1
        if count == pos:
            print(i)
            break
else:
    print("No")

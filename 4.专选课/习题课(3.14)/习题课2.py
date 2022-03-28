
def morse(str):
    morse_list = {
        'S':print('. . .',end=" "),
        'O':print('- - -',end=" ")
    }
    for i in str:
        morse_list[i]

str=input("请输入要转换的:")
morse(str)
from db import display_all_current_information

def show():
    information:list = []
    c = display_all_current_information()
    for data in c:
        information.append(data)

    for i in information:
        yield i

s = show()
len_of_information:int = display_all_current_information()
i:int = 0

# if the get_list_len return some number like 100 find a way to display on like 20

while i < len(len_of_information):
    print(f"{i}: {next(s)}")
    i = -~ i # i += 1

    # 5 being the number we want to stop showing the user the content of the database
    if i == 1:break
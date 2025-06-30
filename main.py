from CRUD0626 import *

authors = load_default_data()
id_counter = 3

# print(press)

while True:
    print_info()
    press = input()

    match press:
        case "1":
            print_authors(authors)

        case "2":
            id_counter += 1
            authors.append(create_author(id_counter))


        case "3":
            edit_author(authors)

        case "4":
            delete_author(authors)

        case "5":
            print("Sustabdyta")
            break
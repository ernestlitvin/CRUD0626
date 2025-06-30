
def print_info():
    print("------------------")
    print("1. Atvaizduoti visus autorius")
    print("2. Itraukti nauja autori")
    print("3. Redaguoti autori/us")
    print("4. Pasalinti autori/us")
    print("5. Sustabdyti programa")
    print("----------Pasirinkite--------")

def load_default_data():
    return [
    {
        "id": 1,
        "name": "Justas",
        "surname": "Matonis"
    },
    {
        "id": 2,
        "name": "Paulius",
        "surname": "Davlionis"
    },
    {
        "id": 3,
        "name": "Tautvydas",
        "surname": "Ravlionis"
    }
    ]

def print_authors(authors):
    for aut in authors:
        print(f"Autoriaus vardas: {aut['name']}. Jo pavarde: {aut['surname']}, ID numeris: {aut['id']}")

def create_author(id_counter):
    print("Prideti")
    print("Iveskite nauja varda:")
    name = input()
    print("Iveskite nauja pavarde")
    surname = input()
    return {
        "id": id_counter,
         "name": name,
         "surname": surname,
            }



def edit_author(authors):
    print("Redaguoti")
    print("Iveskite autoriaus ID, kuri redaguosime")
    new_id = input()
    new_id = int(new_id)

    for aut in authors:
        if aut["id"] == new_id:
            print("Iveskite nauja varda")
            new_name = input()
            print("Iveskite nauja pavarde")
            new_surname = input()
            aut["name"] = new_name
            aut["surname"] = new_surname


def delete_author(authors):
    print("Pasalinti")
    print("Iveskite autoriaus ID, kuri pasalinsime:")
    remove_id = input()
    remove_id = int(remove_id)
    autorius_pasalinimui = None

    for aut in authors:
        if aut["id"] == remove_id:
            print("Pasalinti autori")
            autorius_pasalinimui = aut
            break

    if autorius_pasalinimui:
        authors.remove(autorius_pasalinimui)
        print("Autorius pasalintas")
    else:
        print("Autorius nerastas")

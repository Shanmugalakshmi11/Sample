dictionary = {
    "Schlüssel" : "Wert",
    "Hotel": "Trivagu"
}

def addItem(key, value):
    dictionary[key] = value

addItem("Horst", "Kurt")
print(dictionary["Horst"])

def printValue(s1, s2):
    dictionary[s1]= s2

printValue("Bill", "Gates")
print(dictionary["Bill"])

def value_is_equal(dictionary, key, value):
    # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
    if key in dictionary:
        # Überprüfen, ob der Wert unter dem angegebenen Schlüssel mit dem gegebenen Wert übereinstimmt
        return dictionary[key] == value
    else:
        # Falls der Schlüssel nicht im Dictionary vorhanden ist, geben Sie False zurück
        return False

# Beispielverwendung
my_dict = {'a': 10, 'b': 20, 'c': 30}
result = value_is_equal(my_dict, 'b', 20)

print(result)  # Ausgabe: True

def delete_item(dictionary, key):
    # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
    if key in dictionary:
        # Schlüssel-Wert-Paar aus dem Dictionary entfernen
        del dictionary[key]
        print(f'Schlüssel-Wert-Paar mit Schlüssel "{key}" wurde erfolgreich entfernt.')
    else:
        print(f'Schlüssel "{key}" ist nicht im Dictionary vorhanden.')

# Beispielverwendung
my_dict = {'a': 10, 'b': 20, 'c': 30}
delete_item(my_dict, 'b')

print(my_dict)  # Ausgabe: {'a': 10, 'c': 30}

def print_keys(dictionary):
    # Ausgabe aller Schlüssel im Dictionary
    for key in dictionary.keys():
        print(key)

# Beispielverwendung
my_dict = {'a': 10, 'b': 20, 'c': 30}
print_keys(my_dict)

def print_values(dictionary):
    # Ausgabe aller Werte im Dictionary
    for value in dictionary.values():
        print(value)

# Beispielverwendung
my_dict = {'a': 10, 'b': 20, 'c': 30}
print_values(my_dict)
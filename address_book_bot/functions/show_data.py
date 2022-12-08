from decorator.decorator import input_error


@input_error
def show_contact(data, collection):
    name = data[1]

    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    phones = docs[0]['phones']
    email = docs[0]['email']

    return f"Contact: {name}, contact's phones: {'NO PHONES' if not phones else phones}, contact's email: {'NO EMAIL' if not email else email}"


@input_error
def show_phones(data, collection):
    name = data[1]

    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    phones = docs[0]['phones']

    if not phones:
        return f"Contact {name} doesn't have any phone number"

    return phones


@input_error
def show_email(data, collection):
    name = data[1]

    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    email = docs[0]['email']

    if not email:
        return f"Contact {name} doesn't have any email"

    return email


@input_error
def show_all(data, collection):
    number_of_contacts = int(data[1])
    contacts = []

    for doc in collection.find().limit(number_of_contacts):
        contacts.append({'Contact': doc['name'], "contact's phones": "NO PHONES" if not doc['phones'] else doc['phones'],
                        "contact's email": "NO EMAIL" if not doc['email'] else doc['email']})

    return contacts

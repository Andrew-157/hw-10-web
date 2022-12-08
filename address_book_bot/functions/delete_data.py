from decorator.decorator import input_error


@input_error
def delete_contact(data, collection):
    name = data[1]

    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    collection.delete_one({'name': name})
    return f"Contact {name} was deleted form the Address Book"


@input_error
def delete_phone(data, collection):
    name = data[1]
    phone = data[2]
    phones = []

    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    phones = docs[0]['phones']

    if phone not in phones:
        return f"Contact {name} doesn't have this phone number: {phone}, you cannot delete it"

    phones.remove(phone)
    collection.update_one({'name': name}, {'$set': {'phones': phones}})
    return f"Phone {phone} was deleted for contact {name}"


@input_error
def delete_phones(data, collection):
    name = data[1]

    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    if not docs[0]['phones']:
        return f"Contact {name} doesn't have any phone number"

    collection.update_one({'name': name}, {'$set': {'phones': []}})
    return f"All phone numbers were deleted for contact {name}"


@input_error
def delete_email(data, collection):
    name = data[1]

    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    old_email = docs[0]['email']

    if not old_email:
        return f"Contact {name} email"

    collection.update_one({'name': name}, {'$set': {'email': ''}})
    return f"{old_email} was deleted for contact {name}"

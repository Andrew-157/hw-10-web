from decorator.decorator import input_error
import validation


@input_error
def add_contact(data, collection):
    name = data[1]
    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if docs:
        return f"Contact with {name} already exists"

    collection.insert_one({'name': name, 'phones': [], 'email': ''})
    return f'Contact with {name} was added to the Address Book'


@input_error
def add_phone(data, collection):
    name = data[1]
    phone = data[2]
    documents = collection.find({'name': name})
    docs = []
    phones = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact with {name} doesn't exist"

    check_match = validation.phone.validate(phone)

    if not check_match:
        return "Phone number should be of these formats: (00)-000-0-000 or (00)-000-00-00"

    phones = docs[0]['phones']

    if phone in phones:
        return f"Contact {name} already has this phone number"

    phones.append(phone)

    collection.update_one({'name': name}, {'$set': {'phones': phones}})
    return f"{phone} number was added to contact {name}"


@input_error
def add_email(data, collection):
    name = data[1]
    email = data[2]

    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    check_match = validation.email.validate(email)

    if not check_match:
        return "Email should be of this format: <some_user@gmail.com>"

    if email == docs[0]['email']:
        return f"Contact {name} already has this email: {email}"

    if docs[0]['email']:
        return f"Contact {name} already has an email, use another command to change it"

    collection.update_one({'name': name}, {'$set': {'email': email}})
    return f"{email} was added to contact {name}"

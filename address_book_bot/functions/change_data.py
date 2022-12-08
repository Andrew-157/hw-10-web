from decorator.decorator import input_error
import re


@input_error
def change_phone(data, collection):
    name = data[1]
    old_phone = data[2]
    new_phone = data[3]

    documents = collection.find({'name': name})
    docs = []
    phones = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    check_match_1 = re.search(
        r"\([0-9]{2}\)\-[0-9]{3}\-[0-9]{1}\-[0-9]{3}|\([0-9]{2}\)\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}", new_phone)

    check_match_2 = re.search(
        r"\([0-9]{2}\)\-[0-9]{3}\-[0-9]{1}\-[0-9]{3}|\([0-9]{2}\)\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}", old_phone)

    if not check_match_1 or not check_match_2:
        return "Phone number should be of these formats: (00)-000-0-000 or (00)-000-00-00"

    phones = docs[0]['phones']

    if old_phone not in phones:
        return f"Contact {name} doesn't have this phone number: {old_phone}"

    index = phones.index(old_phone)
    phones.insert(index, new_phone)
    phones.remove(old_phone)

    collection.update_one({'name': name}, {'$set': {'phones': phones}})
    return f"{name} contact's phone number: {old_phone} was changed to {new_phone}"


@input_error
def change_email(data, collection):
    name = data[1]
    email = data[2]

    documents = collection.find({'name': name})
    docs = []

    for doc in documents:
        docs.append(doc)

    if not docs:
        return f"Contact {name} doesn't exist"

    check_match = re.search(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email)

    if not check_match:
        return "Email should be of this format: <some_user@gmail.com>"

    old_email = docs[0]['email']

    if not old_email:
        return f"Contact {name} doesn't have any email, you cannot change it"

    collection.update_one({'name': name}, {'$set': {'email': email}})
    return f"{name} contact's email was changed from {old_email} to {email}"

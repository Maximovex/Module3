calls=0
def count_calls():
    global calls
    calls=calls+1
    return calls
def string_info(string):
    count_calls()
    string_info=(len(string),string.upper(), string.lower())
    return string_info
def is_contains(string, list_to_search):
    count_calls()
    string=string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i]=list_to_search[i].lower()
    if string in list_to_search:
        is_contains=True
    else:
        is_contains=False
    return is_contains
print(string_info('Rooster'))
print(is_contains('apple',['ApplePie','appleton']))
print(string_info('Rollerline'))
print(calls)

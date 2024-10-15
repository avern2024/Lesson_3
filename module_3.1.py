calls = 0

def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    string = (len(string), string.upper(), string.lower())
    print(string)
    count_calls()


def  is_contains(string, list_to_search):
    list_to_search  = [item.lower() for item in list_to_search]
    if string.lower() in list_to_search:
        print(True)
    else:
        print(False)

    count_calls()


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban',  ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)

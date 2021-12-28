# Python dictionary and get method.
# Example.

person = dict(name = 'John', age = 35)

def how_old(person):
    return str(person.get('age'))

print('This person is ' + how_old(person) + ' years old.')
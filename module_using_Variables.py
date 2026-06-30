# variable in module
#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

person1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

import module_using_Variables
print(module_using_Variables.person1["age"])

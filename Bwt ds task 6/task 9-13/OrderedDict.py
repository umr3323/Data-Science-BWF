from collections import OrderedDict

glossary = OrderedDict()

glossary['variable'] = 'A placeholder for a value.'
glossary['list'] = 'A collection of values that can be changed.'
glossary['tuple'] = 'A collection of values that cannot be changed.'
glossary['dictionary'] = 'A collection of key-value pairs.'
glossary['loop'] = 'A structure that allows repeated execution of a block of code.'

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}")

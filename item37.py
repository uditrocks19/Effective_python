# Using generators
def index_words(text):
    res = []
    if text:
        res.append(0)
    for index, char in enumerate(text):
        if char == ' ':
            res.append(index + 1)
    return res
text = "My name is Udit"

# generator version
def index_words_iter(text):
    if text:
        yield 0
    for index, char in enumerate(text):
        if char == ' ':
            yield index + 1

gen_obj = index_words_iter(text)

print(gen_obj)
for index in gen_obj:
    print(index)
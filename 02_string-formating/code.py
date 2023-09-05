name = "Magnus"
greeting = "Hello, {}"

with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")
with_name_three = greeting.format("Florian")

print(with_name)
print(with_name_two)
print(with_name_three)

longer_phrase = "Hello, {}. Today is {}."
formated = longer_phrase.format("Rolf", "Monday")
print(formated)

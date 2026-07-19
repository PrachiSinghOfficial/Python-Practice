# name="prachi"
# print(len(name))
# print(name.endswith("hi"))
# print(name.startswith("Pr"))
# print(name.capitalize())
s = " Hello Python "

# print(s.upper())          # HELLO PYTHON
# print(s.lower())          # hello python
# print(s.strip())          # Hello Python
# print(s.replace("Python", "World"))  # Hello World
# print(s.find("P"))        # 7
# print(s.count("o"))       # 2
# print(s.split())          # ['Hello', 'Python']



print(s.casefold())
print(s.center(20, "*"))
print(s.ljust(15, "-"))
print(s.rjust(15, "-"))
print("45".zfill(5))
print("Hello\nPython".splitlines())
print("apple-banana".partition("-"))
print("a-b-c".rpartition("-"))
print("banana".rfind("a"))
print("Mr.Pihu".removeprefix("Mr."))
print("notes.txt".removesuffix(".txt"))
print("my_var".isidentifier())
print("123".isdecimal())
print("123".isnumeric())
print("Hello World".istitle())
print("Hello".encode())
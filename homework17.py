def check_and_add(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result + 10
        return result
    return wrapper

@check_and_add
def get_number():
    return 5

@check_and_add
def get_text():
    return "Привіт!"

print(get_number())
print(get_text())

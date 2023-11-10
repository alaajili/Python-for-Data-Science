def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} <class 'NoneType'>")
    elif isinstance(obj, float) and obj != obj:
        print(f"Cheese: {obj} <class 'float'>")
    elif isinstance(obj, bool):
        print(f"Fake: {obj} <class 'bool'>")
    elif isinstance(obj, int):
        print(f"Zero: {obj} <class 'int'>")
    elif isinstance(obj, str) and not obj:
        print(f"Empty: <class 'str'>")
    else:
        print("Type not Found")
        return 1
    return 0
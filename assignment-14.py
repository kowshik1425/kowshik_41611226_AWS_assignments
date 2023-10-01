def main():
    try:
        result = kowshik + 41611226
    except NameError as ne:
        print(f"NameError: {ne}")
    else:
        print("No NameError occurred.")

    try:
        result = "42" + 42
    except TypeError as te:
        print(f"TypeError: {te}")
    else:
        print("No TypeError occurred.")

if __name__ == "__main__":
    main()

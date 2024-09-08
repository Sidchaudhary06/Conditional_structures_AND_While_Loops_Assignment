
SIZE_LIMIT = 42

length = float(input("Enter the length of the zander in centimeters: "))

if length >= SIZE_LIMIT:
    print("The zander meets the size limit. You can keep it.")
else:

    below_limit = SIZE_LIMIT - length
    print(f"The zander is {below_limit:.2f} centimeters below the size limit. You must release it back into the lake.")

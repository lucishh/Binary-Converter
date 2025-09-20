# Source code: https://github.com/lucishh/Binary-Converter/blob/main/script.py
# Published at: codedex.io/@lucish / https://www.codedex.io/@lucish/build/binary-converter

# 💙 Demical to Binary Converter 💛
# In terminal, run 'python script.py' to start the program.

first_time = True

try:
    while True:
        if first_time:
            user_input = input("\n🔟 Demical to Binary Converter\n😁 ('q' to quit)\n➕ Enter a decimal number: ")
            first_time = False
        else:
            user_input = input("➕ Enter a decimal number: ")

        if user_input.lower() == 'q':
            print("Goodbye! 💗")
            break

        try:
            decimal_number = int(user_input)
        except ValueError:
            print("\n❓ That's not a valid number. Try again!\n")
            continue

        binary_number = ""
        num = decimal_number

        if num == 0:
            binary_number = "0"

        while num > 0:
            remainder = num % 2
            binary_number = str(remainder) + binary_number
            num = num // 2

        print(f"\n 💙  Demical : {decimal_number}\n 💛  Binary : {binary_number} \n")

except KeyboardInterrupt:
    print("\nGoodbye! 💗")  # [optional] For clean exit on Ctrl+C

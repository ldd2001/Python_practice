responses = {}

polling_active = True
while polling_active:

    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response        # 将输入的 name 作为键（Key），对应的 response 作为值（Value），存储到字典 responses 中

    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False        # 如果 repeat 不是 no ，还是True，接着运行

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

#Receba uma temperatura em Fahrenheit e transforme em celsius.

temp_far = float(input("Digite a temperatura em Fahrenheit: "))

formula = (temp_far - 32) * 5/9

print(f"A temperatura em graus celsius são: {formula}")
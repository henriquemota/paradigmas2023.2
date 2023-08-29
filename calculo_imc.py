# cálculo do imc
peso = input("informe seu peso em KG")
altura = input("informe sua altura em M ex. 1.75")

pesof = float(peso)
alturaf = float(altura)

imc = pesof / (alturaf * alturaf)
print(imc)

if (imc < 18.5):
  print("magreza")
elif (imc >= 18.5 and imc < 24.9):
  print("peso normal")
elif (imc >= 24.9 and imc < 29.9):
  print("sobrepeso")
elif (imc >= 29.9 and imc < 34.9):
  print("obesidade grau I")
elif (imc >= 34.9 and imc < 40):
  print("obesidade grau II")
elif (imc >= 40):
  print("obesidade grau II")




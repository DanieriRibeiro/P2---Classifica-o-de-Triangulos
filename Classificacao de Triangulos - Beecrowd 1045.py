print("Vamos classificar os triângulos!\n\nExistem 2 tipos de classificação dos triângulos: em relação aos seus ângulos E em relação às medidas dos lados.\n \nPara saber a sua classificação precisamos de 3 números racionais positivos, cada número indica a medida de cada um dos lados do triângulo, assim podemos saber de qual tipo se trata. Porém, uma informação importante é que uma das variáveis não pode ser maior ou igual que a soma das outras duas, senão não formará triângulo.\n\n*Obs:Esse exercício é o de número 1045 do Beecrowd.com.br caso você queira conferir ;) \n")

A, B, C = input("Hora de digitar os números!\nDigite 3 números inteiros ou com vírgula separados por um espaço: \n").split(" ")
A = float(A)
B = float(B)
C = float(C)

if(C > B):
    aux = C
    C = B
    B = aux

if(B > A):
    aux = B
    B = A
    A = aux

if(C > B):
    aux = C
    C = B
    B = aux

aquad = A*A
bquad = B*B
cquad = C*C
sumba = bquad + cquad

if A >= B + C:
  print ("Infelizmente as medidas informadas não formam triângulo. Lembre-se! Uma das variáveis não pode ser maior ou igual a soma das outras duas!")
elif aquad == bquad + cquad:
  print ("A medidas informadas formam um TRIANGULO RETÂNGULO!")
elif aquad > sumba:
  print ("A medidas informadas formam um TRIÂNGULO OBTUSÂNGULO!")
elif aquad < sumba:
  print ("A medidas informadas formam um TRIÂNGULO ACUTÂNGULO!")

if A < B + C:
  if A == B and B == C:
   print ("Em relação a medida dos lados ele é um TRIANGULO EQUILÁTERO!")
  elif A == B or A == C or C == B:
    print ("Em relação a medida dos lados ele é um TRIANGULO ISÓSCELES!")
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

altura_total = 0
for altura in student_heights:
  altura_total += altura
print(altura_total)

numero_alunos = 0
for numero in student_heights:
  numero_alunos += 1

media = altura_total / numero_alunos
print(round(media))


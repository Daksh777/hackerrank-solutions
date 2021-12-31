student_marks = {}
for _ in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(f"{(sum(student_marks.get(query_name))/3):.2f}")
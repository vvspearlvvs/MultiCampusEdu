students = [
    {"name":"홍길동","korean":87, "math":98,"english":88, "science":95},
    {"name":"이몽룡","korean":92, "math":98,"english":96, "science":98},
    { "name":"성춘향","korean":76, "math":96,"english":94, "science":90},
    { "name":"변학도","korean":98, "math":92,"english":96, "science":92},
    {"name":"박지성","korean":95, "math":98,"english":98, "science":98},
    {"name":"류현진","korean":64, "math":88,"english":92, "science":92}
]
print("이름   총점  평균")
for student in students:
    name = student['name']
    score = student['korean']+student['math']+student['english']+student['science']
    avg = score/4
    print("{}   {}  {}".format(name,score,avg))

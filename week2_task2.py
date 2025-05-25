data = {
    'std1':{'Name':'Jitu','tests':[67,79,32],'quiz':[55,69]},
    'std2':{'Name':'Hau','tests':[78,82,85],'quiz':[70,91]},
    'std3':{'Name':'Duong','tests':[70,82,69],'quiz':[76,80]},
    'std4':{'Name':'Lam','tests':[81,85,89],'quiz':[73,83]},
    'std5':{'Name':'Tuyen','tests':[40,65,92],'quiz':[39,64]},
    'std6':{'Name':'Joe','tests':[35,79,65],'quiz':[51,72]},
    'std7':{'Name':'Linh','tests':[93,71,87],'quiz':[50,60]},
    'std8':{'Name':'Duc','tests':[77,75,66],'quiz':[57,43]},
    'std9':{'Name':'Liam','tests':[77,88,88],'quiz':[77,66]},
    'std10':{'Name':'Tavis','tests':[30,81,90],'quiz':[81,74]}
}

highest_test = -1
lowest_test = 101
highest_quiz = -1
lowest_quiz = 101
high_test_name = low_test_name = high_quiz_name = low_quiz_name = ''

print("Result Summary:\n")
print("{:<8} {:<6} {:<6} {:<6}".format("Name", "Test", "Quiz", "Grade"))

for std in data.values():
    name = std['Name']
    test_avg = sum(std['tests']) / 3
    quiz_avg = sum(std['quiz']) / 2
    total_avg = (test_avg + quiz_avg) / 2

    # Grade assignment
    if total_avg >= 80:
        grade = 'A'
    elif total_avg >= 69:
        grade = 'B'
    elif total_avg > 54:
        grade = 'C'
    else:
        grade = 'R'

    print("{:<8} {:<6.2f} {:<6.2f} {:<6}".format(name, test_avg, quiz_avg, grade))

    # Update max/min
    for t in std['tests']:
        if t > highest_test:
            highest_test = t
            high_test_name = name
        if t < lowest_test:
            lowest_test = t
            low_test_name = name

    for q in std['quiz']:
        if q > highest_quiz:
            highest_quiz = q
            high_quiz_name = name
        if q < lowest_quiz:
            lowest_quiz = q
            low_quiz_name = name

print("\nThe highest score obtained in Test is:", highest_test, "by", high_test_name)
print("The lowest score obtained in Test is:", lowest_test, "by", low_test_name)
print("The highest score obtained in Quiz is:", highest_quiz, "by", high_quiz_name)
print("The lowest score obtained in Quiz is:", lowest_quiz, "by", low_quiz_name)

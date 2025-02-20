marks={
    'nilesh-geography': 89,
    'alpesh-history': 77,
    'shital-math': 93,
    'dimpal-hindi': 68,
    'nilesh-english': 74,
    'alpesh-sci': 85,
    'shital-history': 91,
    'dimpal-geography': 87,
    'nilesh-sci': 83,
    'alpesh-math': 92,
    'dimpal-english': 78,
    'shital-hindi': 81,
    'nilesh-history': 90,
    'alpesh-geography': 79,
    'dimpal-math': 84,
    'shital-sci': 88,
    'nilesh-hindi': 71,
    'alpesh-english': 80,
    'dimpal-sci': 89,
    'shital-geography': 82,
    'nilesh-math': 93,
    'alpesh-hindi': 75,
    'dimpal-history': 90,
    'shital-english': 87
}
#----------------------------------------------Finding the total marks of the students present inside the dictionary------------------------------------------------------
total_marks={}

for key, value in marks.items():
    name=key.split('-')[0]
    if name in total_marks:
        total_marks[name] += value
    else:
        total_marks[name] = value
print(" \n 1) The total marks of the students present in dictionary are: ",total_marks)


#------------------------------------------------------------Finding the average of the students------------------------------------------------------------------------
per_subject_average={}

for key,value in marks.items():
    name=key.split('-')[0]
    if name in per_subject_average:
        per_subject_average[name] += 1
    else:
        per_subject_average[name]=1
avg_marks= {name:total_marks[name]/per_subject_average[name]
            for name in total_marks}
print(" \n 2) The average marks of the students present in dictionary are: ",avg_marks)

#-------------------------------Identify the Highest Scoring Student: Find out which student has the highest total marks.-----------------------------------------------
highest_scoring_student=max(total_marks,key=per_subject_average.get)
print("\n 3) The highest score of the students present in dictionary is",highest_scoring_student,"with",total_marks[highest_scoring_student],"marks")

#----------------------Subject-wise Highest Marks: Create a new dictionary where the key is the subject, and the value is the highest marks obtained in that subject.----------------------------------

highest_scorer_in_subject={}
for key,value in marks.items():
    _,subject=key.split('-')
    highest_scorer_in_subject[subject]=max(highest_scorer_in_subject.get(subject,0),value)
print("\n 4) Highest marks in each subject: ")
for subject,score in highest_scorer_in_subject.items():
    print(f"\t{subject}:{score}")

#--------------- Sort Students by Total Marks in Descending Order: Sort and display the students based on their total marks from highest to lowest. output will be dict.----------------------------------------------
def get_total_marks(students):
    return students[1]

sorted_students=sorted(total_marks.items(),key=get_total_marks,reverse=True)

print("\n 5) Students sorted by total marks: ")
for name,marks in sorted_students:
    print(f"\t {name}:{marks}")
'''8. Hospital Emergency Queue
A hospital has a list of patients with different priority levels.
Write a program to arrange the patients so that the patient with the
highest priority is treated first.'''

priority_patients = [32, 21, 14, 45, 30]

def Emergency_queue(priority_patients):
    for i in range(1, len(priority_patients)):
        arrange = priority_patients[i]
        j = i - 1
        while j >= 0 and priority_patients[j] < arrange:
            priority_patients[j + 1] = priority_patients[j]
            j -= 1
        priority_patients[j + 1] = arrange
    return priority_patients


print(Emergency_queue(priority_patients))
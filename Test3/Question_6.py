'''6. Employee Salary Report
An HR department has employee salary records collected from two different
branches.
Write a program to combine both lists and display all salaries in
ascending order.'''

def merge_sort(firstbranch, secondbranch):
    salary = firstbranch + secondbranch
    n = len(salary)
    for i in range(n):
        for j in range(n - i - 1):
            if salary[j] > salary[j + 1]:
                salary[j], salary[j + 1] = salary[j + 1], salary[j]
    return salary

firstbranch = [45000, 80000, 90000]
secondbranch = [70000, 920000, 67000]

print(merge_sort(firstbranch, secondbranch))





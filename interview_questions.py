# anagrams-

# cat, tac, 


# input=['tac', 'cat, act, sat, ast, tsa]

# output=[['tac','cat','act']]


# [t->1,a->1,c->1]

from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)
    
    for word in words:
        key = ''.join(sorted(word))  # sorted word as key
        anagram_map[key].append(word)
    
    return list(anagram_map.values())


input_words = ['tac', 'cat', 'act', 'sat', 'ast', 'tsa']
# print(group_anagrams(input_words))

# def emp():
#     employee_db= [
#         {"name": "Alice", "designation": "Software Engineer", "experience": 3, "salary": 75000},
#         {"name": "Bob", "designation": "Senior Developer", "experience": 6, "salary": 110000},
#         {"name": "Charlie", "designation": "Manager", "experience": 10, "salary": 150000},
#         {"name": "Bob2", "designation": "Senior Developer", "experience": 6, "salary": 610000}
#     ]


#     map={}
#     res=[]
#     for i in employee_db:
#         designation=i["designation"]
#         if designation in map and map[designation] < i['salary']:
#            res.append(i['name'])
#         else:
#             map[designation]=i['salary']
#             res
#     return res


# print(emp())

from collections import defaultdict

employee_db = [
    {"name": "Alice", "designation": "Software Engineer", "experience": 3, "salary": 75000},
    {"name": "Bob", "designation": "Senior Developer", "experience": 6, "salary": 110000},
    {"name": "Charlie", "designation": "Manager", "experience": 10, "salary": 150000},
    {"name": "Bob2", "designation": "Senior Developer", "experience": 6, "salary": 610000}
]

def highest_salary_by_department(employees):
    dept_map = defaultdict(list)
    
    # Step 1: Group by designation
    for emp in employees:
        dept_map[emp["designation"]].append(emp)
    
    result = {}
    
    # Step 2: Find highest salary in each designation
    for dept, emp_list in dept_map.items():
        max_salary = max(emp["salary"] for emp in emp_list)
        
        # Collect names with that salary
        result[dept] = [
            emp["name"] for emp in emp_list if emp["salary"] == max_salary
        ]
    
    return result


print(highest_salary_by_department(employee_db))





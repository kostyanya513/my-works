students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def interesteds_age(dict):
  interesteds = []
  for index in dict:
    interesteds.extend(dict[index]['interests'])
  cnt = 0
  for summ in dict:
    cnt += len(dict[summ]['surname'])
  return set(interesteds), cnt

print('Список пар "ID студента — возраст":', [(index, students[index]['age']) for index, age in students.items()])

my_lst = interesteds_age(students)
print('Полный список интересов всех студентов:', my_lst[0])
print('Общая длина всех фамилий студентов:', my_lst[1])

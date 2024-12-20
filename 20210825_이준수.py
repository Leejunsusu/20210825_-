import random

# 데이터 생성 함수
def generate_students(num=30):
    students = []
    for _ in range(num):
        name = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 선택 정렬
def selection_sort(data, key, reverse=False):
    n = len(data)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if (data[j][key] < data[least][key]) != reverse:
                least = j
        data[i], data[least] = data[least], data[i]

# 삽입 정렬
def insertion_sort(data, key, reverse=False):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i - 1
        while j >= 0 and (data[j][key] > current[key]) != reverse:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current

# 스택 기반 비재귀 퀵 정렬
def quick_sort(data, key, left, right, reverse=False):
    stack = [(left, right)]
    while stack:
        left, right = stack.pop()
        if left >= right:  # 범위가 역전되면 스킵
            continue

        pivot_index = median_of_three(data, key, left, right, reverse)
        pivot_index = partition(data, key, left, right, pivot_index, reverse)

        # 스택에 다음 분할 범위를 추가
        if pivot_index - 1 > left:
            stack.append((left, pivot_index - 1))
        if pivot_index + 1 < right:
            stack.append((pivot_index + 1, right))

# 중앙값 피벗 선택 함수
def median_of_three(data, key, left, right, reverse):
    mid = (left + right) // 2
    candidates = [(data[left][key], left), (data[mid][key], mid), (data[right][key], right)]
    candidates.sort(reverse=reverse)
    return candidates[1][1]  # 중간값의 인덱스를 반환

# 분할 함수
def partition(data, key, left, right, pivot_index, reverse):
    pivot_value = data[pivot_index][key]
    data[pivot_index], data[right] = data[right], data[pivot_index]  # 피벗을 끝으로 이동
    store_index = left

    for i in range(left, right):
        if (data[i][key] < pivot_value) != reverse:
            data[i], data[store_index] = data[store_index], data[i]
            store_index += 1

    data[store_index], data[right] = data[right], data[store_index]  # 피벗을 제자리로 이동
    return store_index

# 기수 정렬 (성적 전용)
def radix_sort(data):
    max_val = max(student["성적"] for student in data)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(data, exp)
        exp *= 10

# 계수 정렬 (기수 정렬 보조)
def counting_sort_radix(data, exp):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for student in data:
        index = (student["성적"] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (data[i]["성적"] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1

    for i in range(n):
        data[i] = output[i]

# 출력 함수
def display_students(data):
    print(f"{'이름':<5} {'나이':<5} {'성적':<5}")
    print("-" * 20)
    for student in data:
        print(f"{student['이름']:<5} {student['나이']:<5} {student['성적']:<5}")

# 메뉴 함수
def main():
    students = generate_students()
    print("생성된 학생 목록:")
    display_students(students)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")

        choice = input("정렬 기준을 선택하세요 (1, 2, 3, 4): ")

        if choice == "4":
            print("프로그램을 종료합니다.")
            break

        print("\n정렬 알고리즘을 선택하세요:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적 전용)")

        algo_choice = input("선택: ")

        reverse = input("오름차순(0) 또는 내림차순(1)을 선택하세요: ") == "1"

        key = ""
        if choice == "1":
            key = "이름"
        elif choice == "2":
            key = "나이"
        elif choice == "3":
            key = "성적"
        else:
            print("잘못된 입력입니다.")
            continue

        data_copy = students.copy()

        if algo_choice == "1":
            selection_sort(data_copy, key, reverse)
        elif algo_choice == "2":
            insertion_sort(data_copy, key, reverse)
        elif algo_choice == "3":
            quick_sort(data_copy, key, 0, len(data_copy) - 1, reverse)
        elif algo_choice == "4" and choice == "3":
            radix_sort(data_copy)
            if reverse:
                data_copy.reverse()
        else:
            print("잘못된 입력이거나 기수 정렬은 성적 전용입니다.")
            continue

        print("\n정렬된 학생 목록:")
        display_students(data_copy)

if __name__ == "__main__":
    main()

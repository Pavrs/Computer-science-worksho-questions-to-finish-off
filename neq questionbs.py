# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [comment]
def one():
    try:
        arr=[1,2,3,4,5,6,7,8,9,10]
        print(arr)
        target=int(input('input number: '))
        def binary (arr, target):
            left, right = 0, len(arr) -1
            while left <= right:
                mid = (left+right)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid+1
                else:
                    right= mid-1
            return -1

        result= binary(arr, target)

        if result!=-1:
            print(f'the target {target} has the index {result}')
        else:
            print(f'{target} not found in list')
        
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def two():
    try:
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def three():
    try:
        score= int(input('Please input your score'))
        grades = [0,48,61,74,88,102]
        u=0, e=48, d=61, c=74, b=88, a=102
        for index in range(len(grades)):
            if score == grades[index]:
                print(x)
            elif score < grades[index]:
                score= int(input('please input your correct score'))
            pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def four():
    try:
        import random
        numbers= []
        for x in range(10):
            number=random.randint(1,50)
            numbers.append(number)
            print(numbers)
        for y in numbers:
            if y > 25:
                print('the numbers greater than 25 are')
                print(y, end= '')
            elif y > 0:
                print('the max of the numbers is', max(numbers))
                print('the min of the numbers is', min(numbers))
            else:
                print('the sum of the numbers is', sum(numbers))
                break
        
        
        pass   
    except Exception as e:
        print("Error occurred:", e )
# [comment]
def main():
    try:
        four()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()

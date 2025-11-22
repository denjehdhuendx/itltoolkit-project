def f(score):
    if score<60:
        return "初级教师"
    elif score<90:
        return "中级教师"
    else:
        return "高级教师"

while True:
    score = input('请输入分数')
    if score !='end':
        print(f(int(score)))
    else:
        break 
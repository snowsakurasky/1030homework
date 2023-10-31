student = {'sid': ' ', 'sname': ' ', 'fchina': ' ', 'fmath': ' ', 'finfo': ' '}
student["sid"] = input("請輸入您的學號：")
student["sname"] = input("請輸入您的姓名：")
student["fchina"] = input("請輸入您的國文成績：")
student["fmath"] = input("請輸入您的數學成績：")
student["finfo"] = input("請輸入您的電腦成績：")
print(format("-" * 30))
print(format(student["sname"] + "(" + student["sid"] + ")" + "同學您好："))
print(format("以下是您的各科成績與分數評定"))
print()
sum = float(student["fchina"]) + float(student["fmath"]) + float(
    student["finfo"])
average = round(sum / 3, 2)
print(format("國文：" + student["fchina"] + " / 數學：" + student["fmath"] +
             " / 電腦：" + student["finfo"]))
print(format("總分：" + str(sum) + " / 平均：" + str(average)))
print(format("-" * 30))
if average >= 60:
    print(format("成績判定：合格"))
else:
    print(format("成績判定：不合格"))

zhaocheng = "高富帅"
if zhaocheng == "高富帅123":
    print("111")
if zhaocheng == "123":
    print("222")

userName = input("请输入您的用户名：")
pwd = input("请输入您的密码：")

if userName == "admin" and pwd == "000":
    print("恭喜您，登录成功")
else:
    print("抱歉，您的用户名和密码错误")


height = float(input("请输入身高："))
if 1 <= height <= 1.5:
    print("小强 你在哪里？")
elif 1.5 < height <= 1.7:
    print("没有安全感~")
elif 1.8 < height <= 2:
    print("帅哥 你建议多一个女朋友吗")
else:
    print("没有改身高的外星人类")
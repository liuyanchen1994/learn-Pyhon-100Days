"""
用户身份验证
"""
name = input('请输入用户名：')
pwd = input('请输入密码：')
if name == 'admin' and pwd == '123456':
    print('验证成功')
else:
    print('验证失败')
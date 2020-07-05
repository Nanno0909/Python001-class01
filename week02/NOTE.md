学习笔记
1.
pass



2.使用request登录网页时（个人真实账号），个人信息应保存在本地文件中，然后从文件中读取。

【
 在windows系统当中读取文件路径可以使用\,但是在python字符串中\有转义的含义，如\t可代表TAB， \n代表换行，所需要采取一些方式使得\不被解读为转义字符。

    1、在路径前面加r，即保持字符原始值的意思。
----sys.path.append(r'c:\Users\mshacxiang\VScode_project\web_ddt')

    2、替换为双反斜杠
----sys.path.append('c:\\Users\\mshacxiang\\VScode_project\\web_ddt')

    3、替换为正斜杠
----sys.path.append('c:/Users/mshacxiang/VScode_project/web_ddt')
】


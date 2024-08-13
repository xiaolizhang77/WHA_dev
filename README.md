# WHA_dev
![logo](image/logo.jpeg)

视频介绍：

    https://www.bilibili.com/video/BV1QevNemEhU/
    https://www.bilibili.com/video/BV11x8zeWEfF/
    https://www.bilibili.com/video/BV1Gp8peHEav/

#   代码使用

生成对应requirement.txt：

    pip freeze > requirements.txt

main_ui.spec文件中pathex参数为QTDesigner绝对路径，配置方法请参照[PyQt6](https://github.com/xiaolizhang77/PyQt6)
\
生成exe文件：

    pyinstaller .\main_ui.spec

生成exe文件后，运行dist文件夹里的“物华弥新小助手.exe”即可
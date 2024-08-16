# WHA开发文档
<p align="center">
  <picture>
    <img src="./image/logo.jpeg" alt="ServerlessLLM" width="30%">
  </picture>
</p>

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
# WHA开发文档
<p align="center">
  <picture>
    <img src="./image/logo.jpeg" alt="ServerlessLLM" width="30%">
  </picture>
</p>

视频介绍：

    【物华弥新小助手1.3】 https://www.bilibili.com/video/BV1gcWAeVE1R/
    【物华弥新小助手1.2】 https://www.bilibili.com/video/BV1QevNemEhU/
    【物华弥新小助手1.1】 https://www.bilibili.com/video/BV11x8zeWEfF/
    【物华弥新小助手1.0】 https://www.bilibili.com/video/BV1Gp8peHEav/

#   代码使用

### 项目结构及功能介绍

```
WHA_dev/
|-main_ui.spec
|-README.md
|-requirements.txt
|-code/
 |-adb.py				###adb模拟器控制代码
 |-Call.py
 |-config.json			###用户设置保存
 |-const.py				
 |-cv.py				###图像识别相关代码
 |-DispatchCompany.py
 |-Fight.py
 |-home.py
 |-known_features.pkl			###标定图片原图预处理后的图片特征
 |-known_features_area.pkl
 |-known_features_button.pkl
 |-log.txt				###日志
 |-logo.ico				
 |-main.py				###程序入口
 |-main_ui.py			###含ui程序入口
 |-preprocess.py		###标定图片原图预处理为pkl文件
 |-SimpleTask.py		###简单功能
 |-tools.py				
 |-known_pic/			###标定图片原图
  |-bulabula.png
  |-...
 |-pic/
 |-ui/					###pyqt6的UI文件
  |-WHA.py
  |-WHA.ui
  |-__init__.py
|-image/				###项目图标
 |-ico_change.py
 |-logo.ico
 |-logo.jpeg
 |-logo2.ico
 |-logo2.jpeg
```

### 程序运行

无`UI`运行程序入口：

```
code/main.py
```

含`UI`运行程序入口：

```
code/main_ui.py
```

### 可执行文件生成

`main_ui.spec`文件中`pathex`参数为`QTDesigner`绝对路径，配置方法请参照[PyQt6](https://github.com/xiaolizhang77/PyQt6)

生成可执行文件指令：

    pyinstaller .\main_ui.spec

生成可执行文件后，将`ui`文件、`pkl`文件、`ico`等文件复制进`dist`文件夹后，运行`dist`文件夹里的`物华弥新小助手.exe`即可。


#   附录  
生成对应`requirement.txt`：

    pip freeze > requirements.txt
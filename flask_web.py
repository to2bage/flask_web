"""
Project name: flask_web
Description:
Create Time: 2020/7/28 08:42
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from app import app

app = app.create_application()


# 打印路由匹配表
print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
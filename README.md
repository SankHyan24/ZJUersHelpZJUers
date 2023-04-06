# ZJUers Help ZJUers
An application for ZJUers to help ZJUers!

## For Devs:
run `make debug` to start the server in debug mode.

## File Structure:
For Frontend Developers:
- All the frontend files should be put in `static` and `templates` folder.

For Backend Developers:
- Use flask as the basic framework.(Python=3.10.8)
- 几把，安装python环境要按requirements.txt里的版本
- 在Makefile里面写东佬

pipreqs --force --encoding=utf8 --savepath requirements.txt
pip install -r requirements.txt

TODO LIST:
- [x] 1. 一个简单的登录界面
- [x] 2. 一个简单的注册界面
- [x] 3. 一个简单的主界面用来进行登录和注册
- [ ] 4. 注册需包含info信息，后端相应添加信息到数据库
- [ ] 5. 添加个人主页，显示个人信息
- [ ] 6. 前端图床接口


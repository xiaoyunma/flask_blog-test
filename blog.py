# encoding:utf-8

from flask import Flask, render_template, request, redirect, url_for, session
#导入数据库配置文件
import config
from exts import db
#导入数据库映射模型
from models import User
from models import Posts

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

#默认进入主页
@app.route('/')
def index():
    return render_template("index.html")

#登录服务功能
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user_id'] = user.id  #保存登录后的id
            session.permanent = True    #30天内保存登录信息
            # 保存此会话
            return redirect(url_for('index'))  #登陆成功继续进入主页
        else:
            return u'手机号码或密码错误'

#注册服务功能
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # 手机号码验证，如果该手机号码已经被注册，就不能被注册
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u'该手机号码已被注册，请更换手机号码！'
        else:
            # 验证两次密码是否一致
            if password1 != password2:
                return u'两次密码不一致，请重新输入！'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)   #向数据库添加注册信息
                db.session.commit()    #提交此会话
                return redirect(url_for('login'))  # 注册成功后跳转到登录界面

#发布博客服务功能
@app.route('/post/', methods=['GET', 'POST'])
def post():
    if request.method == 'GET':
        return render_template('publish.html')
    else:
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        image = request.form.get('image')

        posts = Posts(postsauthor=author, poststitle=title, postscontent=content, postsimage=image)
        db.session.add(posts)
        db.session.commit()
        return redirect(url_for('index'))


#钩子函数，利用之前保存的登录信息，完成相应的功能
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id') #得到用户id
    posts = Posts.query.all()  #得到数据库所有博客信息

    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {"user": user, "posts": posts}   #已字典形式返回相应信息，在前端显示出相应的信息
    else:
        return {}


#注销服务
@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))


#跳转到发布博客界面
@app.route('/publish/')
def publish():
    return render_template('publish.html')


#删除博客列表服务，根据前端传过来的titleid
@app.route('/post_delete/<int:titleid>')
def post_delete(titleid):
    post = Posts.query.get_or_404(titleid)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

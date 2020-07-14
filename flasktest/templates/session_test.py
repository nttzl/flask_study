from flask import session
from datetime import timedelta

# 设置 session
@app.route('/set_session')
def set_session():
    session.permanent = True   # 设置session的持久化
    app.permanent_session_lifetime = timedelta(minutes=5)   # 设置session的存活时间为5分钟
    session['username'] = 'shixiaolou'
    return '成功设置session'

# 获取 session
@app.route('/get_session')
def get_session():
    value = session.get('username')
    return '获取的session值为{}'.format(value)

# 移除 session
@app.route('/del_session')
def del_session():
    value = session.pop('username')
    return '成功移除session，其值为{}'.format(value)
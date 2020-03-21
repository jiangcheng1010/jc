from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('dome.html')

@app.route('/dome', methods=['GET', 'POST'])
def dome():
        getDate = request.args  # 利用request对象获取GET请求数据
        print('获取的GET数据为：', getDate) # 打印获取到的GET数据 ImmutableMultiDict([])
        postData = request.form # 利用request对象获取POST请求数据
        print('获取的POST数据为：', postData) # 打印获取到的POST请求 ImmutableMultiDict([('username', '456'), ('password', '789')])
        ID = request.form.get('ID')
        d1 = request.form.get('d1')
        d2 = request.form.get('d2')
        d3 = request.form.get('d3')
        d4 = request.form.get('d4')
        d5 = request.form.get('d5')
        d6 = request.form.get('d6')
        d7 = request.form.get('d7')
        d8 = request.form.get('d8')
        d9 = request.form.get('d9')
        d10 = request.form.get('d10')
        h1 = request.form.get('h1')
        h2 = request.form.get('h2')
        h3 = request.form.get('h3')
        h4 = request.form.get('h4')
        h5 = request.form.get('h5')
        h6 = request.form.get('h6')
        h7 = request.form.get('h7')
        h8 = request.form.get('h8')
        h9 = request.form.get('h9')
        h10 = request.form.get('h10')
        m1 = request.form.get('m1')
        m2 = request.form.get('m2')
        m3 = request.form.get('m3')
        m4 = request.form.get('m4')
        m5 = request.form.get('m5')
        m6 = request.form.get('m6')
        m7 = request.form.get('m7')
        m8 = request.form.get('m8')
        print(ID,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10)
        print( h1, h2, h3, h4, h5, h6, h7, h8, h9,h10)
        print(m1, m2, m3, m4, m5, m6, m7, m8)
        return '已获得测试数据'
if __name__ == '__main__':
    app.run(debug=True)
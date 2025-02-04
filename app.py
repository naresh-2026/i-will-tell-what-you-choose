from flask import Flask,render_template,request,jsonify,session
app = Flask(__name__)
count=0
@app.route("/")
def home():
    return render_template('startPage.html')
@app.route('/next',methods=['POST'])
def page1():
    return render_template('page1.html')
@app.route('/play Again',methods=['POST'])
def startPage():
    return render_template('startPage.html')
@app.route('/submit', methods=['POST'])
def submit_number():
    data = request.json
    number = data.get('number', 0)
    global count
    count += int(number)
    return jsonify({'received_number': count})
@app.route('/page2')
def page2():
    return render_template('page2.html')
@app.route('/page3')
def page3():
    return render_template('page3.html')
@app.route('/page4')
def page4():
    return render_template('page4.html')
@app.route('/page5')
def page5():
    return render_template('page5.html')
@app.route('/page6')
def page6():
    return render_template('page6.html')
@app.route('/page7')
def page7():
    return render_template('page7.html')
@app.route('/finalPage')
def finalPage():
    global count
    data=""
    if count==1200:
        data="apple"
    elif count==1300:
        data="banana"
    elif count==1400:
        data="grape"
    elif count==1500:
        data="mango"
    elif count==1600:
        data="orange"
    elif count==1700:
        data="pine apple"
    elif count==1800:
        data="pomegranate"
    elif count==1900:
        data="strawberry"
    if(count>=1200 and count<=1900):
        count=0
        data1="the item you selected is "+data
        return render_template('finalPage.html',content=data1)
    else:
        count=0
        return render_template('finalPage.html',content="You have given something wrong")
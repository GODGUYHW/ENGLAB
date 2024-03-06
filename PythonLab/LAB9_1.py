from flask import Flask
app = Flask(__name__)
 
@app.route('/<opt>/<float:a>/<float:b>')
 
def cal(opt,a,b):
    ans = None
    if opt == 'add':
        ans = a+b
    elif opt == 'sub':
        ans = a-b
    elif opt=='mul':
        ans = a*b
    elif opt=='div':
        if b == 0:
            return 'Error'
        else:
            ans = a/b
    else:
        return  'Hi'
   
    return f'Answer: {ans}'
 
       
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
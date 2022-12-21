from model import get_response, get_response2
from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get')
def getMessage():
    message = request.args.get('msg')
    response1 = get_response(message)
    response2 = get_response2(message)
    print (f'response1 {response1}')
    print (f'response2 {response2}')
    return str(response1) +'<br>'+str(response2)

        
    return response1 + '<br>' + response2

# main driver function
if __name__ == '__main__':
    app.run()
from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host= 'localhost', 
        port= 2024,
        debug= True,
        load_dotenv= True
    )
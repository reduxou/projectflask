from flask import Flask
app = Flask(__name__)

@app.route('/')
def alo_mundo():
    return 'Alô, Mundo!'

if __name__ == '__main__':
    app.run()
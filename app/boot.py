
from flask import Flask, Response, render_template, request, url_for
from datetime import datetime

#__name__ = "app"

app = Flask(__name__)
pub = open("id_rsa.pub").read()

@app.route("/boot")
def boot():
    mac = request.args.get('mac')
    #server = request.environ['SERVER_NAME']
    #server = request.host.split(':')[0]
    server = request.host
    return Response(render_template('.boot.tmpl', mac = mac, server = server), mimetype='text/plain')

@app.route("/run")
def run():
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    mac = request.args.get('conf')
    return Response(render_template('.run.tmpl', mac = mac, date = date, pub = pub), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

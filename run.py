__author__ = 'ISY'

from app.app import app


if __name__ == '__main__':
    if app.config['CERTFOLDER']:
        context = (f"{app.config['CERTFOLDER']}/server.pem", f"{app.config['CERTFOLDER']}/private_key.pem")
        app.run(debug=app.config['DEBUG'], ssl_context=context, host=app.config['HOST'], port=app.config['PORT'])
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])

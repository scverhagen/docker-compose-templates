#!/usr/bin/python3

from flask import Flask, request, send_file, render_template, redirect, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

app.config.update(
    CELERY_BROKER_URL='redis://redis:6379'
)

from celery import Celery
def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
celery = make_celery(app)

@app.route('/')
def www_root():
    ru = request.url_root
    if ru[-1] == '/':
        ru = ru[0:-1]
    return render_template('index.html', ru=ru)

if __name__ == '__main__':
    app.run(debug=True,port=5000)

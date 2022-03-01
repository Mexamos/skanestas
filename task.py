from celery import Celery

app = Celery('task', broker='redis://localhost:6379/0')

@app.task
def update():
    print('hello')

app.conf.beat_schedule = {
    'update-tickers': {
        'task': 'task.update',
        'schedule': 10.0
    }
}
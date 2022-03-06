from apscheduler.schedulers.blocking import BlockingScheduler

from clickhouse import init_db
from jobs import update_prices

scheduler = BlockingScheduler()
scheduler.add_job(
    update_prices,
    name='update_prices',
    trigger='interval',
    seconds=1,
)

if __name__ == '__main__':
    try:
        init_db()
        scheduler.start()
    except KeyboardInterrupt:
        print('Scheduler manually stopped')
    finally:
        scheduler.shutdown()

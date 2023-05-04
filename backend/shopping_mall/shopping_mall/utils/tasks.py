from celery import Celery

app = Celery("shopping_mall_app", backend="redis://127.0.0.1/10", broker="redis://127.0.0.1/11")

# 加载配置
# app.config_from_object("celery_tasks.config")

#注册异步任务
# app.autodiscover_tasks(['celery_tasks.sms'])

@app.task
def test():
    pass

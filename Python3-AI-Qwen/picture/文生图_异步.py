from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis
import os

prompt = "一间有着精致窗户的花店，漂亮的木质门，摆放着花朵"


def async_call():
    print('----create task----')
    task_info = create_async_task()
    print('----wait task done then save image----')
    wait_async_task(task_info)


# 创建异步任务
def create_async_task():
    rsp = ImageSynthesis.async_call(
        # api_key=os.getenv("DASHSCOPE_API_KEY"),
        api_key="sk-796c2eb58df24dccb67c5892a9107810",
        model="wanx2.1-t2i-turbo",
        prompt=prompt,
        n=1,
        size='1024*1024')

    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
    return rsp


# 等待异步任务结束
def wait_async_task(task):
    rsp = ImageSynthesis.wait(task)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        for result in rsp.output.results:
            file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
            with open('./%s' % file_name, 'wb+') as f:
                f.write(requests.get(result.url).content)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


# 获取异步任务信息
def fetch_task_status(task):
    status = ImageSynthesis.fetch(task)
    print(status)
    if status.status_code == HTTPStatus.OK:
        print(status.output.task_status)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (status.status_code, status.code, status.message))


# 取消异步任务，只有处于PENDING状态的任务才可以取消
def cancel_task(task):
    rsp = ImageSynthesis.cancel(task)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output.task_status)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    async_call()

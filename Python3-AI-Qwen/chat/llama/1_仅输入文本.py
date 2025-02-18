from http import HTTPStatus
import os
import dashscope


def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '介绍一下自己'}]
    response = dashscope.Generation.call(
        # api_key=os.getenv('DASHSCOPE_API_KEY'),
        api_key="sk-796c2eb58df24dccb67c5892a9107810",
        model='llama3.3-70b-instruct',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == '__main__':
    call_with_messages()

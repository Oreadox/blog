# encoding: utf-8

def fail_msg(msg):
    message = {
        "status": 0,
        "message": msg
    }
    return message


success_msg = {
    "status": 1,
    "message": "成功!"
}

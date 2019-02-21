# encoding: utf-8

def to_json(dict):
    if "_sa_instance_state" in dict:
        del dict["_sa_instance_state"]
    return dict


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

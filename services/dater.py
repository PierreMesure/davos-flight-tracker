import time

def date_from_epoch(epoch):
    return time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(epoch // 1000))

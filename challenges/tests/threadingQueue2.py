from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from time import sleep
from threading import Thread


def retry(status, time_sleep=5):
    sleep(time_sleep)
    pending_tasks[executor.submit(bool, status)] = status


executor = ThreadPoolExecutor(3)
conditions = [1, 0, 1]

pending_tasks = {executor.submit(bool, status): status for status in conditions}


while pending_tasks:
    done, _ = wait(pending_tasks, timeout=0, return_when=FIRST_COMPLETED)
    for task in done:
        status = task.result()
        print(status)
        if not status:
            thread = Thread(target=retry, args=(status,), daemon=True)
            thread.start()
            thread.join()
        del pending_tasks[task]

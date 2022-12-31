from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import time
import threading
import _thread


class Task:
    def __init__(self, task):
        self.task = task

    def doSomething(self):
        if self.task.get("name") == "task3":
            return False
        return True


def retry(task, time_sleep):
    global pending_tasks
    time.sleep(time_sleep)
    pending_tasks[executor.submit(Task(task).doSomething)] = task


def set_timeout(time_sleep):
    time.sleep(time_sleep)
    _thread.interrupt_main()


tasks = ["task1", "task2", "task3"]
tasks = [Task({"name": t, "retries": 0}) for t in tasks]

done_tasks = []
failed_tasks = []

try:
    threading.Thread(target=set_timeout, args=(15,)).start()
    with ThreadPoolExecutor(max_workers=3) as executor:
        global pending_tasks
        pending_tasks = {executor.submit(t.doSomething): t.task for t in tasks}
        tasks = []
        while pending_tasks:
            done, not_done = wait(pending_tasks, timeout=0, return_when=FIRST_COMPLETED)
            for future in done:
                result = future.result()
                task = pending_tasks[future]
                print(future.exception())
                if result == False:
                    if task.get("retries") < 3:
                        task["retries"] += 1
                        t = threading.Thread(
                            target=retry,
                            args=(
                                task,
                                3,
                            ),
                            daemon=True,
                        )
                        t.start()
                        t.join()
                    else:
                        failed_tasks.append(task)
                else:
                    done_tasks.append(task)

                del pending_tasks[future]
except KeyboardInterrupt:
    pass
print(done_tasks)
print(failed_tasks)

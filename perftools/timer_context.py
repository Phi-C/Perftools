import time

class TimerContext:
    """Used to measure the time cost of a block of code.
   
    Usage:
        with TimerContext("sleep") as timer:
            // target_code_block
            ...
    """
    def __init__(self, name, verbose=True):
        self.name = name.upper()
        self.verb = verbose

    def __enter__(self):
        if self.verb:
            self.start_time = time.time()
            print(f"[START_{self.name}]: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.verb:
            self.end_time = time.time()
            self.elapsed_time = self.end_time - self.start_time
            print(f"[END_{self.name}]: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
            print(f"{self.name} cost: {self.elapsed_time:.4f} s")

if __name__ == "__main__":
    with TimerContext("sleep") as timer:
        time.sleep(2)
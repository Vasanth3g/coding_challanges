import signal

class GracefulDeath:
    """Catch signals to allow graceful shutdown."""

    def __init__(self):
        self.receivedSignal = self.receivedTermSignal = False
        catchSignals = [
            1,
            2,
            3,
            10,
            12,
            15,
        ]
        for signum in catchSignals:
            signal.signal(signum, self.handler)

    def handler(self, signum, frame):
        print("Caught signal %d" % signum)
        self.lastSignal = signum
        print("Received signal %d" % signum)
        self.receivedSignal = True
        if signum in [2, 3, 15]:
            self.receivedTermSignal = True
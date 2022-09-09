from threading import Lock, Thread


class LoggerSingleton:
    '''
        Implement a Logger class using Singleton which logs messages. 
        Logger accepts a value sink which can be either "console" or "file_name" in which,
        it prints to the console in the former and to the given file in the later case.
        Here, for simplicity print to console in both cases.
    '''
    _sink = None

    def log(self, msg):
     	print(msg)


def test_singleton(sink):
    singleton = Singleton(sink)
    return singleton._sink

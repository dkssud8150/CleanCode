import contextlib

class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()
    
    def __exit(self, ext_type, ex_value, ex_traceback):
        start_database()

@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")
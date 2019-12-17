import multiprocessing
import os


bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() * 2 + 1
reload = True if os.environ.get("ENV") == "DEV" else False
errorlog="-"
accesslog="-"

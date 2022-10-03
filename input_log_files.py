import os
import operation
import datetime as dt
import output_txt as out

# TODO : for future first create the interface for any input log format and consider in
#  real scenario logs come from syslog or logstash in stream format
# reading log files in path


def get_logs(path):
    start_time = dt.datetime.now()
    total_log = 0   # number of all log for calculate eps
    bytes_exchanged = 0     # number of bytes exchanged for output result
    try:
        # iterate through all file
        for file in os.listdir():
            # Check whether file is in text format or .log
            if file.endswith(".txt") or file.endswith(".log"):
                file_path = f"{path}\\{file}"
                with open(file_path) as f:
                    for line in f:
                        # check for empty line or invalid log, suppose each event has at least 10 fields
                        if len(line.split()) > 9:
                            # TODO : should implement in thread for huge log
                            operation.operate_log(line)
                            # getting number of bytes exchanged , we do not use length of file
                            # because for future work (stream base log) this method needed
                            bytes_exchanged += len(line.encode('utf-8'))
                            total_log += 1
                        else:
                            print('invalid log format detected !\n log was: ' + line)
                f.close()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

    end_time = dt.datetime.now()  # end time of reading logs and operating on them
    eps = total_log  # default eps(event per second) for small log file , this escape division by zero
    if (end_time - start_time).total_seconds() > 0:
        # TODO : calculate eps for each second in future
        eps = total_log / (end_time - start_time).total_seconds()  # calculate average event per second

    out.eps = eps
    out.bytes_exchanged = bytes_exchanged
    out.path = f"{path}"


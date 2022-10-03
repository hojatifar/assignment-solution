import os.path
import input_log_files
import output_txt

# start point of tool
if __name__ == '__main__':
    # get path of log files from user input
    path = input('Enter path of log files (Directory of log files):\n')
    # check the user input for correct path of files
    while not os.path.isdir(path):
        path = input('Path is not correct! Please enter path (Directory of log files):\n')

    input_log_files.get_logs(path)  # TODO : should implement in thread for future and real scenario
    output_txt.write_file()

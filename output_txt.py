import datetime
import operation
import json

eps = 0
bytes_exchanged = 0
most_frequent_ip = []
most_frequent_num = 0
least_frequent_ip = []
least_frequent_num = 0
output_content = {}
path = '.'


# TODO : Should implement IOutput for future (to support any output format)
# write output in json format
def write_file():
    get_operation_data()
    file_postfix_name = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    output_filename = "output-" + str(file_postfix_name) + ".json"
    file_path = f"{path}\\{output_filename}"
    print('### output file generated successfully in : ' + file_path)
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(output_content, f, ensure_ascii=False, indent=4)
    # json.dump(output_content)
    # f.write()
    f.close()


def get_operation_data():
    operation.get_frequent_ips()
    output_content["most_frequent_ips"] = operation.most_frequent_ip
    output_content["number_of_most_frequency"] = operation.most_frequent_num
    output_content["least_frequent_ips"] = operation.least_frequent_ip
    output_content["number_of_least_frequency"] = operation.least_frequent_num

    output_content["eps"] = eps
    output_content[" byte_exchanged"] = bytes_exchanged



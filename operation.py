ips = {}    # storing IPs as key and frequency of them as value in dictionary
most_frequent_ip = []   # list of most frequent ips
most_frequent_num = 1   # number of most frequent ips
least_frequent_ip = []  # list of the least frequent ips
least_frequent_num = 1000000    # number of the least frequent ips


# TODO : for future should implement event class, any operation on source_ip,
#  dest_ip , ... need to have proper obj of each log
def operate_log(log):
    field_list = log.split()
    timestamp = field_list[0]
    response_header_size = field_list[1]
    client_ip_address = field_list[2]
    http_response_code = field_list[3]
    response_size = field_list[4]
    http_request_method = field_list[5]
    url = field_list[6]
    username = field_list[7]
    access_type__destination_ip = field_list[8]
    access_type = str(access_type__destination_ip).split('/')[0]
    # some destination_ip is "-", in this situation we can use ipaddress library in python for check correct ip format
    # , but I ignore this issue , because it decreases the performance , and it can be useful for analysis (null ip !)
    destination_ip = str(access_type__destination_ip).split('/')[1]
    response_type = field_list[9]

    # Because nothing was said about the IP type in the assignment, here both the client IP and
    # the destination IP were considered together. In the future, this processing should be
    # done separately for the source and destination IPs for better analysis.
    # TODO : for future work need to use redis (for storing huge log and
    #  its performance in key value search and ...)
    if client_ip_address not in ips:
        ips.update({client_ip_address: 1})
    else:
        val = ips[client_ip_address]
        ips.update({client_ip_address: val+1})

    if destination_ip not in ips:
        ips.update({destination_ip: 1})
    else:
        val = ips[destination_ip]
        ips.update({destination_ip: val+1})


def get_frequent_ips():
    max_num = 1
    min_num = 100000
    # for finding max and min number
    for x in ips:
        if ips[x] > max_num:
            max_num = ips[x]
            # most_frequent_ip = x  ## for one result this is enough
        if ips[x] < min_num:
            min_num = ips[x]
            # least_frequent_ip = x  ## for one result this is enough

    # for getting all ip with max repeat and min repeat
    for x in ips:
        if ips[x] == max_num:
            most_frequent_ip.append(x)
        elif ips[x] == min_num:
            least_frequent_ip.append(x)
    global most_frequent_num, least_frequent_num
    most_frequent_num = max_num
    least_frequent_num = min_num


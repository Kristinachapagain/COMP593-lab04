import sys
import os 
import re 
def main():
    log_file = get_log_file_path_from_cmd_line()
    filter_log_by_regex(log_file, 'sshd')

def get_log_file_path_from_cmd_line():
    number_parameters = len(sys.argv) - 1
    if number_parameters >= 1:
        log_file_path = sys.argv[1]
        if os.path.isfile(log_file_path):
            return os.path.abspath(log_file_path)
        else: 
            print("Error: Log file does not exist.")
            sys.exit(1)
    else: 
        print("Error: Missing log file.")
        sys.exit(1)


def get_log_file_path_from_cmd_line():

    return

# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex.

    Args:
        log_file (str): Path of the log file
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.

    Returns:
        (list, list): List of records that match regex, List of tuples of captured data
    """
    matching_records = []
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(regex, line)
            if match: 
                matching_records.append(line)
    print(*matching_records, sep='')




    return

# TODO: Step 8
def tally_port_traffic(log_file):
    return

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()
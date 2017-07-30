import os


# Creates a project folder if one does not already exist
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project: " + directory)
        os.makedirs(directory)


# change this later, REMEMBER STEEVE
# create_project_dir("thenewboston")


# create queue and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"

    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, "")


# next two functions are house-keeping, just making and
# writing to files
def write_file(path, data):
    with open(path, "w") as f:
            f.write(data)


# Add data onto existing file
# which file, what to append to it
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete file contents, basically opening a new blank file
# w/ same name
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read file, convert each line to set elements
def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))

    return results


# Iterate through set, each line of set wil be new line of file
def set_to_file(links, filename):
    with open(filename, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")
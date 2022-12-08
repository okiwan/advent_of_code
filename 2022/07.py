from helpers import read_input

def get_file_struct(data):
    structure = {'/': {'size': 0, 'nodes': {}}}
    breadcrum = []

    # First step: re-create the folder structure
    for line in data:
        line_elements = line.split(' ')

        if line_elements[0] == '$':
            if line_elements[1] == 'cd':
                dirname = line_elements[2]

                if dirname == '..':
                    breadcrum.pop()
                else:
                    if dirname == '/':
                        breadcrum.append(structure['/'])
                    else:
                        if dirname not in breadcrum[-1]['nodes']:
                            breadcrum[-1]['nodes'][dirname] = {
                                'size': 0,
                                'nodes': {}
                            }

                        breadcrum.append(breadcrum[-1]['nodes'][dirname])
            elif line_elements[1] == 'ls':
                # We can pretty much ignore this command
                continue
        else:
            dirname = line_elements[1]

            if dirname not in breadcrum[-1]['nodes']:
                if line_elements[0] == 'dir':
                    breadcrum[-1]['nodes'][dirname] = {
                        'size': 0,
                        'nodes': {}
                    }
                else:
                    breadcrum[-1]['nodes'][dirname] = {
                        'size': int(line_elements[0]),
                    }

                    # Update folder sizes
                    for node in breadcrum:
                        node['size'] += int(line_elements[0])

    return structure

def get_size_for_le10k_folders(element):
    current_size = 0

    if 'nodes' in element:
        for node_element in element['nodes'].values():
            current_size += get_size_for_le10k_folders(node_element)

        if element['size'] <= 100000:
            current_size += element['size']

    return current_size

def get_folder_sizes(element):
    folder_sizes = []

    if 'nodes' in element:
        for node_element in element['nodes'].values():
            folder_sizes.extend(get_folder_sizes(node_element))

        folder_sizes.append(element['size'])

    return folder_sizes

data = read_input("07.in")
output = get_file_struct(data)
output_size = get_size_for_le10k_folders(output['/'])
print(f"Question 1's answer if {output_size}")

"""
Question 2
"""
file_system_size = 70000000
required_free_space = 30000000
currently_used = output['/']['size']
current_free_space = file_system_size - currently_used

# We need to find a folder that weights the closest to this number
required_space_to_free = required_free_space - current_free_space

folder_sizes = sorted(get_folder_sizes(output['/']))

#print('---')
#print(required_space_to_free)
#print(folder_sizes)
#print('---')

candidate = None
for size in reversed(folder_sizes):
    if size >= required_space_to_free:
        candidate = size

print(f"Question 2's answer is {candidate}")

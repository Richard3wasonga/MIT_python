# File Objects

# without context manager
# f = open('text.txt', 'r')

# print(f.mode)

# f.close()

# with context manager
with open('text.txt', 'r') as f:

    # for line in f:
    #     print(line, end='')

    size_to_read = 10

    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    # used to manipulate position of file pointer/cursors
    # f.seek(0)

    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')
    
    # used to tell position file pointer is at
    # print(f.tell())

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

# if you use w it overwrites the file so if you have content and just want to add use a 
# with open('text.txt', 'r') as rf:
#     with open('text_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

with open('city_view.jpg', 'rb') as rf:
    with open('city_view_copy.jpg', 'wb') as wf:
        chunk_size =4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

        # also this works
        # for line in rf:
        #     wf.write(line)
    


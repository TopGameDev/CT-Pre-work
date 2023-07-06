def is_consecutive(a_list):
    a_list = sorted(a_list)
    for list in range(0, len(a_list)):
        if a_list[list] == a_list[list - 1] + 1:
            print("True")
            

unsorted_list = [1,2,4,5,3,6]
is_consecutive(unsorted_list)
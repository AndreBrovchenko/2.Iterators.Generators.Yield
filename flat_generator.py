def flat_generator(input_list):
    list_flat = [list_item for internal_list in input_list for list_item in internal_list]
    start = 0
    end = len(list_flat)
    while start < end:
        yield list_flat[start]
        start += 1
    # for item_list in list_flat:
    #     yield item_list

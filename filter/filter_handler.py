import filter.filters_types.random_patch_filter as random_patch_filter



def filter_factory(filter_num):
    print("in factory of filter")

    if filter_num == 1:
        return random_patch_filter.RandomPatch()


def get_filters(filters):
    print("in filter handler")

    filter_list = []
    for num_filter in filters:
        filter_list.append(filter_factory(int(num_filter)))
    return filter_list
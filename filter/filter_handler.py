import filter.filters_types.random_patch_filter as random_patch_filter
import filter.filters_types.time_filer as time_filter



def filter_factory(filter_num):
    print("in factory of filter")

    if filter_num == 1:
        args = input("insert from - to").split()
        print(args)
        filter = time_filter.Time_filter(args[0],args[1], args[2])
        print(filter)
        return filter


def get_filters(filters):
    print("in filter handler")

    filter_list = []
    for num_filter in filters:
        filter_list.append(filter_factory(int(num_filter)))
    return filter_list
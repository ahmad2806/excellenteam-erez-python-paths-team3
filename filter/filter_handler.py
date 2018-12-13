import filter.filters_types.random_patch_filter as random_patch_filter
import filter.filters_types.time_filer as time_filter


def filter_factory(filter_num):
    if filter_num == 1:
        args = input("insert : [from Hour] [to Hour] [date] : date format YYYY-MM-DD(0 for all dates)\n").split()
        filter = time_filter.Time_filter(args[0], args[1], args[2])
        return filter


def get_filters(filters):
    filter_list = []
    for num_filter in filters:
        filter_list.append(filter_factory(int(num_filter)))
    return filter_list

import filter.filters_types.random_patch_filter as random_patch_filter
import filter.filters_types.specific_patch_filter as specific_patch_filter



def filter_factory(filter_num):
    if filter_num == 1:
        return random_patch_filter.RandomPatch()


def get_filters(filters):
    filter_list = []
    for num_filter in filters:
        filter_list.append(filter_factory(int(num_filter)))
    return filter_list
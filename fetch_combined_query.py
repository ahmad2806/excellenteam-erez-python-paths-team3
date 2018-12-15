import data.data_api as data_api


def combine_query_get_pathes_from_db(filter_list):
    print("in fetch query of filters")
    pathes = data_api.get_pathes(filter_list)
    return pathes

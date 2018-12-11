import filter.filter_handler as filter_handler
import fetch_combined_query

def create_filters():
    filters = input("insert filters: ").split(",")
    filter_list = filter_handler.get_filters(filters)
    pathes = fetch_combined_query.combine_query_get_pathes_from_db(filter_list)




def display_filters():
    return None


def change_filter():
    return None


def set_mode():
    return None
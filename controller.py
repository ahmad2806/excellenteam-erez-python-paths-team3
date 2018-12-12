import filter.filter_handler as filter_handler
import fetch_combined_query
import display.display_handler as display_handler


def create_filters():
    print("in controller")
    print("in create filter")

    filters = input("insert filters: ").split(",")
    filter_list = filter_handler.get_filters(filters)
    pathes,objs = fetch_combined_query.combine_query_get_pathes_from_db(filter_list)
    display_handler.use_display(pathes,objs)


def display_filters():
    return None


def change_filter():
    return None


def set_mode():
    return None

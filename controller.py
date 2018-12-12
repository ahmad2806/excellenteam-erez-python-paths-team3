import filter.filter_handler as filter_handler
import fetch_combined_query
import display.display_handler as display_handler
import configrations

g_filters = []

def create_filters():
    global g_filters
    print("in controller")
    print("in create filter")
    filters = input(f"insert filters: {configrations.filters}").split(",")
    g_filters = filter_handler.get_filters(filters)
    pathes ,objs = fetch_combined_query.combine_query_get_pathes_from_db(g_filters)
    display_handler.use_display(pathes,objs)


def display_filters():
    global g_filters
    for filter in g_filters:
        filter.print()


def change_filter():
    return None


def set_mode():
    return None

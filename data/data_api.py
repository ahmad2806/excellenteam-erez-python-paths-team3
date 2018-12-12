from data import file_handler
import pandas as pa

df = None
check = True


def get_df():
    global df
    global check
    if check:
        df = file_handler.load_file("/Users/odaiodeh/PycharmProjects/path_project_prep/mypkl.pkl.xz")
        check = False


def get_pathes(filter_list):
    global df
    ##get data df from csv
    get_df()
    local_df = df.copy()

    ##all filters
    for filter in filter_list:
        ## df on filters , df will get changed
        local_df = filter.get_query(local_df)

    ## group filters
    objs = local_df.groupby(['filename', 'objectNum']).size()
    df_by_obj = local_df.set_index(['filename', 'objectNum']).sort_index()

    if objs.empty:
        print(" none")
    else:
        print("not none")

    ##return pathes form group
    return df_by_obj, objs

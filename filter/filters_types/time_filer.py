import pandas as pa


class Time_filter():

    def __init__(self, from_time, to_time, date):
        self.from_time = from_time
        self.to_time = to_time
        if date == '0':
            self.date = 0
            print("hi")
        else:
            self.date = pa.to_datetime(date)

    def get_query(self, df):
        if self.date == 0:
            tf = df[df.time.dt.hour.between(int(self.from_time), int(self.to_time))]
        else:
            tf = df[
                df.time.dt.hour.between(int(self.from_time), int(self.to_time)) & (df.time.dt.date == self.date.date())]

        return tf

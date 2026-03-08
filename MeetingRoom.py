
class Meeting:
    def __init__(self, sttime: int, endtime: int, index: int):
        self.sttime = sttime
        self.endtime = endtime
        self.index = index

    def __repr__(self):
        return f"Meeting(sttime={self.sttime}, endtime={self.endtime}, index={self.index})"


def meetingroom(start: list, end: list):
    freetime,count=0,0
    meetings = [Meeting(start[i], end[i], i) for i in range(len(start))]
    meetings.sort(key=lambda m: m.endtime)
    for meet in meetings:
        if meet.sttime > freetime:
            count+=1
            freetime=meet.endtime
    return count



if __name__ == "__main__":
    print(meetingroom([0, 3, 1, 5, 5, 8], [5, 4, 2, 9, 7, 9]))



import datetime

# Returns all entries in the JSON file in a list.
def ReturnJSONAsList(jsonObject):
    listAll = []

    for x in  jsonObject[0].json['entries']:
        listAll.append(x)

    return listAll

# Return Stop objects with specified marker and
# the duration spent on that marker (Vogabyggd JSON file)
# The Stop object has attributes, "marker" and "duration"
def UltimateTest(data):
    allStops = []

    r = False
    marker = ''
    time1 = ''
    time2 = ''
    for x in data[0].json['entries']:
        if (x['contents'][1] == 'S' and not r):
            r = True
            time1 = ConvertTimestamp(x['timestamp'])
            marker = x['contents']
            #print(x['contents'] + ' ' + time1)
        elif (x['contents'] == '[out-start]' and r):
            r = False
            time2 = ConvertTimestamp(x['timestamp'])
            #print(x['contents'] + ' ' + time2)

            duration = SubtractTime(time1,time2)
            #print('Time spent on stop: ' + str(duration))

            obj = Stop(marker, duration)
            allStops.append(obj)

    return allStops

def ConvertTimestamp(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp / 1e3)
    fmt = "%Y-%m-%d %H:%M:%S"

    return date.strftime(fmt)

def SubtractTime(time2,time1):
    d1 = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
    d2 = datetime.datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")

    return d1-d2

class Stop(object):

    def __init__(self,marker,duration):
        self.marker = marker
        self.duration = duration

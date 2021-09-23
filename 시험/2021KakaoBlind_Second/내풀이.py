import json, requests
from collections import deque

base_url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
headers = {
    'X-Auth-Token': '4205e29e873a08e2040c091923b068a1',
    'Content-Type': 'application/json'
}
token ="69c88758dd0806b3eb703cad187be486"
parameter = {'problem': 1}

class TruckCommands:
    def __init__(self, id, commands):
        self.id = id
        self.commands = commands

    def asJson(self):
        return {
            'truck_id': self.id,
            'command': self.commands
        }

## 자전거 대여소 및 트럭에 대한 정보를 초기화 한다.
def postStart():
    url = base_url + '/start'
    data = '{"problem": 1}'
    response = requests.post(url, headers = headers, data = data)
    response_json = response.json()
    print("start() (status_code: %d) (response: %s) " %(response.status_code, response_json))
    return response_json

def makeAccessHeader(start_response):
    return {
        'Authorization': start_response,
        'Content-Type': 'application/json'
    }


## 각 자전거 대여소가 보유한 자너거 수
def getLocations(auth_key):
    print("getLocations()")
    url = base_url + '/locations'
    headers = makeAccessHeader(auth_key)
    response = requests.get(url, headers = headers)
    response_json = response.json()
    locations = response_json['locations']
    for location in locations:
        print(location)
    print("\n\n")
    return response_json

## 현재 (1)각 트럭의 위치 (2) 싣고 있는 자전 거 수
def getTrucks(auth_key):
    print("getTrucks()")
    url = base_url + '/trucks'
    headers = makeAccessHeader(auth_key)
    response = requests.get(url, headers = headers)
    response_json = response.json()['trucks']
    for truck in response_json:
        print(truck)
    print('\n')
    return response_json

def simulate(auth_key, command_list):
    url = base_url + '/simulate'
    headers = makeAccessHeader(auth_key)
    commands = json.dumps({"commands": command_list})
    print(commands)
    response = requests.put(url, headers = headers, data=commands)
    response_json = response.json()
    print("simulate() (status_code: %d) (response: %s) " %(response.status_code, response_json))
    return response_json

def getScore(auth_key):
    url = base_url + '/score'
    headers = makeAccessHeader(auth_key)
    response = requests.get(url, headers = headers)
    response_json = response.json()
    print("getScore() (status_code: %d) (response: %s) " %(response.status_code, response_json))
    return response_json

def getCommands(start, end, problem):
    start_id, end_id = start['id'], end['id']
    start_bikes_count, end_bikes_count = start['located_bikes_count'], end['located_bikes_count']
    commands = deque([])
    if start_id > end_id:
        mok = (start_id - end_id) // 5
        namujee = (start_id - end_id) % 5

        if problem == 1:
            commands = deque([5 for _ in range(start_bikes_count, 2, -1)])
        else:
            commands = deque([5 for _ in range(start_bikes_count, 4, -1)])
        for _ in range(mok):
            commands.append(4)
        for _ in range(namujee):
            commands.append(3)

        if problem == 1:
            for _ in range(start_bikes_count, 2, -1):
                commands.append(6)
        else:
            for _ in range(start_bikes_count, 4, -1):
                commands.append(6)


    else:
        mok = (end_id - start_id) // 5
        namujee = (end_id - start_id) % 5
        if problem == 1:
            commands = deque([5 for _ in range(start_bikes_count, 2, -1)])
        else:
            commands = deque([5 for _ in range(start_bikes_count, 4, -1)])
        for _ in range(mok):
            commands.append(2)
        for _ in range(namujee):
            commands.append(1)
        if problem == 1:
            for _ in range(start_bikes_count, 2, -1):
                commands.append(6)
        else:
            for _ in range(start_bikes_count, 4, -1):
                commands.append(6)
    return commands

def getDist(start_id, end_id):
    mok, namujee, dir = 0, 0, 0
    if start_id > end_id:
        mok = (start_id - end_id) // 5
        namujee = (start_id - end_id) % 5
        dir = 0
    else:
        mok = (end_id - start_id) // 5
        namujee = (end_id - start_id) % 5
        dir = 1
    return (mok, namujee, dir)





start_response = postStart()
AUTH_KEY = start_response['auth_key']

for i in range(20):
    locations = getLocations(AUTH_KEY)
    if i == 0:
        simulate(AUTH_KEY, [])
        continue
    stops = locations['locations']
    ## 가장 많은 곳, 가장 적은 곳 구하기
    min_stop = min(stops, key=lambda stop: stop['located_bikes_count'])
    max_stop = max(stops, key=lambda stop: stop['located_bikes_count'])
    print("start = {start}, end = {end}".format(start = max_stop, end = min_stop))
    ## 가장 많은 곳 -> 가장 적은 곳 명령어 구하기
    commands = getCommands(max_stop, min_stop, parameter['problem'])

    ## 가장 많은 곳과 가장 가까운 트럭 구하기
    trucks = getTrucks(AUTH_KEY)
    min_dist_bus = (-1, 1e9, 1e9, -1, -1)
    for truck in trucks:
        id, loaded_bikes_count, location_id = truck.values()
        min_dist = min_dist_bus[1]
        dist_mok, dist_namujee, dir = getDist(max_stop['id'], location_id)
        if min_dist > dist_mok + dist_namujee:
            min_dist_bus = (id, dist_mok, dist_namujee, dir, location_id)
    if min_dist_bus[3]:
        for _ in range(min_dist_bus[1]):
            commands.appendleft(2)
        for _ in range(min_dist_bus[2]):
            commands.appendleft(1)
    else:
        for _ in range(min_dist_bus[1]):
            commands.appendleft(4)
        for _ in range(min_dist_bus[2]):
            commands.appendleft(3)

    result_command = [TruckCommands(min_dist_bus[0], list(commands)).asJson()]
    simulate(AUTH_KEY, result_command)
getScore(AUTH_KEY)




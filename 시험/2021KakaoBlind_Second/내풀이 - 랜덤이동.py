import json, requests, random
## 210.74488095238095 점
base_url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
tcommand = {
    'not': 0,
    'up': 1,
    'right': 2,
    'down': 3,
    'left': 4,
    'bike_up': 5,
    'bike_down': 6
}


## 자전거 대여소 및 트럭에 대한 정보를 초기화 한다.
# 반환 값: auth_key
def start(pid):
    url = base_url + '/start'
    data = {"problem": pid}
    headers = {
        'X-Auth-Token': 'f003e6ca4e7aea545b55bdc780521e64',
        'Content-Type': 'application/json'
    }
    ## data 부분만 dumps를 한다. json.dumps() JSON으로 직렬화를 하는 것이다.
    res = requests.post(url, headers=headers, data=json.dumps(data))
    return res.json()['auth_key']


# 각 시간마다 ->  각 정류장에서 보관중인 자전거의 수: 정류장 id, 자전거
#    { "id": 0, "located_bikes_count": 3 }
def getLocations(base_url, headers, msize):
    res = requests.get('/'.join([base_url, 'locations']), headers=headers)
    j = res.json()
    bicycles = [0 for _ in range(msize * msize)]
    for id, count in [(location['id'], location['located_bikes_count']) for location in j['locations']]:
        bicycles[id] = count
    return bicycles


class Truck:
    def __init__(self):
        self.id = 0
        self.location_id = 0
        self.bikes_count = 0

    def set(self, id, location_id, bikes_count):
        self.id, self.location_id, self.bikes_count = id, location_id, bikes_count

    def __str__(self):
        return '(id: {id} -  bikes_count: {bikes_count})'.format(id=self.id, bikes_count=self.bikes_count)

    def __repr__(self):
        return '(id: {id} - bikes_count: {bikes_count})'.format(id=self.id, bikes_count=self.bikes_count)


# 각 시간마다 -> 트럭 id, 트럭 위치, 트럭이 가진 자전거 수
#  { "id": 0, "location_id": 0, "loaded_bikes_count": 0 }
def getTrucks(base_url, headers, truck_count):
    res = requests.get('/'.join([base_url, 'trucks']), headers=headers)
    j = res.json()
    trucks = [Truck() for _ in range(truck_count)]

    for id, location_id, bikes_count in [(j['id'], j['location_id'], j['loaded_bikes_count']) for j in j['trucks']]:
        trucks[id].set(id, location_id, bikes_count)
    return trucks


## simulate 요청이 720번 실행되면, 서버의 상태가 finished가 되고 더이상의 simulate 요청은 실행되지 않는다.
## 같은 Simulate 하고 싶다면 Start API를 이용해 새로운 AUTH_KEY를 발급받아야 합니다.
# commands = [   { "truck_id": 0, "command": [2, 5, 4, 1, 6] }]
def simulate(base_url, headers, commands):
    res = requests.put('/'.join([base_url, 'simulate']), headers=headers, data=json.dumps({"commands": commands}))
    j = res.json()
    return (j['time'], j['failed_requests_count'], j['distance'])


# 해당 Auth key로 획득한 점수를 반환합니다.
# 점수는 높을수록 좋습니다.
# 카카오 T 바이크 서버의 상태가 finished가 아닐 때 본 API를 호출하면 response의 score는 무조건 0.0입니다.
def getScore(base_url, headers):
    res = requests.get('/'.join([base_url, 'score']), headers=headers)
    j = res.json()
    return j['score']


class Destinations:
    def __init__(self):
        self.destinations = []
        self.destinations_set = set()

    def add(self, id):
        if id not in self.destinations_set:
            self.destinations.append(id)
            self.destinations_set.add(id)

    def is_exist(self, id):
        return id in self.destinations_set

    def __len__(self):
        return len(self.destinations)


def getDestinationIds(bicycles, msize, truck_size):
    destinations = Destinations()
    ## 우선적으로 방문해야할 곳 구하기
    min_id, min_value, max_id, max_value = -1, 1e9, -1, -1
    for i, bicycle in enumerate(bicycles):

        if bicycle == 0:
            destinations.add(i)

        if min_value > bicycle:
            min_id = i
            min_value = bicycle
        if max_value < bicycle:
            max_id = i
            max_value = bicycle

    destinations.add(min_id)
    destinations.add(max_id)

    d_count = len(destinations)
    ## 랜덤 목적지
    while d_count < truck_size:
        dest = random.randint(0, msize * msize - 1)
        if not destinations.is_exist(dest):
            destinations.add(dest)
            d_count += 1

    return destinations.destinations


def get_movement_command(truck_location_id, dest_id, id_to_map):
    truck_r, truck_c = id_to_map[truck_location_id]
    dest_r, dest_c = id_to_map[dest_id]

    ret_command = [tcommand['down'] for _ in range(abs(truck_r - dest_r)) if truck_r < dest_r]
    ret_command.extend([tcommand['up'] for _ in range(abs(truck_r - dest_r)) if truck_r > dest_r])
    ret_command.extend([tcommand['right'] for _ in range(abs(truck_c - dest_c)) if truck_c < dest_c])
    ret_command.extend([tcommand['left'] for _ in range(abs(truck_c - dest_c)) if truck_c > dest_c])
    # print('truck({truck}) -> dest({dest}): {command}'.format(truck = truck_location_id, dest = dest_id, command = ret_command))
    return ret_command


#### 옮기기!!!!
def kakao(qid):
    auth_key = start(qid)
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    msize, truck_size, mean = [0, 5, 60], [0, 5, 10], [0, 2, 15]
    map = [[msize[qid] - i - 1 + j * 5 for j in range(msize[qid])] for i in range(msize[qid])]
    id_to_map = {map[i][j]: (i, j) for i in range(msize[qid]) for j in range(msize[qid])}

    for _ in range(720):
        ## 로직
        bicycles = getLocations(base_url, headers, msize[qid])
        trucks = getTrucks(base_url, headers, truck_size[qid])
        destination_ids = getDestinationIds(bicycles, msize[qid], truck_size[qid])

        simulation_comm = []
        ## 명령어 만들기
        for dest_id, truck in zip(destination_ids, trucks):
            ## 트럭 이동 명령어 만들기
            command = get_movement_command(truck.location_id, dest_id, id_to_map)

            ## 자전거 승하차 명령어 만들기
            load_count = truck.bikes_count
            if bicycles[dest_id] < mean[qid]:
                while len(command) < 10 and load_count < min(truck.bikes_count, mean[qid] - bicycles[dest_id]):
                    command.append(tcommand['bike_down'])
                    load_count += 1
            elif bicycles[dest_id] > mean[qid]:
                while len(command) < 10 and load_count < min(20 - truck.bikes_count, bicycles[dest_id] - mean[qid]):
                    command.append(tcommand['bike_up'])
                    load_count += 1

            simulation_comm.append({'truck_id': truck.id, 'command': command})

        ## simulate 하기
        time, failed_count, distance = simulate(base_url, headers, simulation_comm)
        print('time: {time} \nfailed_count: {failed_count}\ndistance: {distance}\n'.format(time=time,
                                                                                         failed_count=failed_count,
                                                                                         distance=distance))
    score = getScore(base_url, headers)
    print(score)




kakao(1)

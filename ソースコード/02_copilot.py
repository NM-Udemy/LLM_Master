from typing import List


class Room:
    """
    部屋を表すクラス
    属性
    number: 部屋番号 (int)
    capacity: 部屋の定員 (int)
    price: 部屋の料金 (float)
    is_booked: 予約済みかどうかを表すフラグ (bool)
    
    メソッド:
    book(): 予約する (Noneを返す)
    free(): 予約を取り消す (Noneを返す)
    """
    def __init__(self, number: int, capacity: int, price: float, is_booked: bool = False):
        self.number = number
        self.capacity = capacity
        self.price = price
        self.is_booked = is_booked

    def book(self) -> None:
        if not self.is_booked:
            self.is_booked = True
        else:
            print(f"Room {self.number} is already booked.")

    def free(self) -> None:
        if self.is_booked:
            self.is_booked = False
        else:
            print(f"Room {self.number} is not booked.")

class Hotel:
    """
    ホテルを表すクラス
    属性:
    name: ホテル名 (str)
    rooms: ホテルの部屋のリスト (List[Room])
    
    メソッド:
    add_room(room: Room): 部屋を追加する (Noneを返す)
    check_in(room_number: int): チェックインする (Noneを返す)
    check_out(room_number: int): チェックアウトする (Noneを返す)
    show_vacancies(): 空き部屋を表示する (Noneを返す)
    """
    def __init__(self, name: str, rooms: List[Room] = None):
        self.name = name
        self.rooms = rooms if rooms is not None else []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def check_in(self, room_number: int) -> None:
        for room in self.rooms:
            if room.number == room_number:
                if not room.is_booked:
                    room.book()
                    print(f"Room {room_number} is booked.")
                else:
                    print(f"Room {room_number} is already booked.")
                return
        print(f"Room {room_number} does not exist.")

    def check_out(self, room_number: int) -> None:
        for room in self.rooms:
            if room.number == room_number:
                if room.is_booked:
                    room.free()
                    print(f"Room {room_number} is now free.")
                else:
                    print(f"Room {room_number} is not booked.")
                return
        print(f"Room {room_number} does not exist.")

    def show_vacancies(self) -> None:
        vacant_rooms = [room.number for room in self.rooms if not room.is_booked]
        if vacant_rooms:
            print(f"Vacant rooms are: {', '.join(map(str, vacant_rooms))}.")
        else:
            print("No rooms are vacant.")


def create_hotel(name: str) -> Hotel:
    """ホテルを作成する"""
    return Hotel(name)

def add_rooms_to_hotel(hotel: Hotel, room_info: List[Tuple[int, int, int]]) -> None:
    """部屋を作成し、ホテルに追加する"""
    for number, capacity, price in room_info:
        room = Room(number, capacity, price)
        hotel.add_room(room)

def check_in(hotel: Hotel, room_number: int) -> None:
    """チェックイン（部屋を予約）する"""
    hotel.check_in(room_number)

def show_vacancies(hotel: Hotel) -> None:
    """空き部屋を表示する"""
    hotel.show_vacancies()

def check_out(hotel: Hotel, room_number: int) -> None:
    """チェックアウト（部屋の予約を解除）する"""
    hotel.check_out(room_number)

# ホテルを作成
hotel = create_hotel("Ritz")

# 部屋番号と部屋の情報のリスト
room_info = [
    (101, 3, 15000),
    (102, 2, 20000),
    (103, 1, 5000),
    (201, 2, 25000),
    (202, 2, 20000),
    (203, 1, 5000),
    (301, 3, 15000),
    (302, 2, 20000),
    (303, 1, 5000)
]

# 部屋を作成し、ホテルに追加
add_rooms_to_hotel(hotel, room_info)

# チェックイン（部屋を予約）
check_in(hotel, 101)
check_in(hotel, 202)
check_in(hotel, 303)

# 空き部屋の表示
show_vacancies(hotel)

# チェックアウト（部屋の予約を解除）
check_out(hotel, 101)

# 再度空き部屋の表示
show_vacancies(hotel)

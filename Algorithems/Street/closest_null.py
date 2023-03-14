# ID решения 83702628
def data_input():
    length_street = int(input())
    street = [int(num) for num in input().split()]
    return length_street, street


def closest_null(length_street:int,street:list ):
    distance = [length_street]*length_street
    zero_position = None
    for house in range(0, length_street):
        if street[house] == 0:
            distance[house] = 0
            zero_position = house
        if street[house] != 0 and zero_position is not None:
            distance[house] = house-zero_position
    zero_position = None
    for house in range(length_street-1, -1, -1):
        if street[house] == 0:
            zero_position = house
        if ((street[house] != 0)
            and (zero_position is not None)
            and (
                distance[house] > (zero_position - house)
                )):
            distance[house] = (zero_position - house)
    return distance


if __name__ == '__main__':
    length_street, street = data_input()
    print(*closest_null(length_street, street))

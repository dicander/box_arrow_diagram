class Node:
    def __init__(self, value, following):
        self.value = value
        self.following = following


def print_values(first):
    temp = first
    while temp:
        print(temp.value)
        temp = temp.following


def create_list(size):
    first = Node(size, None)
    for i in range(size-1, 0, -1):
        first = Node(i, first)
    return first


def destroy_element(first, index):
    """returns the first element where index has been destroyed"""
    if index == 0:
        return first.following
    answer = first #we will change this variable
    for i in range(index-1):
        first = first.following
    following_following = first.following.following
    first.following = following_following
    return answer


def main():
    first = create_list(4)
    print_values(first)
    first = destroy_element(first, 2)
    print_values(first)


if __name__ == '__main__':
    main()


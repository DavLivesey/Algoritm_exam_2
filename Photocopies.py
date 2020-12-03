

def spred_out_copies(data_center_size, count_centres):
    count_copies = 0
    if len(data_center_size) < 2:
        return 0
    data_center_size.sort(reverse=True)
    while data_center_size[0] and data_center_size[1]:
        data_center_size[0] -= 1
        data_center_size[1] -= 1
        count_copies += 1
        data_center_size.sort(reverse=True)
    return count_copies


if __name__ == '__main__':
    count_datacentres = int(input())
    data_center_size = list(map(int, input().split(' ')))
    print(spred_out_copies(data_center_size, count_datacentres))

# Код посылки 43352749
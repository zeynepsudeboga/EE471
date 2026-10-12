HATLESS = "H"
NO_GROUP_START = -1


def find_first_oriented_cap(caps):
    for cap in caps:
        if cap != HATLESS:
            return cap
    return None


def announce_flips(start, exclusive_end):
    last = exclusive_end - 1
    if start == last:
        print(f"Person in position {start} flip your cap!")
    else:
        print(f"People in positions {start} through {last} flip your caps!")


def close_group_if_open(start, exclusive_end):
    if start == NO_GROUP_START:
        return NO_GROUP_START
    announce_flips(start, exclusive_end)
    return NO_GROUP_START


def pleaseConformOnepass(caps):
    if not caps:
        return

    target_orientation = find_first_oriented_cap(caps)
    if not target_orientation:
        return

    caps = caps + [target_orientation]
    group_start = NO_GROUP_START

    for index, cap in enumerate(caps):
        if cap == HATLESS:
            group_start = close_group_if_open(group_start, index)
            continue

        if cap != target_orientation and group_start == NO_GROUP_START:
            group_start = index
        elif cap == target_orientation and group_start != NO_GROUP_START:
            group_start = close_group_if_open(group_start, index)


cap3 = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]
pleaseConformOnepass(cap3)

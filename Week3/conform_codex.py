HOUSE_CAP = "H"


def _print_flip_instruction(start_position, end_position):
    if start_position == end_position:
        print(f"Person in position {start_position} flip your cap!")
    else:
        print(
            f"People in positions {start_position} through {end_position} "
            "flip your caps!"
        )


def please_conform_one_pass(caps):
    if not caps:
        return

    first_cap_orientation = None
    for cap_orientation in caps:
        if cap_orientation != HOUSE_CAP:
            first_cap_orientation = cap_orientation
            break

    if not first_cap_orientation:
        return

    # Appending the first orientation makes the final group close like any other.
    caps_with_wraparound = caps + [first_cap_orientation]
    group_start_position = None

    for position, cap_orientation in enumerate(caps_with_wraparound):
        if cap_orientation == HOUSE_CAP:
            if group_start_position is not None:
                _print_flip_instruction(group_start_position, position - 1)
                group_start_position = None
            continue

        if cap_orientation != first_cap_orientation and group_start_position is None:
            group_start_position = position
        elif cap_orientation == first_cap_orientation and group_start_position is not None:
            _print_flip_instruction(group_start_position, position - 1)
            group_start_position = None


cap3 = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]
please_conform_one_pass(cap3)

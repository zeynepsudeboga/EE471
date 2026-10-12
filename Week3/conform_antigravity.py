"""
Module to determine cap flips required to conform orientations in a line of people.
"""

from typing import Sequence

HATLESS = "H"
NO_ACTIVE_GROUP = None


def find_reference_orientation(caps: Sequence[str]) -> str | None:
    """Finds the orientation of the first person wearing a cap."""
    for cap in caps:
        if cap != HATLESS:
            return cap
    return None


def print_flip_instruction(start_index: int, end_index: int) -> None:
    """Prints the instruction to flip caps for an individual or a contiguous range."""
    if start_index == end_index:
        print(f"Person in position {start_index} flip your cap!")
    else:
        print(f"People in positions {start_index} through {end_index} flip your caps!")


def close_active_group(group_start: int | None, current_index: int) -> int | None:
    """Announces flip instructions if an interval was active and resets interval tracking."""
    if group_start is not None:
        last_person_index = current_index - 1
        print_flip_instruction(group_start, last_person_index)
    return NO_ACTIVE_GROUP


def pleaseConformOnepass(caps: Sequence[str] | None) -> None:
    """
    Instructs people in a line to flip their caps in one pass so that everyone
    wearing a cap conforms to the same orientation.

    People without caps ('H') are skipped.
    """
    if not caps:
        return

    if not isinstance(caps, (list, tuple)):
        raise TypeError(f"Expected caps to be a list or tuple, but got {type(caps).__name__}")

    reference_orientation = find_reference_orientation(caps)
    if reference_orientation is None:
        return

    extended_caps = list(caps) + [reference_orientation]
    group_start: int | None = NO_ACTIVE_GROUP

    for current_index, cap in enumerate(extended_caps):
        if cap == HATLESS or cap == reference_orientation:
            group_start = close_active_group(group_start, current_index)
        elif group_start is None:
            group_start = current_index


cap3 = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]

if __name__ == "__main__":
    pleaseConformOnepass(cap3)
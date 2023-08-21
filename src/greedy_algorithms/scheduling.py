#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""Select the most number of events without overlapping schedules."""
from typing import NamedTuple


class Event(NamedTuple):
    name: str
    start_time: int
    end_time: int

    def __str__(self) -> str:
        return (f"Event(name={self.name},start_time={self.start_time},"
                f"end_time={self.end_time})")


def print_events(events: list[Event]) -> None:
    print("=" * 10)
    for event in events:
        print(event)
    print("=" * 10)


def select_short_events(events: list[Event]) -> list[Event]:
    events_with_duration = sorted([
        (event, event.end_time - event.start_time)
        for event in events
    ], key=lambda e: e[1])

    selected_events = []
    latest_event = None
    
    for event, _ in events_with_duration:
        if latest_event is None or latest_event.end_time <= event.start_time:
            selected_events.append(event)
            latest_event = event
    
    return selected_events


def select_start_early_events(events: list[Event]) -> list[Event]:
    early_sorted_events = sorted(events, key=lambda event: event.start_time)
    selected_events = []
    latest_event = None
    for event in early_sorted_events:
        if latest_event is None or latest_event.end_time <= event.start_time:
            selected_events.append(event)
            latest_event = event
    
    return selected_events


def select_end_early_events(events: list[Event]) -> list[Event]:
    early_sorted_events = sorted(events, key=lambda event: event.end_time)
    selected_events = []
    latest_event = None
    for event in early_sorted_events:
        if latest_event is None or latest_event.end_time <= event.start_time:
            selected_events.append(event)
            latest_event = event
    
    return selected_events


if __name__ == "__main__":
    events = [
        Event("A", 1, 3),
        Event("B", 2, 5),
        Event("C", 3, 9),
        Event("D", 6, 8)
    ]
    print("Assume that we have the following events")
    print_events(events)
    print("Select as many non overlapping events as possible from the list.")
    print("First approach: Select the shortest non overlapping events.")
    print_events(select_short_events(events))
    print("Looks good at first, but consider this case:")
    faulty_short_events = [
        Event("A", 1, 5),
        Event("B", 4, 7),
        Event("C", 6, 10)
    ]
    print_events(faulty_short_events)
    print("The selection will be:")
    print_events(select_short_events(faulty_short_events))
    print("Even though we could have selected events A and C.")
    print("Consider a different approach. Let us pick events that start as "
          "early as possible instead.")
    print_events(select_start_early_events(events))
    print("Looks good as well, but consider this schedule:")
    faulty_early_events = [
        Event("A", 1, 10),
        Event("B", 3, 4),
        Event("C", 6, 7)
    ]
    print_events(faulty_early_events)
    print("The result of the algorithm is this:")
    print_events(select_start_early_events(faulty_early_events))
    print("But events B and C could've been picked!")
    print("The actual optimal algorithm is selecting the events that end as "
          "early as possible:")
    print_events(select_end_early_events(events))
    print("Even the other two examples could produce a better result this way.")
    print("First, the counterexample for the short events solution.")
    print_events(select_end_early_events(faulty_short_events))
    print("Then, the counterexample for the start early events solution.")
    print_events(select_end_early_events(faulty_early_events))

#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""Select order of tasks depending on duration and deadline."""
from typing import NamedTuple


class Schedule(NamedTuple):
    name: str
    duration: int
    deadline: int

    def __str__(self) -> str:
        return (f"Schedule(name={self.name},duration={self.duration},"
                f"deadline={self.deadline})")


def print_schedules(schedules: list[Schedule]) -> None:
    print("=" * 10)
    for schedule in schedules:
        print(schedule)
    print("=" * 10)


def verify_solution(schedules: list[Schedule]) -> int:
    """Calculate score given a specific schedule order"""
    current_time = 0
    score = 0
    for schedule in schedules:
        current_time += schedule.duration
        score += schedule.deadline - current_time
    return score


def schedule_tasks(schedules: list[Schedule]) -> list[Schedule]:
    return sorted(schedules,
                  key=lambda schedule: (schedule.duration, schedule.deadline))


if __name__ == "__main__":
    schedules = [
        Schedule("A", 4, 2),
        Schedule("B", 3, 5),
        Schedule("C", 2, 7),
        Schedule("D", 4, 5)
    ]
    print("Consider this list of schedules with their duration and deadline:")
    print_schedules(schedules)
    print("Choose an order to perform the tasks. Each task yields d - x "
          "points, where d is the duration and x is the moment at which the "
          "task was finished.")
    print("The solution does not involve the deadlines, just the durations.")
    print("We just have to sort the schedules in ascending duration order:")
    scheduled_tasks = schedule_tasks(schedules)
    print_schedules(scheduled_tasks)
    print(f"This yields {verify_solution(scheduled_tasks)} points.")
    print("Just to be sure, let's reverse A and D's deadlines...")
    schedules = [
        Schedule("A", 4, 5),
        Schedule("B", 3, 5),
        Schedule("C", 2, 7),
        Schedule("D", 4, 2)
    ]
    print_schedules(schedules)
    scheduled_tasks = schedule_tasks(schedules)
    print_schedules(scheduled_tasks)
    print(f"This yields {verify_solution(scheduled_tasks)} points.")

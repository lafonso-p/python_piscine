import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "jump", "climb", "hide", "use", "release", "sleep",
               "eat", "move", "swim"]
    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(event_list: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        event = random.choice(event_list)
        event_list.remove(event)
        yield event


def main() -> None:
    print("=== Data Stream Processor ===")
    stream = gen_event()

    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list: list[tuple[str, str]] = []
    for i in range(10):
        event_list.append(next(stream))

    print(f"built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remaining in list: {event_list}")


if __name__ == "__main__":
    main()

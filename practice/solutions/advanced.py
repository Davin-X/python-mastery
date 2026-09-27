"""Reference answers for the 10 advanced Python prompts."""

import asyncio
from collections.abc import Awaitable, Callable, Hashable, Iterable, Iterator
from heapq import merge
from itertools import islice
from typing import TypeVar

Item = TypeVar("Item")
Result = TypeVar("Result")
HashableItem = TypeVar("HashableItem", bound=Hashable)


class PositiveInt:
    """Descriptor that stores a positive integer separately on each instance."""

    def __set_name__(self, owner: type, name: str) -> None:
        self._storage_name = f"_{name}"

    def __get__(self, instance: object | None, owner: type | None = None) -> object:
        if instance is None:
            return self
        try:
            return getattr(instance, self._storage_name)
        except AttributeError as exc:
            raise AttributeError(self._storage_name.removeprefix("_")) from exc

    def __set__(self, instance: object, value: object) -> None:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value <= 0:
            raise ValueError("value must be positive")
        setattr(instance, self._storage_name, value)


class PluginMeta(type):
    """Register plugin subclasses by unique name."""

    registry: dict[str, type] = {}

    def __new__(
        metaclass,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, object],
    ) -> type:
        plugin_class = super().__new__(metaclass, name, bases, namespace)
        plugin_class.registry = metaclass.registry
        if any(isinstance(base, metaclass) for base in bases):
            plugin_name = namespace.get("plugin_name")
            if not isinstance(plugin_name, str) or not plugin_name.strip():
                raise ValueError("plugin subclasses require a non-empty plugin_name")
            if plugin_name in metaclass.registry:
                raise ValueError(f"duplicate plugin name: {plugin_name}")
            metaclass.registry[plugin_name] = plugin_class
        return plugin_class


class Plugin(metaclass=PluginMeta):
    """Base class for registered plugins."""


async def map_limited(
    items: list[Item],
    worker: Callable[[Item], Awaitable[Result]],
    limit: int,
) -> list[Result]:
    """Run async work with bounded concurrency and preserve input order."""
    if limit < 1:
        raise ValueError("limit must be positive")
    semaphore = asyncio.Semaphore(limit)

    async def run_one(item: Item) -> Result:
        async with semaphore:
            return await worker(item)

    return list(await asyncio.gather(*(run_one(item) for item in items)))


async def retry_async(
    operation: Callable[[], Awaitable[Result]],
    attempts: int,
    delay: float = 0.0,
) -> Result:
    """Retry only timeout failures and propagate other exceptions."""
    if attempts < 1:
        raise ValueError("attempts must be at least 1")
    if delay < 0:
        raise ValueError("delay must not be negative")
    for attempt in range(attempts):
        try:
            return await operation()
        except TimeoutError:
            if attempt == attempts - 1:
                raise
            await asyncio.sleep(delay)
    raise AssertionError("unreachable")


async def run_with_timeout(
    operation: Callable[[], Awaitable[Result]],
    timeout: float,
) -> Result:
    """Run one operation with a positive timeout."""
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    return await asyncio.wait_for(operation(), timeout=timeout)


class NotificationDispatcher:
    """Dispatch notifications through registered sender strategies."""

    def __init__(self) -> None:
        self._senders: dict[str, Callable[[str], object]] = {}

    def register(self, name: str, sender: Callable[[str], object]) -> None:
        if not name:
            raise ValueError("name must not be empty")
        if name in self._senders:
            raise ValueError(f"sender already registered: {name}")
        self._senders[name] = sender

    def send(self, name: str, message: str) -> object:
        return self._senders[name](message)


class EventBus:
    """Publish events to handlers in subscription order."""

    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable[[object], None]]] = {}

    def subscribe(self, event: str, handler: Callable[[object], None]) -> None:
        handlers = self._handlers.setdefault(event, [])
        if handler not in handlers:
            handlers.append(handler)

    def unsubscribe(self, event: str, handler: Callable[[object], None]) -> None:
        handlers = self._handlers.get(event, [])
        if handler in handlers:
            handlers.remove(handler)

    def publish(self, event: str, payload: object) -> None:
        for handler in tuple(self._handlers.get(event, [])):
            handler(payload)


def chunked(items: Iterable[Item], size: int) -> Iterator[list[Item]]:
    """Yield bounded-size lists from an iterable without eager materialization."""
    if size < 1:
        raise ValueError("size must be positive")
    iterator = iter(items)
    while chunk := list(islice(iterator, size)):
        yield chunk


def unique_in_order(items: Iterable[HashableItem]) -> Iterator[HashableItem]:
    """Yield each hashable value once, in first-seen order."""
    seen: set[HashableItem] = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item


def merge_sorted(*iterables: Iterable[int]) -> Iterator[int]:
    """Lazily merge sorted integer iterables."""
    return merge(*iterables)


async def _check_async() -> None:
    async def double_async(value: int) -> int:
        await asyncio.sleep(0)
        return value * 2

    assert await map_limited([1, 2, 3], double_async, limit=2) == [2, 4, 6]

    attempts = 0

    async def flaky_operation() -> str:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise TimeoutError
        return "ok"

    assert await retry_async(flaky_operation, attempts=2) == "ok"

    async def fast_operation() -> str:
        return "done"

    assert await run_with_timeout(fast_operation, timeout=1.0) == "done"


def _check() -> None:
    class Product:
        stock = PositiveInt()

    first = Product()
    second = Product()
    first.stock = 3
    second.stock = 4
    assert first.stock == 3
    assert second.stock == 4

    class CsvPlugin(Plugin):
        plugin_name = "csv"

    assert Plugin.registry["csv"] is CsvPlugin
    try:

        class DuplicatePlugin(Plugin):
            plugin_name = "csv"

    except ValueError:
        pass
    else:
        raise AssertionError("duplicate plugin names must fail")

    dispatcher = NotificationDispatcher()
    dispatcher.register("email", lambda message: f"sent: {message}")
    assert dispatcher.send("email", "hello") == "sent: hello"

    bus = EventBus()
    received: list[object] = []

    def record_event(payload: object) -> None:
        received.append(payload)
        bus.unsubscribe("saved", record_event)

    bus.subscribe("saved", record_event)
    bus.publish("saved", {"id": 1})
    bus.publish("saved", {"id": 2})
    assert received == [{"id": 1}]
    assert list(chunked(range(5), 2)) == [[0, 1], [2, 3], [4]]
    assert list(unique_in_order("banana")) == ["b", "a", "n"]
    assert list(merge_sorted([1, 4], [2, 3], [])) == [1, 2, 3, 4]
    asyncio.run(_check_async())


if __name__ == "__main__":
    _check()
    print("OK")

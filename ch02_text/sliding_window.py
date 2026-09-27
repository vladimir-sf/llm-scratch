"""Ch2 — write this. Copy tiktoken + DataLoader from the book around it."""


def sliding_window(token_ids: list[int], context_length: int, stride: int) -> list[tuple[list[int], list[int]]]:
    """Return (input, target) pairs where target is input shifted by 1."""
    pairs = []
    # TODO: loop start = 0, stride, stride, ...
    # window of length context_length + 1 so y has the next token
    raise NotImplementedError

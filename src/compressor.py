import gzip
import bz2

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Compressor:
    __compressors = {
        "gzip": gzip.compress,
        "bzip2": bz2.compress,
        "none": lambda x: x,
    }

    def __init__(self, name, encoding, function, **extra_arguments):
        self.name = name
        self.encoding = encoding
        self.function = function
        self.extra_arguments = extra_arguments

    @classmethod
    def new(cls, name, encoding="utf-8", **compress_extra_arguments):
        return cls(name, encoding, cls.__compressors[name], **compress_extra_arguments)

    def compress(self, text: str) -> bytes:
        return self.function(text.encode(self.encoding), **self.extra_arguments)

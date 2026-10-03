#!/usr/bin/env python3
# Copyright © Advanced Micro Devices, Inc., or its affiliates.
# SPDX-License-Identifier:  MIT

"""Unit tests for rock_dev_bootstrap.gpu_short, which names the default build dir.

A concrete target keeps its whole name so ``gfx1250`` and ``gfx1250-strict`` get distinct
build dirs; a TheRock family or generic name is cut at its first hyphen so existing
default build dirs keep their names.
"""

import unittest

from rock_dev_bootstrap import gpu_short


class TestGpuShort(unittest.TestCase):
    def test_concrete_targets_are_kept_whole(self):
        for target in ("gfx942", "gfx90a", "gfx1250", "gfx1250-strict"):
            with self.subTest(target=target):
                self.assertEqual(gpu_short(target), target)

    def test_family_and_generic_names_are_cut_at_first_hyphen(self):
        for name, short in (
            ("gfx94X-dcgpu", "gfx94X"),
            ("gfx125X-dcgpu", "gfx125X"),
            ("gfx950-dcgpu", "gfx950"),
            ("gfx90a-dcgpu", "gfx90a"),
            ("gfx906-dgpu", "gfx906"),
            ("gfx90c-igpu", "gfx90c"),
            ("gfx950-all", "gfx950"),
            ("gfx11-generic", "gfx11"),
            ("gfx9-4-generic", "gfx9"),
        ):
            with self.subTest(name=name):
                self.assertEqual(gpu_short(name), short)


if __name__ == "__main__":
    unittest.main()

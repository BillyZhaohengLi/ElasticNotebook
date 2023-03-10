#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021-2022 University of Illinois

from typing import List
from elastic.core.graph.variable_snapshot import VariableSnapshot

from enum import Enum


class OptimizerType(Enum):
    """
        String representations of all implemented optimizers.
    """
    EXACT = "exact"
    EXACT_C = "exact_c"
    EXACT_R = "exact_r"
    GREEDY = "greedy"
    RANDOM = "random"
    MIGRATE_ALL = "migrate_all"
    RECOMPUTE_ALL = "recompute_all"
    HEURISTIC = "heuristic"
    GREEDY_SIMPLE = "greedy_simple"


class Selector:
    """
        The `Selector` class provides interfaces to pick a subset of active VSs to migrate based on
            various heuristics and algorithms.
    """

    def __init__(self, migration_speed_bps=1):
        """
            Creates a Selector instance with a migration speed estimate. The dependency graph and active VS fields
            must be populated prior to calling select_vss.
        """
        self.dependency_graph = None
        self.active_vss = None
        self.overlapping_vss = None
        self.migration_speed_bps = migration_speed_bps

    def select_vss(self) -> set:
        """
            Classes that inherit from the `Selector` class (such as `Optimizer` and various baselines)
                should override `select_vss`.

            Returns:
                set(VariableSnapshot): a subset of active VSs selected to migrate based on various heuristics and
                algorithms.
        """
        raise NotImplementedError()

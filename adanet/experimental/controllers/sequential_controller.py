# Copyright 2019 The AdaNet Authors. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A manual controller for model search."""

from __future__ import absolute_import
from __future__ import division
from __future__ import google_type_annotations
from __future__ import print_function

from adanet.experimental.controllers.controller import Controller
from adanet.experimental.phases.phase import Phase
from adanet.experimental.storages.in_memory_storage import InMemoryStorage
from adanet.experimental.storages.storage import Storage
from adanet.experimental.work_units.work_unit import WorkUnit
import tensorflow as tf
from typing import Iterator, Sequence


class SequentialController(Controller):
  """A controller where the user specifies the sequences of phase to execute."""

  def __init__(self, phases: Sequence[Phase],
               storage: Storage = InMemoryStorage()):
    self._phases = phases
    self._storage = storage

  def work_units(self) -> Iterator[WorkUnit]:
    prev_phase = None
    for phase in self._phases:
      phase.build(self._storage, previous=prev_phase)
      for work_unit in phase.work_units():
        yield work_unit
      prev_phase = phase

  def get_best_models(self, num_models) -> Sequence[tf.keras.Model]:
    return self._storage.get_best_models(num_models)

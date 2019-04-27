from collections import abc

# Adapted from https://github.com/kennethreitz/requests/blob/v1.2.3/requests/structures.py#L37

# Original Author's License:
# Copyright 2018 Kenneth Reitz
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        https://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

class CaseInsensitiveDict(abc.MutableMapping):
    def __init__(self, data={}, **kwargs):
        self._store = dict()
        self.update(data, **kwargs)

    def __setitem__(self, key, value):
        self._store[key.lower()] = (key, value)

    def __getitem__(self, key):
        return self._store[key.lower()][1]

    def __contains__(self, key):
        return key.lower() in self._store

    def __delitem__(self, key):
        del self._store[key.lower()]

    def __iter__(self):
        return (casedkey for casedkey, mappedvalue in self._store.values())

    def __len__(self):
        return len(self._store)

    def get_pair(self, key):
        """ returns (key, value) with correct case key """
        return self._store[key.lower()]

    def keys(self):
        return self._store.keys()
    
    def items(self):
        return self._store.values()

    def values(self):
        return [v[1] for v in self._store.values()]

    def copy(self):
        return CaseInsensitiveDict(self._store.values())

    def __repr__(self):
        return f'{self.__class__.__name__}({dict(self.items())})'

    # __eq__ not implemented for now


#
# Copyright 2026 Capital One Services, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Comparator classes."""

from datacompy.comparator.array import (
    PandasArrayLikeComparator,
    PolarsArrayLikeComparator,
    SnowflakeArrayLikeComparator,
    SparkArrayLikeComparator,
)
from datacompy.comparator.boolean import (
    PandasBooleanComparator,
    PolarsBooleanComparator,
    SnowflakeBooleanComparator,
    SparkBooleanComparator,
)
from datacompy.comparator.numeric import (
    PandasNumericComparator,
    PolarsNumericComparator as _PolarsNumericComparator,
    SnowflakeNumericComparator as _SnowflakeNumericComparator,
    SparkNumericComparator as _SparkNumericComparator,
)
from datacompy.comparator.string import (
    PandasStringComparator,
    PolarsStringComparator,
    SnowflakeStringComparator,
    SparkStringComparator,
)


class PolarsNumericComparator(_PolarsNumericComparator):
    """Polars numeric comparator with Boolean dispatch parity."""

    def compare(self, col1, col2, rtol=1e-5, atol=1e-8):
        boolean_result = PolarsBooleanComparator().compare(col1, col2)
        if boolean_result is not None:
            return boolean_result
        return super().compare(col1, col2, rtol=rtol, atol=atol)


class SparkNumericComparator(_SparkNumericComparator):
    """Spark numeric comparator with Boolean dispatch parity."""

    def compare(self, dataframe, col1, col2, rtol=1e-5, atol=1e-8):
        boolean_result = SparkBooleanComparator().compare(dataframe, col1, col2)
        if boolean_result is not None:
            return boolean_result
        return super().compare(dataframe, col1, col2, rtol=rtol, atol=atol)


class SnowflakeNumericComparator(_SnowflakeNumericComparator):
    """Snowflake numeric comparator with Boolean dispatch parity."""

    def compare(self, dataframe, col1, col2, col_match, rtol=1e-5, atol=1e-8):
        boolean_result = SnowflakeBooleanComparator().compare(
            dataframe, col1, col2, col_match
        )
        if boolean_result is not None:
            return boolean_result
        return super().compare(
            dataframe, col1, col2, col_match, rtol=rtol, atol=atol
        )


__all__ = [
    "PandasArrayLikeComparator",
    "PandasBooleanComparator",
    "PandasNumericComparator",
    "PandasStringComparator",
    "PolarsArrayLikeComparator",
    "PolarsBooleanComparator",
    "PolarsNumericComparator",
    "PolarsStringComparator",
    "SnowflakeArrayLikeComparator",
    "SnowflakeBooleanComparator",
    "SnowflakeNumericComparator",
    "SnowflakeStringComparator",
    "SparkArrayLikeComparator",
    "SparkBooleanComparator",
    "SparkNumericComparator",
    "SparkStringComparator",
]

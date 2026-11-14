# ruff check --fix has not been run here till now becuase it just removes a lot of
# lines which show some of the examples of the pep8 rules.
# you can run it and check how it works.

# !. IMPORTS: Top of the file, Grouped ( Stdlib -> 3rd Party -> Local), alphabetical
import os
import sys

import requests

from billing_app import models  # Explicit absolute import
from . import utils  # Exlicit relative import(using dot notation)

# 2. NAMING: ALL_CAPS for module-level constants
MAX_RETRIES = 3
DEFAULT_CURRENCY = "USD"


# 3. NAMING: CapitalizedWords for classes and exceptions
class PaymentProcessorError(Exception):
    pass


class PaymentProcessor:
    # 4. NAMING: 'self' for instance methods, lowercase_underscore for args/vars
    def __init__(self, api_key: str, pending_items: list) -> None:
        self.api_key = api_key  # Public attribute
        self._retry_count = 0  # _leading_underscore:Protected (internal use)
        self.__secret_token = (
            "xyz_987"  # __double_leading: Private (name-mangled)
        )
        self.pending_items = pending_items

    # 5. NAMING: 'cls' as first parameter for @classmethod
    @classmethod
    def from_env(cls, pending_items: list):
        return cls(os.getenv("API_KEY", ""), pending_items)

    # 6. NAMING: lowercase_underscore for methods and functions
    def process_batch(self, discount=None):
        # 7. EXPRESSIONS: Implicit falsiness for empty sequences (no len(x) == 0)
        if not self.pending_items:
            return 0.0

        # 8. EXPRESSIONS: Inline negation ('is not') & implicit truthiness ('if self.pending_items')
        if discount is not None and self.pending_items:
            # 9. EXPRESSIONS: Parantheses for multiline expressions (no backslashes \)
            # Plus 4 extra spaces on continuation lines!
            total_amount = (
                sum(item.price for item in self.pending_items)
                - discount.amount
                + discount.tax_adjustment
            )
        else:
            total_amount = sum(item.price for item in self.pending_items)

        # 10. EXPRESSIONS: Multi-line loops and try/except (never single-line)
        for item in self.pending_items:
            try:
                utils.charge_card(self.__secret_token, item, total_amount)
            except requests.RequestException as exc:
                self._retry_count += 1
                raise PaymentProcessorError("Charge failed") from exc

        return total_amount

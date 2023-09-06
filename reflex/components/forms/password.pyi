"""Stub file for password.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional
from reflex.components.component import Component
from reflex.components.forms.input import Input
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Password(Input):
    @overload
    @classmethod
    def create(cls, *children, type_: Optional[Union[Var[str], str]] = None, **props) -> "Password": ...  # type: ignore
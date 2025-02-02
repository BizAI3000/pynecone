"""Stub file for plotly.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Dict, Union, overload, Optional
from reflex.components.component import NoSSRComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class PlotlyLib(NoSSRComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "PlotlyLib": ...  # type: ignore

class Plotly(PlotlyLib):
    @overload
    @classmethod
    def create(cls, *children, data: Optional[Union[Var[Figure], Figure]] = None, layout: Optional[Union[Var[Dict], Dict]] = None, width: Optional[Union[Var[str], str]] = None, height: Optional[Union[Var[str], str]] = None, use_resize_handler: Optional[Union[Var[bool], bool]] = None, **props) -> "Plotly": ...  # type: ignore

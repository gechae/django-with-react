# from django.views.generic.base import RedirectView, TemplateView, View
from . import TemplateView, beas1
from .beas1 import BaseTemplate1, BaseTemplate2
# from django.views.generic.dates import (
#     ArchiveIndexView,
#     DateDetailView,
#     DayArchiveView,
#     MonthArchiveView,
#     TodayArchiveView,
#     WeekArchiveView,
#     YearArchiveView,
# )
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
# from django.views.generic.list import ListView

__all__ = [
    "TemplateView",
    "beas1",
    'BaseTemplate1'
]


class GenericViewError(Exception):
    """A problem in a generic view."""

    pass

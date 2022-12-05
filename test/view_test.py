
import unittest

from django.views.generic import DetailView

from test.TemplateView import TemplateView


# class TestView(unittest.TestCase):
#
#     def test_detail_View(self):
#         print(DetailView.mro)
#         view = DetailView.as_view(model='test')
#
#         view()

if __name__ == '__main__':

    TemplateView.setString()
    pass

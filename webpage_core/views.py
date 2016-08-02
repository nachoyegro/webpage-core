from django.shortcuts import render
from django.views.generic import View
from webpage_core.models import Page, Content, SimpleText
from django.shortcuts import get_object_or_404

# Create your views here.
class PageView(View):
    def get(self, request, url_name, extras = {}):
        page = get_object_or_404(Page, url_name=url_name)
        contents = [content.get_html() for content in Content.objects.filter(pages=page).order_by('position').select_subclasses()]
        extras['contents'] = contents
        extras['title'] = page.title
        extras['background'] = page.background
        return render(request, page.html_name, extras)
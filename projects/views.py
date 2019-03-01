from django.shortcuts import render
from projects.models import ProjectPage
from pathlib import Path

def projectindex(request):
    project_objs = ProjectPage.objects.all()
    context_dict = {"project_objs": project_objs}
    return render(request, 'projects/projectindex.html', context_dict)

def projectpage(request, name):
    context_dict = {}
    query_objs = ProjectPage.objects.filter(name=name)
    if len(query_objs) > 0:
        page_obj = query_objs[0]
        context_dict = {"project_obj": page_obj}
    html_dir = 'projects/' + page_obj.name + '.html'
    print(html_dir)
    if not Path("templates/" + html_dir).is_file():
        html_dir = 'projects/pagenotfound.html'
    return render(request, html_dir, context_dict)

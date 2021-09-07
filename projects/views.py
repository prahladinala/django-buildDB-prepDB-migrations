from django.shortcuts import render

from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]
def projects(request):
    # return HttpResponse('Here are our projects')
    # return render(request, 'projects.html')
    # PASSING VARIABLES
    # msg = 'Hello, you are on the projects page'
    # return render(request, 'projects/projects.html', {'message': msg})
    page = 'projects'
    number = 10
    context = {'page':page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)

    # return render(request, 'projects/projects.html', {'anyname_here_to_call_in_html': msg})

def project(request, pk):
    # return HttpResponse('Single Project' + ' ' + str(pk))
    # return render(request, 'single-project.html')
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})

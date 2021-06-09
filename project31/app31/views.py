from django.shortcuts import render

from django.http import HttpResponse

def showIndex(http_request):
    message = '''
             <html>
                  <body bgcolor ="red">
                      <h1> welcome to django </h1>
                  </body>
             </html>'''
    return HttpResponse(message)
from django.http import HttpResponse
from django.views import generic
import io
import matplotlib.pyplot as plt
import logging
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
import os
from . import eda
from  monitor import views

UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'  # アップロードしたファイルを保存するディレクトリ

logger = logging.getLogger('development')


#class IndexView(LoginRequiredMixin, generic.ListView):
class IndexView(generic.ListView):
    model=None
    paginate_by = 5
    ordering = ['-updated_at']
    template_name = 'monitor/index.html'

def index(request):
    return render(request, 'monitor/index.html')


def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s



def simple(request):
    import django
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    import matplotlib.pyplot as plt
    # prepare for data
    fig=eda.getFig()

    canvas=FigureCanvas(fig)
 #   response=django.http.HttpResponse(content_type='image/png')
 #   canvas.print_png(response)
    svg = pltToSvg() # convert plot to SVG
    plt.cla()        # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response
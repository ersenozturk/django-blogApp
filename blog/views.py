from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
# from .forms import StudentForm

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request, "users/post_list.html")

class HomeView(TemplateView):
    template_name = "blog/home.html"
    


# class StudentListView(ListView):
#     model = Student
#     context_object_name = 'students'



# class StudentCreateView(CreateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'blog/student_add.html'
#     success_url = reverse_lazy('list')
    
#     def form_valid(self, form):
#         self.object = form.save()
#         if not self.object.number:
#             self.object.number = 9999
#         self.object.save()
#         return super().form_valid(form) 

# class StudentDetailView(DetailView):
#     model = Student
#     pk_url_kwarg = 'id'




# class StudentUpdateView(UpdateView):
#     model = Student
#     form_class = StudentForm
#     template_name = "blog/student_update.html"
#     success_url = reverse_lazy('list')
#     # pk_url_kwarg = 'id'



# class StudentDeleteView(DeleteView):
#     model = Student
#     template_name = "blog/student_delete.html"
#     success_url = reverse_lazy('list')
#     # pk_url_kwarg = 'id'
from django.shortcuts import render, redirect
from django.contrib import messages
from protektalk_app.models import Incident_report
from django import forms

class IncidentReportForm(forms.Form):
    incident_report_number = forms.CharField(max_length=100, required=True)

def index(request):
    form = IncidentReportForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        incident_number = form.cleaned_data['incident_report_number']
        try:
            report = Incident_report.objects.get(incident_report_number=incident_number)
            return render(request, 'parents_dashboard/incident.html', {
                'report': report,
                'form': form
            })
        except Incident_report.DoesNotExist:
            messages.error(request, 'Incident report not found.')
            return redirect('parent_dashboard:dashboard')
    return render(request, 'parents_dashboard/incident.html', {'form': form})

def dashboard(request):
    return render(request, 'parents_dashboard/dashboard.html')

def contact(request):
    return render(request, 'parents_dashboard/contact.html')
from django.shortcuts import render
from reports.models import *
from django.core.paginator import Paginator
from django.db.models import Q, Sum
import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages



def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(Q(student_name__icontains = search) | 
                                    Q(student_id__icontains = search)| 
                                   Q(student_age__icontains = search)| 
                                   Q(student_email__icontains = search)| 
                                   Q(department__department__icontains = search))


    paginator = Paginator(queryset, 25)  
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "students.html", {'queryset': page_obj})


    
def generate_and_send_otp(request, student_id):
    student = Student.objects.get(student_id__student_id=student_id)
    generated_otp = random.randint(100000, 999999)
    request.session['generated_otp'] = generated_otp
    request.session['student_id'] = student_id

    context = {'student': student, 'otp': generated_otp} 
    html_content = render_to_string('otp_email.html', context)

    try:
        send_mail(
            'OTP Verification',
            html_content,
            settings.EMAIL_HOST_USER,
            ['hapor23129@ebuthor.com'],
            fail_silently=False
        )
    except Exception as e:
        raise ValueError("Failed to send OTP email: {}".format(e))
    
    return redirect('verify_otp')



def verify_otp(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(student_id__student_id=student_id)

    if request.method == 'POST':
        submitted_otp = str(request.POST.get('otp'))
        generated_otp = str(request.session.get('generated_otp'))

        if submitted_otp == generated_otp: 
            messages.success(request, 'OTP verification successful!')
            return redirect('see_marks', student_id=student_id)
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'verification_popup.html', {'student': student})


def resend_otp(request):
    if request.method == 'POST' and 'resend_otp' in request.POST:
        student_id = request.session.get('student_id') 
        # Logic to generate and send new OTP
        generate_and_send_otp(request, student_id)
        messages.success(request, 'New OTP sent to your email.')
    else:
        messages.error(request, 'Invalid request.')
    
    return redirect('verify_otp')



def see_marks(request, student_id):

    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks=Sum('marks'))

    return render(request, 'gradesheet.html', {'queryset': queryset, 'total_marks': total_marks, 'marks_list': [marks.marks for marks in queryset]})



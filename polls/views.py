from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import Http404

from .models import Blog, Comment, Feedback
from .forms import FeedbackForm, CommentForm

def handleFeedback(request):
    # create a variable to keep track of the form
    messageSent = False

    if request.method == 'POST':

        form = FeedbackForm(request.POST)
        
         # check if data from the form is clean
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            fromEmail = data['fromEmail']
            message = data['message']
            subject = data['subject']

            fb = Feedback(id=Feedback.objects.count() + 1, name=name, email=fromEmail, subject=subject, message=message)
            fb.save()

            # send the email to the recipent
            send_mail('Feedback', 'Cảm ơn bạn đã gửi phản hồi cho chúng tôi!', 'anonymoustpt11@gmail.com', [fromEmail])

            # set the variable initially created to True
            messageSent = True
    else:
        form = FeedbackForm()

    return render(request, 'contact.html', {
        'form': form,
        'messageSent': messageSent,
    })


def BlogDetailView(request, _id):
    try:
        data = Blog.objects.get(id=_id)
        comments = Comment.objects.filter(blog=data)
    except Blog.DoesNotExist:
        raise Http404('Data does not exist')
     
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                name=request.user.username,
                commentText=form.cleaned_data['commentText'],
                blog=data)
            comment.save()
            return redirect(f'/menu/{_id}')
    else:
        form = CommentForm()
 
    context = {
            'data': data,
            'form': form,
            'comments': comments,
        }
    return render(request, 'detailview.html', context)

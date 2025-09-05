from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from .models import *  # Prefer explicit import over *

def index(request):
    social_links = SocialLinks.objects.all()
    profile = Profile.objects.all()
    about_data = AboutData.objects.all()
    port_stats = PortfolioStats.objects.all()
    skills = PortfolioSkills.objects.all()
    resume_des = PortfolioResumeDes.objects.first()
    resume_edu = ResumeEducation.objects.all()
    resume_exp = ResumeExperience.objects.all()
    resume_exp_des = ResumeExperienceDescription.objects.all()
    port_service_des = PortfolioServiceDescription.objects.all()
    port_services = PortfolioServices.objects.all()
    port_testimonials = PortfolioTestimonials.objects.all()
    port_port_des = PortfolioPortfolioDes.objects.first()
    port_port_filter = PortfolioFilter.objects.all()
    port_item = PortfolioItem.objects.all()
    contact_des = ContactDescription.objects.first()
    location = ContactInfoLocation.objects.first()
    if request.method == "POST":
        conName = request.POST.get("con_name")
        conEmail = request.POST.get("con_email")
        conSubj = request.POST.get("con_sub")
        conMsg = request.POST.get("con_msg")
        ContactDataByUser.objects.create(con_name=conName, con_email=conEmail, con_sub=conSubj, con_msg=conMsg)

        # HTML Email to User
        html_content = f"""
        <html>
          <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 8px; padding: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
              <h2 style="color: #333;">Hi {conName},</h2>
              <p style="font-size: 16px; color: #555;">
                Thank you for contacting <strong>Abdullah's Portfolio</strong>! 🌟<br>
                We’ve received your message and will get back to you shortly.
              </p>
              <hr style="margin: 20px 0;">
              <p style="font-size: 14px; color: #999;">In the meantime, feel free to explore more of my work:</p>
              <a href="https://virus997.pythonanywhere.com" style="display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px;">
                Visit Portfolio
              </a>
              <p style="margin-top: 30px; font-size: 12px; color: #bbb;">Sent with ❤️ from Abdullah</p>
            </div>
          </body>
        </html>
        """

        email = EmailMessage(
            subject='Thanks for contacting Abdullah!',
            body='This is a plain text fallback message.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[conEmail],
        )
        email.content_subtype = 'html'
        email.body = html_content
        email.send(fail_silently=False)

        # Email to Admin
        send_mail(
            subject='New Contact Form Submission',
            message=f'Name: {conName}\nEmail: {conEmail}\nSubject: {conSubj}\nMessage: {conMsg}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['abdullahmehboob2255@gmail.com'],  # 👈 Replace with your real email
            fail_silently=False
        )
        

    context = {
        'social_links': social_links,
        'profile' : profile,
        'about_data': about_data,
        'port_stats': port_stats,
        'skills': skills,
        'resume_des': resume_des,
        'resume_edu': resume_edu,
        'resume_exp': resume_exp,
        'resume_exp_des': resume_exp_des,
        'port_service_des': port_service_des,
        'port_services': port_services,
        'port_testimonials': port_testimonials,
        'port_port_des': port_port_des,
        'port_port_filter': port_port_filter,
        'port_item': port_item,
        'contact_des': contact_des,
        'location': location

    }
    return render(request, 'pages/index.html', context)


def service_detail_page(request, service_slug_url):
    social_links = SocialLinks.objects.all()
    profile = Profile.objects.all()
    service = get_object_or_404(PortfolioServices, service_slug=service_slug_url)
    port_services = PortfolioServices.objects.all()
    port_ser_detail_des = PortfolioServicesDetailDescrition.objects.filter(service_name = service)
    context = {
        'social_links': social_links,
        'profile': profile,
        'service': service,
        'port_services': port_services,
        'port_ser_detail_des': port_ser_detail_des
    }
    return render(request, 'pages/service-details.html', context)


def portfolio_detail_page(request, portfolio_slug_url):
    social_links = SocialLinks.objects.all()
    profile = Profile.objects.all()
    portfolio_slug = PortfolioItem.objects.get(port_item_slug=portfolio_slug_url)
    port_item = PortfolioItem.objects.all()
    port_item_image = PortfolioItemDetailImages.objects.filter(port_item=portfolio_slug)
    context = {
        'social_links': social_links,
        'profile': profile,
        'portfolio_slug': portfolio_slug,
        'port_item': port_item,
        'port_item_image': port_item_image
    }
    return render(request, 'pages/portfolio-details.html', context)


def contact_thanks(request):
    return render(request, 'pages/contact_thanks.html')
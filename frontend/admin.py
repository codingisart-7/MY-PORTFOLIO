from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['profile_name' , 'profile_img_header']

    def has_add_permission(self, request):
        return not Profile.objects.exists()


@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ['platform_name', 'icon', 'url']


@admin.register(AboutData)
class AboutDataAdmin(admin.ModelAdmin):
    list_display = ['about_heading', 'about_age', 'about_degree', 'about_city', 'about_website']
    def has_add_permission(self, request):
        return not AboutData.objects.exists()
    

@admin.register(PortfolioStats)
class PortfolioStatsAdmin(admin.ModelAdmin):
    list_display = ['stats_text', 'stats_number', 'stats_icon']


@admin.register(PortfolioSkills)
class PortfolioSkillsAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'skill_expertise']

@admin.register(PortfolioResumeDes)
class PortfolioResumeDesAdmin(admin.ModelAdmin):
    list_display = ['resume_des']
    def has_add_permission(self, request):
        return not PortfolioResumeDes.objects.exists()
    

@admin.register(ResumeEducation)
class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ['edu_degree', 'edu_start_year', 'edu_end_year', 'edu_institute']


@admin.register(ResumeExperience)
class ResumeExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'job_start_year', 'job_end_year', 'job_company']

@admin.register(ResumeExperienceDescription)
class ResumeExperienceDescriptionAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'job_description']


@admin.register(PortfolioServiceDescription)
class PortfolioServiceDescriptionAdmin(admin.ModelAdmin):
    list_display = ['service_des']
    def has_add_permission(self, request):
        return not PortfolioServiceDescription.objects.exists()

@admin.register(PortfolioServices)
class PortfolioServicesAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_icon', 'service_slug']

@admin.register(PortfolioServicesDetailDescrition)
class PortfolioServicesDetailDescritionAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_description']

@admin.register(PortfolioTestimonials)
class PortfolioTestimonialsAdmin(admin.ModelAdmin):
    list_display = ['testimonial_name', 'testimonial_img']


@admin.register(PortfolioPortfolioDes)
class PortfolioPortfolioDesAdmin(admin.ModelAdmin):
    list_display = ['portfolio_des']
    def has_add_permission(self, request):
        return not PortfolioPortfolioDes.objects.exists()
    
@admin.register(PortfolioFilter)
class PortfolioFilterAdmin(admin.ModelAdmin):
    list_display = ['filter_name', 'filter_display_text']


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['port_item_category', 'port_item_title','port_item_created_date' ,'port_item_slug']

@admin.register(PortfolioItemDetailImages)
class PortfolioItemDetailImagesAdmin(admin.ModelAdmin):
    list_display = ['port_item', 'port_item_detail_image']


@admin.register(ContactDescription)
class ContactDescriptionAdmin(admin.ModelAdmin):
    list_display = ['contact_des']
    def has_add_permission(self, request):
        return not ContactDescription.objects.exists()

@admin.register(ContactInfoLocation)
class ContactInfoLocationAdmin(admin.ModelAdmin):
    list_display = ['location_embed_map']

@admin.register(ContactDataByUser)
class ContactDataByUserAdmin(admin.ModelAdmin):
    list_display = ['con_name', 'con_email', 'con_sub']
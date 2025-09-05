from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify
# Create your models here.

class Profile(models.Model):
    profile_name = models.CharField(max_length=50)
    profile_img_header = models.ImageField(upload_to='profile_image')
    profile_skills = models.TextField(help_text="Comma-separated values, e.g. Full Stack Web Developer, Python, Django")

    class Meta:
        verbose_name = "01 - Site Profile"
        verbose_name_plural = "01 - Site Profile"

    def __str__(self):
        return f"{self.profile_name}"



class SocialLinks(models.Model):
    platform_name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='social_icons/')
    url = models.URLField()

    class Meta:
        verbose_name = "02 - Social Media Links Header"
        verbose_name_plural = "02 - Social Media Links Header"

    def __str__(self):
        return f"{self.platform_name}"
    


class AboutData(models.Model):
    about_image = models.ImageField(upload_to='profile_image')
    about_heading = models.CharField(max_length=100, default="Full Stack Web Developer")
    about_intro = models.TextField()
    about_short_text = models.TextField(help_text="Italic line under heading")
    about_birthday = models.DateField()
    about_website = models.URLField()
    about_phone = models.CharField(max_length=20)
    about_city = models.CharField(max_length=100)
    about_age = models.IntegerField()
    about_degree = models.CharField(max_length=50)
    about_email = models.EmailField()
    about_freelance = models.CharField(max_length=50)
    about_detail = models.TextField(help_text="Bottom paragraph in About section")


    def __str__(self):
        return self.about_intro

    class Meta:
        verbose_name = "03 - About Section"
        verbose_name_plural = "03 - About Section"



class PortfolioStats(models.Model):
    stats_number = models.IntegerField()
    stats_text = models.CharField(max_length=100)
    stats_icon = models.ImageField(upload_to='stats_icons/')
    show_plus = models.BooleanField(default=False, help_text="Check to show + after the number")

    class Meta:
        verbose_name = "04 - Stats Section"
        verbose_name_plural = "04 - Stats Section"

    def __str__(self):
        return f"{self.stats_number}"
    

class PortfolioSkills(models.Model):
    skill_name = models.CharField(max_length=100, help_text='For example: HTML, CSS, JS, WordPress etc')
    skill_expertise = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], help_text='Expertise Percentage (value between 1 - 100)')

    class Meta:
        verbose_name = "05 - Skills Section"
        verbose_name_plural = "05 - Skills Section"

    def __str__(self):
        return f"{self.skill_name}"
    

class PortfolioResumeDes(models.Model):
    resume_des = models.TextField(help_text='Resume Description Under Resume Heading')

    class Meta:
        verbose_name = "06 - Resume Description"
        verbose_name_plural = "06 - Resume Description"

    def __str__(self):
        return f"{self.resume_des}"
    

class ResumeEducation(models.Model):
    edu_degree = models.CharField(max_length=200)
    edu_start_year = models.IntegerField()
    edu_end_year = models.IntegerField()
    edu_institute = models.CharField(max_length=200)
    edu_description = models.TextField()

    class Meta:
        verbose_name = "07 - Resume - Education"
    
    def __str__(self):
        return self.edu_degree
    

class ResumeExperience(models.Model):
    job_title = models.CharField(max_length=200)
    job_start_year = models.CharField(max_length=10)
    job_end_year = models.CharField(max_length=10)
    job_company = models.CharField(max_length=200)

    class Meta:
        verbose_name = "08-1 - Resume - Experience"
        verbose_name_plural = "08-1 - Resume - Experience"

    def __str__(self):
        return self.job_title
    

class ResumeExperienceDescription(models.Model):
    job_title = models.ForeignKey(ResumeExperience, on_delete=models.CASCADE)
    job_description = models.TextField(help_text='Resume Description add as many as needed')

    class Meta:
        verbose_name = "08-2 - Resume - Experience Description"
        verbose_name_plural = "08-2 - Resume - Experience Description"

    def __str__(self):
        return f"{self.job_title}"
    

class PortfolioServiceDescription(models.Model):
    service_des = models.TextField(help_text='Services Description Under Services Heading')

    class Meta:
        verbose_name = "09 - Services Description"
        verbose_name_plural = "09 - Services Description"

    def __str__(self):
        return f"{self.service_des}"

class PortfolioServices(models.Model):
    service_name = models.CharField(max_length=100, unique=True)
    service_icon = models.ImageField(upload_to='service_icons/')
    service_short_detail = models.TextField(help_text="Short paragraph for service card")
    Service_long_detail = models.TextField(help_text='long para graph for service detail page')
    service_image = models.ImageField(upload_to='service_images/',  help_text='image for detail Page')
    service_extra_detailed = models.TextField(help_text='Extra detailed description for service detail page under descriotion')
    service_slug = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "10-1 - Services Section"
        verbose_name_plural = "10-1 - Services Section"

    def __str__(self):
        return f"{self.service_name}"
    
    def save(self, *args, **kwargs):
        if not self.service_slug:
            self.service_slug =  slugify(self.service_name)
        return super().save(*args, **kwargs)
    

class PortfolioServicesDetailDescrition(models.Model):
    service_name = models.ForeignKey(PortfolioServices, on_delete=models.CASCADE)
    service_description = models.TextField(help_text='Description for service detail add ass many as needed')
    

    class Meta:
        verbose_name = "10-2 - Services Section Detail Descrition"
        verbose_name_plural = "10-2 - Services Section Detail Description"

    def __str__(self):
        return f"{self.service_name}"

class PortfolioTestimonials(models.Model):
    testimonial_name = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    testimonial_img = models.ImageField(upload_to='testimonial_images/')
    testimonial_company = models.CharField()

    class Meta:
        verbose_name = "11 - Testimonial Section"
        verbose_name_plural = "11 - Testimonial Section"

    def __str__(self):
        return f"{self.testimonial_name}"
    


class PortfolioPortfolioDes(models.Model):
    portfolio_des = models.TextField()

    class Meta:
        verbose_name = "12 - Portfolio Description"
        verbose_name_plural = "12 - Portfolio Description"

    def __str__(self):
        return f"{self.portfolio_des}"
    

class PortfolioFilter(models.Model):
    filter_name = models.SlugField(max_length=50, unique=True, help_text="Used as CSS class. Eg: filter-app")
    filter_display_text = models.CharField(max_length=100, help_text="Text to show in filter menu. Eg: App")

    def __str__(self):
        return self.filter_display_text

    class Meta:
        verbose_name = "13 - Portfolio Filters"
        verbose_name_plural = "13 - Portfolio Filters"



class PortfolioItem(models.Model):
    port_item_category = models.ForeignKey(PortfolioFilter, on_delete=models.CASCADE)
    port_item_title = models.CharField(max_length=200, unique=True)
    port_item_image = models.ImageField(upload_to='portfolio/')
    port_item_description = models.TextField()

    port_item_detail_client = models.CharField(max_length=200)
    port_item_detail_project_url = models.URLField(null=True, blank = True, help_text='Leave empty if not needed')
    
    port_item_detail_description = models.TextField()

    port_item_created_date = models.DateField()

    port_item_slug = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "14-1 - Portfolio Items"
        verbose_name_plural = "14-1 - Portfolio Items"

    def __str__(self):
        return self.port_item_title
    

    def save(self, *args, **kwargs):
        if not self.port_item_slug:
            self.port_item_slug =  slugify(self.port_item_title)
        return super().save(*args, **kwargs)
    

class PortfolioItemDetailImages(models.Model):
    port_item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE)
    port_item_detail_image = models.ImageField(upload_to='portfolio_detail/')

    class Meta:
        verbose_name = "14-2 - Portfolio Item Detail Images"
        verbose_name_plural = "14-2 - Portfolio Item Detail Images"

    def __str__(self):
        return f"{self.port_item}"
    
class ContactDescription(models.Model):
    contact_des = models.TextField()

    class Meta:
        verbose_name = '15 Contact Description'
        verbose_name_plural = '15 Contact Description'
    def __str__(self):
        return f"{self.contact_des}"

class ContactInfoLocation(models.Model):
    location_embed_map = models.TextField(help_text="Paste Google Maps iframe embed code here")

    class Meta:
        verbose_name = '16 Contact Location'
        verbose_name_plural = '16 Contact Location'
    def __str__(self):
        return f"{self.location_embed_map}"
    

class ContactDataByUser(models.Model):
    con_name = models.CharField(max_length=100)
    con_email = models.EmailField()
    con_sub = models.CharField(max_length=50)
    con_msg = models.TextField()


    class Meta:
        verbose_name = '17 Contact Data By User'
        verbose_name_plural = '17 Contact Data By User'
    def __str__(self):
        return f"{self.con_name} - {self.con_email} - {self.con_sub} - {self.con_msg}"

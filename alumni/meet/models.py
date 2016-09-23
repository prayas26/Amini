from django.db import models
import datetime
from smart_selects.db_fields import ChainedForeignKey

now = datetime.datetime.now()

GENDER_CHOICE = (
	('M', 'Male'),
	('F', 'Female'),
)

def upload_location(enrollment_no, filename):
    filebase, extension = filename.split(".")
    return "%s.%s" %(enrollment_no, extension)

class campus_select(models.Model):
	campus = models.CharField('Campus', max_length=20)

	def __unicode__(self):
		return self.campus
		
class branch_select(models.Model):
	from_campus = models.ForeignKey(campus_select,)
	branch = models.CharField('Branch', max_length=70)

	def __unicode__(self):
		return self.branch

class Alumnus(models.Model):
	enrollment_no = models.CharField('Enrollment No.', max_length=12, primary_key=True, default='AXXXXXXXXXXX')
	name = models.CharField(max_length=50)
	gender = models.CharField(default='Gender', max_length=1, choices=GENDER_CHOICE)
	dob = models.DateField('Date of Birth', default = '1994-01-01')
	contactno = models.IntegerField('Contact No.')
	image = models.ImageField('Add Image', upload_to=upload_location)
	fblink = models.CharField('Facebook ID Link', default='http://www.facebook.com/', max_length=100)
	linkedin = models.CharField('LinkedIn Link', default='http://www.linkedin.com/', max_length=100)
	email = models.EmailField('Email ID',)
	campus = models.ForeignKey(campus_select)
	branch = ChainedForeignKey(
		'branch_select',
		chained_field = "from_campus",
		chained_model_field="from_campus", 
        show_all=True, 
        auto_choose=True
		)
	batch = models.IntegerField('Passout Year', default='%d' %now.year)
	placed = models.CharField('Presently Placed at', max_length=100, default='Where are you presently working?')

	class Meta:
		ordering = ('name', 'batch')

	def __unicode__(self):
		return self.name

class Answer(models.Model):
	answer = models.CharField('Things you will miss the most', max_length=100)

class Suggest(models.Model):
	sname = models.CharField('Name', max_length=50)
	semail = models.EmailField('Email ID')
	smessage = models.TextField('Message', max_length=250)
	
	class Meta:
		ordering = ('semail', 'smessage')
	
	def __unicode__(self2):
		return self2.sname
	
class Change(models.Model):
    cname = models.CharField('Name', max_length=50)
    cbatch = models.IntegerField('Passout Year')
    cemail = models.EmailField('Email ID')
    ccontact = models.IntegerField('Contact No.')
    cdetail = models.TextField('Changes', max_length=500)
	
    class Meta:
    	ordering = ('cname', 'cemail')
		
    def __unicode__(self3):
    	return self3.cemail
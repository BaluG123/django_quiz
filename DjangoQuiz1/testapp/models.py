from django.db import models

# Create your models here.
class six(models.Model):
    Subject_Choices=(('science','Science'),('socialscience','SocialScience'),('maths','Maths'))
    subject=models.CharField(max_length=15,choices=Subject_Choices)
    question=models.CharField(max_length=100000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-created']    

class seven(models.Model):
    Subject_Choices=(('science','Science'),('socialscience','SocialScience'),('maths','Maths'))
    subject=models.CharField(max_length=15,choices=Subject_Choices)
    question=models.CharField(max_length=100000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-created']    

class eight(models.Model):
    Subject_Choices=(('science','Science'),('socialscience','SocialScience'),('maths','Maths'))
    subject=models.CharField(max_length=15,choices=Subject_Choices)
    question=models.CharField(max_length=100000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-created']    

class nine(models.Model):
    Subject_Choices=(('science','Science'),('socialscience','SocialScience'),('maths','Maths'))
    subject=models.CharField(max_length=15,choices=Subject_Choices)
    question=models.CharField(max_length=100000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-created']    

class ten(models.Model):
    Subject_Choices=(('science','Science'),('socialscience','SocialScience'),('maths','Maths'))
    subject=models.CharField(max_length=15,choices=Subject_Choices)
    question=models.CharField(max_length=100000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-created']                                    

class CurrentAffairs(models.Model):
    question=models.CharField(max_length=100000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question

    class Meta:
        ordering=['-created']    

class GeneralKnowledge(models.Model):
    question=models.CharField(max_length=100000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question

    class Meta:
        ordering=['-created'] 

from django.db import models

class student(models.Model):
    sid = models.IntegerField(primary_key=True, auto_created=True)
    sname = models.CharField(max_length=50, null= False)
    semail = models.EmailField( null= False)
    scity = models.CharField(max_length=50, null= False)
    sbranch = models.CharField(max_length=50, null= False)
   

    def __str__(self):
        return {
            "Student Id ": self.sid,
            "Student Name" : self.sname,
            "Student Email" : self.semail,
            "Student City" : self.semail,
            "Student Branch" : self.semail,
            "Student Picture" : self.semail
               }
    def __repr__(self):
        return str(self)

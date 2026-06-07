from django.db import models

# Create your models here.

class Hotel(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Food(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='htl')

    def __str__(self):
        return self.name
    


# from django.db import models

# # Create your models here.
# class Student(models.Model):
#     name=models.CharField(max_length=20)
#     age=models.IntegerField()
#     def __str__(self):
#         return self.name
    

# One-to-Many with Student
# class Assignment(models.Model):
#     student = models.ForeignKey(
#         Student,
#         on_delete=models.CASCADE,
#         related_name="assignments"
#     )
#     title = models.CharField(max_length=200)
#     marks = models.IntegerField()

#     def __str__(self):
#         return self.title


# One-to-One with Student
# class StudentProfile(models.Model):
    # student = models.OneToOneField(
    #     Student,
    #     on_delete=models.CASCADE,
    #     related_name="profile"
    # )
    # address = models.TextField()
    # phone = models.CharField(max_length=15)

    # def __str__(self):
    #     return f"{self.student.name} Profile"


 ## Many-to-Many with Student
# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     students = models.ManyToManyField(
#         Student,
#         related_name="courses"
#     )

#     def __str__(self):
#         return self.name


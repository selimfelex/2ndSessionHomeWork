class Udacian():
    def __init__(self,name, city, enrollment, nanodegree, status):
       self.student_name= name
       self.city_name = city
       self.enrolment_name = enrollment
       self.nanodegree_name = nanodegree
       self.status_code = status

    def print_udacian(self):
                print("student " + self.student_name + " is enrolled in " + self.city_name + " studing "
                        + self.enrolment_name + " in " + self.nanodegree_name + " and hi is " + self.status_code)


student_object =  Udacian("Selim","Riyadh","FSND","MON","active")
print(student_object.print_udacian())


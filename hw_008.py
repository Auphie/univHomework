name = input()
birth = input()
FirstName = name.split()[0]
LastName = name.split()[1]
yyyy = birth.split('/')[0]
mm = birth.split('/')[1]
dd = birth.split('/')[2]
print('{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.'.format(FirstName=FirstName, yyyy=yyyy,mm=mm,dd=dd,LastName=LastName))
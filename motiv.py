# Calculation of my motivation but the data can easily be changed
# old - this is the data for last year, for example, in December 2018 there were 100 applications
# new-data for this year, for example for December 2019 there were 200 applications
# prosent is an increase in the percentage of growth, for example pplan +10%, 100+10%
# in prosent the if function displays the data plan+motivation completed or not
# raschet vyvodit data as not Havtan applications to the plan
# motiv is a monetary motivation for every 50 applications in my case

old = int(input('enter last years data '))
new = int(input('enter the data for this year '))
prosent = (int(old/100*10))+old
if (prosent+50) <= new:
  print("The plan is executed!")
else:
  nehv = (prosent + 50) - new
  print("poorly - ", nehv, "application")
raschet = new-prosent
motiv = (raschet/50)*3000
print (int(motiv), "ETB", prosent,"application plan")

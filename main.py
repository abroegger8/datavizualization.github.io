import json
import os
import matplotlib.pyplot as plt
import numpy as np

#Graph 1 (China vs. USA GDP Comparison)
gdp_china = []
chinagdp = '/Users/alexbroegger/Desktop/Data Visualization/chinagdp.json'
with open(chinagdp, encoding='ascii') as f:
    chinagdp = f.read()
    gdp_china += json.loads(chinagdp)

y_china=[]
for dict in gdp_china[1]:
    y_china.append(dict['value'])

x_china=[]
for year_china in range(2020, 1959, -1):
    x_china.append(year_china)

gdp_usa = []
unitedstatesgdp = '/Users/alexbroegger/Desktop/Data Visualization/unitedstatesgdp.json'
with open(unitedstatesgdp, encoding='ascii') as f:
    unitedstatesgdp = f.read()
    gdp_usa += json.loads(unitedstatesgdp)

y_US=[]
for dict in gdp_usa[1]:
    y_US.append(dict['value'])

x_US=[]
for year_US in range(2020, 1959, -1):
    x_US.append(year_US)

plt.xlabel('Years')
plt.ylabel('GDP (ten trillions)')
plt.title('China vs. USA GDP Over Time by Alex Broegger')
plt.plot(x_US, y_US, label = 'US\'s GDP')
plt.plot(x_china, y_china, label = 'China\'s GDP')
plt.legend()
plt.savefig('CHINAvsUSA_GDP_comparison.png')
plt.show() 

#Graph 2 (Astronauts on ISS vs. Shenzhou 13)

astronauts = []
spacepeople = '/Users/alexbroegger/Desktop/Data Visualization/spacepeople.json'
with open(spacepeople, encoding='ascii') as f:
    spacepeople = f.read()
    astronauts += json.loads(spacepeople)
number_astronauts_ISS = 7
number_astronauts_shenzhou = 3
number_astronauts = 10

percent_ISS = (number_astronauts_ISS/number_astronauts)*100
percent_shenzhou = (number_astronauts_shenzhou/number_astronauts)*100

fig, ax = plt.subplots()
y = np.array([percent_ISS, percent_shenzhou])
mylabels = ["ISS (70%)", "Shenzhou 13 (30%)"]
plt.pie(y, labels = mylabels, startangle = 90)
ax.set_title('Percentage of Astronauts in Space on ISS vs. Shenzhou 13 by Alex Broegger')
plt.savefig('ISSvsShenzhou_Astronaut_comparison.png')
plt.show()
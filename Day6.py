c={'Sunio':'Nobita','Marvel':'Henry','Hulk':'Saski','Naruto':'Dora'}
r={'nobita':'80%','Henry':'85%','Hulk':'75%','Dora':'100%'}
#merge 2 python dictionaries
cr={**c,**r}
print('new dictionary:',cr)
#remove a particular key from the dictionary
cr.pop('Dora')
print('dictionary after deletion:',cr)
#map two lists into a dictionary
q={'jesus','geetha','love','kai'}
s={'jissa','jayan','hate','mine'}
a=zip(q,s)
d=dict(a)
print('d:',d)
o={'karthick',34,56,89,'daniel'}
print('set :',o)
print('length of the set:',len(o))
p1={1,67,890,23,143}
p2={23,3,1,45,167,12,6}
p3={29,45,7,90,1}
p4={1,2,3,29,7,00}
print('***Original sets***')
print('p1:',p1)
print('p2:',p2)
print('p3:',p3)
print('p4:',p4)
print('remove the intersection of a 2nd set from the 1st set using difference_update():')
s1.difference_update(p2)
print('p1:',p1)
print('p2:',p2)
print('remove the intersection of a 4th set from the 3rd set using -=operator:')
p4-=p3
print('p3:',p3)
print('p4:',p4)

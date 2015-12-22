'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

fw = open('sample.txt', 'w')
fw.write('hi, pukeng ina mo!!\n')
fw.write('panget mong putanginang hinayupak ka! \n')
fw.close()


###############

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

# - *- coding: utf- 8 - *-
#coEjere
import csv
import operator

def sum_of_property_DK():
	ejer_dict = dict()
	sorted_ejer_dict = dict()
	with open('coEjere.csv', 'r') as csvfile:
		reader = csv.reader(csvfile)
		#LAVER 	DICT MED EJERNAVN OG KØBESUM
		for row in reader:
			try:
				if row[9] in ejer_dict:
					ejer_dict[row[9]].append(float(row[15]))
				else:
					ejer_dict[row[9]] = [float(row[15])]
			except:
				ejer_dict[row[9]] = [float(0)]
		#SUMMERER ALLE KØBESUMME PR EJERNAVN
		for item in ejer_dict:
			sorted_ejer_dict[item] = sum(ejer_dict[item])
		#SORTERER EFTER STØRSTE SAMLEDE KØBESUM
		sorted_ejer_list = sorted(sorted_ejer_dict.items(), key=operator.itemgetter(1), reverse=True)
		sorted_ejer_tuple = tuple(sorted_ejer_list)
		#SKRIVER TIL CSV-FIL
		with open('outfile.csv','wb') as out:
		    writer = csv.writer(out, delimiter=';')
		    writer.writerows(sorted_ejer_tuple)
			
		out.close()    	
	csvfile.close()


#MANGLER AT TÆLLE ANTALLET AF FOREKOMSTER PER EJER - EVT DEL DET OP PÅ KOMMUNE FOR AT FÅ LOKALE AKTØRER

#Ejendomsejernummer = 6, ejernavn = 9, købesum = 15


'''

{'18641534': ['1500000'], '56675817': ['0'], '36502428': ['0'], '58574813': ['0'], '32555136': ['39500000'], '32838278': ['6199800'],
 '29975108': ['3800000'], '66264815': ['567000'], '33167555': ['0'], '28886543': ['500000'], '68533317': ['0'], '24243427': ['45000'],
 '29421536': ['4000000'], '27223028': ['750300'], '29932840': ['33426575'], '24243893': ['45000'], '27177301': ['0'], '21278378': ['7000000'],
 '15944838': ['5300000'], '89351413': ['0'], '15128984': ['1458000'], '15108592': ['15800000'], '24243907': ['45000']}


 {'ELTIME EJENDOMME ApS': ['0'], 'BEDRE BOLIG EJENDOMME ApS AF 2003': ['750300'],
 'DIRACH EJENDOMME ApS': ['5300000'], 'APG SLANGERUP ApS': ['0'], 'STEENSBJERG A/S': ['7000000'],
 'NILAUS ApS': ['45000'], 'NDP KARLSLUNDE ApS': ['39500000'], 'LIND OG RIS\xd8R HOLDING A/S': ['15800000'],
 'K/S EGEDALSCENTRET': ['33426575'], 'BORGEN EJENDOMME A/S': ['567000'], 'J\xc6GERBYG A/S': ['500000'],
 'EJENDOMSSELSKABET H\xc5NDV\xc6RKERVANGEN': ['4000000'], '\xc5.K.M. ApS ADMINISTRATION': ['0'],
 'LINDH EJENDOMME ApS': ['3800000'], 'DANCOP A/S': ['1500000'], 'TELEDYNE RESON A/S': ['0'],
 'EJENDOMSSELSKABET AF 1.11.1979 ApS': ['0'], 'ALINI ApS': ['45000'], 'Umove Ejendomme II ApS': ['1458000'],
 'ASX 620 MEZZANIN A/S': ['0'], 'Ejerlejlighedsforeningen': ['0'], 'JN INVEST OG BOLIG ApS': ['45000'], 'NYHUUS EJENDOMME ApS': ['6199800']}
 '''
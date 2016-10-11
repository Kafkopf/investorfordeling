# - *- coding: utf- 8 - *-
#Ejere af aktier
#Side fra Bentow: http://www.nationalbanken.dk/da/statistik/find_statistik/Sider/V%C3%A6rdipapirer-p%C3%A5-fondskodeniveau.aspx
import csv
import operator

def sum_of_markedsvaerdi():
	investor_dict = dict()
	sum_investor_dict = dict()
	husholdning_dict = dict()
	pct_investor_dict = dict()
	
	with open('fondskode_201608.csv', 'r') as csvfile:
		next(csvfile)
		reader = csv.reader(csvfile, delimiter=';')

		#SAMLER ALLE MARKEDSVARDI I DICT PR PAPIRNAVN
		for row in reader:
			if row[3] in investor_dict:
				investor_dict[row[3]].append(float(row[11].replace(',','.')))
			else:
				investor_dict[row[3]] = [float(row[11].replace(',','.'))]

		#SUMMERER ALLE MARKEDSVAERDI PR PAPIRNAVN
		for item in investor_dict:
			sum_investor_dict[item] = sum(investor_dict[item])
	
		#LAVER DICT MED HUSHOLDNINGERE	
	with open('fondskode_201608.csv', 'r') as csvfile:
		next(csvfile)
		reader = csv.reader(csvfile, delimiter=';')
		for row in reader:
			if row[9] == "1.5.0. Husholdninger, inkl. non-profit institutioner rettet mod hush.":
				husholdning_dict[row[3]] = float(row[11].replace(',','.'))

		#DIVIDERER DE TO DICTS FOR AT FÅ PCT SOM HUSHOLDNINGER UDGØR AF DE SAMLEDE INVESTERINGER
		for k in husholdning_dict:
			if sum_investor_dict[k] > 0:
				pct_investor_dict[k] = float(husholdning_dict[k] / sum_investor_dict[k] * 100)

		#SORTERER EFTER HØJESTE PCT
	sorted_investor_list = sorted(pct_investor_dict.items(), key=operator.itemgetter(1), reverse=True)
	sorted_investor_tuple = tuple(sorted_investor_list)
	
		#SKRIVER TIL CSV-FIL
	with open('outfile.csv','wb') as out:
	    writer = csv.writer(out, delimiter=';')
	    writer.writerows(sorted_investor_tuple)
	out.close()
	csvfile.close()

sum_of_markedsvaerdi()


'''
Frekvens;Reference periode;ISIN_kode;papirnavn;Vardipapirtype;Valuta;Restlobetid;Renter;Udstedersektor;Investorsektor;nominel;markedsvaerdi;ejerkoncentration;Fortroligt
Manedlig;201608;DK0002000421;6,00% UNIKREDIT ANN 1993 2026;Obligationer, noterede;Danske kroner;restlobetid>1 ar (inkl. uendelig lobetid);5% < kupon <= 6%;MFI - Realkreditinstitutter;1.4.0. Offentlig forvaltning og service;0,997991;1,102780055;M;
Manedlig;201608;DK0002000421;6,00% UNIKREDIT ANN 1993 2026;Obligationer, noterede;Danske kroner;restlobetid>1 ar (inkl. uendelig lobetid);5% < kupon <= 6%;MFI - Realkreditinstitutter;1.1.0 Ikke-finansielle selskaber;0,52720669;0,58256339245;M;
Manedlig;201608;DK0002000421;6,00% UNIKREDIT ANN 1993 2026;Obligationer, noterede;Danske kroner;restlobetid>1 ar (inkl. uendelig lobetid);5% < kupon <= 6%;MFI - Realkreditinstitutter;1.0.0. Alle indenlandske sektorer (Danmark);7,25493948;8,0167081254;M;
'''
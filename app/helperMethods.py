from .sqlQueries import returnListFromQuery, mlsNumQuery

def searchDictFromList(listings):
	"""Creates a dictionary from a list pass in for a mls listing or set of listings mainly for readability purposes"""
	

	dictResult = []
	toBeDict = []
	dictToBeAdded = {'mls_num':None, 'property_type': None, 'list_price':None, 'property_address': None, 
					'property_streetname': None, 'property_streetname_ext': None, 'property_county': None, 
					'property_zip': None, 'remarks': None, 'num_bedrooms': None, 'num_total_baths': None,
					'square_footage_finished': None}

	for row in listings:
		for item in row:
			toBeDict.append(str(item))

		dictToBeAdded['mls_num']= toBeDict[0]
		
		dictToBeAdded['property_type']= toBeDict[1]
		dictToBeAdded['list_price']= float(toBeDict[2])

		if toBeDict[3] == 'None':
			dictToBeAdded['property_address']= None
		else:
			dictToBeAdded['property_address']= toBeDict[3]

		dictToBeAdded['property_streetname']= toBeDict[4]

		if toBeDict[5] == 'None':
			dictToBeAdded['property_streetname_ext']= None
		else:
			dictToBeAdded['property_streetname_ext']= toBeDict[5]

		dictToBeAdded['property_county']= toBeDict[6]
		dictToBeAdded['property_zip']= toBeDict[7]
		
		if toBeDict[8] == 'None':
			dictToBeAdded['remarks']= None
		else:
			dictToBeAdded['remarks']= toBeDict[8]

		dictToBeAdded['num_bedrooms']= toBeDict[9]
		dictToBeAdded['num_total_baths']= toBeDict[10]
		dictToBeAdded['square_footage_finished']= toBeDict[11]
		
		toBeDict=[]

		dictResult.append(dictToBeAdded.copy())
		

	return dictResult

def mlsResultToDict(db, mlsnum):
	"""retrieving information about a specific listing by mls number then returning dictionary of info"""
	query = mlsNumQuery(mlsnum)
	result = []
	result = returnListFromQuery(db,query)
	toBeDict = result[0]
	dictToBeAdded = {'mls_num':None, 'list_price':None, 'tax_cost': None, 'owner_type': None, 'property_type': None,'take_posession_time': None,
					'remarks': None, 'directions':None, 'property_address': None, 'property_streetname': None, 'property_streetname_ext': None,
					'property_county': None, 'property_zip': None, 'area': None, 'subdivision': None,'sewer_type': None, 'acres': None,
					'lot_description': None, 'elementary_school': None, 'middle_school': None, 'high_school': None, 'listing_office_name': None,
					'year_built': None, 'square_footage_finished': None, 'num_rooms': None, 'num_bedrooms': None, 'num_stories': None,
					'num_full_baths': None, 'num_total_baths': None, 'master_bedroom_level': None, 'basement': None, 'garage': None,
					'num_fireplaces': None, 'pool': None, 'construction': None, 'structure_type': None, 'roof_construction': None,
					'handicap_equipped': None, 'house_style': None, 'appliances': None, 'cooling_system_type': None, 'heat_source': None,
					'heating_system_type': None, 'basement_type': None, 'community_amenities': None, 'parking_type': None,'interior_features': None,
					'exterior_features': None}

	dictToBeAdded['mls_num']= toBeDict[0]
	dictToBeAdded['list_price']= toBeDict[1]
	dictToBeAdded['tax_cost']= float(toBeDict[2])
	dictToBeAdded['owner_type']= toBeDict[3]
	dictToBeAdded['property_type']= toBeDict[4]
	dictToBeAdded['take_posession_time']= toBeDict[5]
	dictToBeAdded['remarks']= toBeDict[6]
	dictToBeAdded['directions']= toBeDict[7]
	dictToBeAdded['property_address']= toBeDict[8]
	dictToBeAdded['property_streetname']= toBeDict[9]
	dictToBeAdded['property_streetname_ext']= toBeDict[10]
	dictToBeAdded['property_county']= toBeDict[11]
	dictToBeAdded['property_zip']= toBeDict[12]
	dictToBeAdded['area']= toBeDict[13]
	dictToBeAdded['subdivision']= toBeDict[14]
	dictToBeAdded['sewer_type']= toBeDict[15]
	dictToBeAdded['acres']= toBeDict[16]
	dictToBeAdded['lot_description']= toBeDict[17]
	dictToBeAdded['elementary_school']= toBeDict[18]
	dictToBeAdded['middle_school']= toBeDict[19]
	dictToBeAdded['high_school']= toBeDict[20]
	dictToBeAdded['listing_office_name']= toBeDict[21]
	dictToBeAdded['year_built']= toBeDict[22]
	dictToBeAdded['square_footage_finished']= toBeDict[23]
	dictToBeAdded['num_rooms']= toBeDict[24]
	dictToBeAdded['num_bedrooms']= toBeDict[25]
	dictToBeAdded['num_stories']= toBeDict[26]
	dictToBeAdded['num_full_baths']= toBeDict[27]
	dictToBeAdded['num_total_baths']= toBeDict[28]
	dictToBeAdded['master_bedroom_level']= toBeDict[29]
	dictToBeAdded['basement']= toBeDict[30]
	dictToBeAdded['garage']= toBeDict[31]
	dictToBeAdded['num_fireplaces']= toBeDict[32]
	dictToBeAdded['pool']= toBeDict[33]
	dictToBeAdded['construction']= toBeDict[34]
	dictToBeAdded['structure_type']= toBeDict[35]
	dictToBeAdded['roof_construction']= toBeDict[36]
	dictToBeAdded['handicap_equipped']= toBeDict[37]
	dictToBeAdded['house_style']= toBeDict[38]
	dictToBeAdded['appliances']= toBeDict[39]
	dictToBeAdded['cooling_system_type']= toBeDict[40]
	dictToBeAdded['heat_source']= toBeDict[41]
	dictToBeAdded['heating_system_type']= toBeDict[42]
	dictToBeAdded['basement_type']= toBeDict[43]
	dictToBeAdded['community_amenities']= toBeDict[44]
	dictToBeAdded['parking_type']= toBeDict[45]
	dictToBeAdded['interior_features']= toBeDict[46]
	dictToBeAdded['exterior_features']= toBeDict[47]

	
	"""
	if toBeDict[3] == 'None':
		dictToBeAdded['property_address']= None
	else:
		dictToBeAdded['property_address']= toBeDict[3]
		"""
	return dictToBeAdded
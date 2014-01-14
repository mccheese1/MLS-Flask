
"""Creating a few variables to be used as sql queries or parts of sql queries"""
searchResultQuery = 'select mls_num, property_type, list_price, property_address, property_streetname,'
searchResultQuery +=' property_streetname_ext, property_county, property_zip, remarks, num_bedrooms, num_total_baths,'
searchResultQuery +=' square_footage_finished from listing where '

lastImportDate = 'select date from import order by id desc limit 1;'

mlsNumSearch = 'select mls_num, list_price, tax_cost, owner_type, property_type, take_posession_time, remarks, directions,'
mlsNumSearch +=' property_address, property_streetname, property_streetname_ext, property_county, property_zip, area, subdivision,'
mlsNumSearch +=' sewer_type, acres, lot_description, elementary_school, middle_school, high_school, listing_office_name, year_built,'
mlsNumSearch +=' square_footage_finished, num_rooms, num_bedrooms, num_stories, num_full_baths, num_total_baths, master_bedroom_level,'
mlsNumSearch +=' basement, garage, num_fireplaces, pool, construction, structure_type, roof_construction, handicap_equipped, house_style,'
mlsNumSearch +=' appliances, cooling_system_type, heat_source, heating_system_type, basement_type, community_amenities, parking_type,'
mlsNumSearch +=' interior_features, exterior_features from listing where mls_num = '


def buildListingsQuery(form):
	"""Building a query for mls listings based off of form data then sending it back to be executed"""
	sql = searchResultQuery
	#add property_type values to sql statement where clause
	if form.propertyType.data:
		sql += 'property_type in ('
		for item in form.propertyType.data:
			sql+=("'"+str(item)+"'"+', ')
		sql=sql[:-2]
		sql+=')'
	else:
		sql += "property_type like '%'"
	#add area values to sql statement where clause
	if form.areaSelect.data:
		sql += ' and area in (' 
		for item in form.areaSelect.data:
			sql+=(str(item)+', ')
		sql=sql[:-2]
		sql+=')'
	#add price values to sql statement where clause
	if form.minPrice.data:
		sql += ' and list_price > ' 
		sql +=str(form.minPrice.data)
	if form.maxPrice.data:
		sql += ' and list_price < ' 
		sql +=str(form.maxPrice.data)
	#add square feet values to sql statement where clause
	if form.minSqFeetSelect.data != 0:
		sql += ' and square_footage_finished > ' 
		sql +=str(form.minSqFeetSelect.data)
	if form.maxSqFeetSelect.data != 0:
		sql += ' and square_footage_finished < ' 
		sql +=str(form.maxSqFeetSelect.data)
	#add acre values to sql statement where clause
	if form.minAcresSelect.data != 0:
		sql += ' and acres > ' 
		sql +=str(form.minAcresSelect.data)
	if form.maxAcresSelect.data != 0:
		sql += ' and acres < ' 
		sql +=str(form.maxAcresSelect.data)
	#add bedroom value to sql statement where clause
	if form.bedroomSelect.data != 0:
		sql += ' and num_bedrooms > ' 
		sql += str(form.bathSelect.data)
	#add bath value to sql statement where clause
	if form.bathSelect.data != 0:
		sql += ' and num_total_baths > ' 
		sql += str(form.bathSelect.data)
	#add basement value to sql statement where clause
	if form.basementSelect.data != '0':
		sql += ' and garage = '
		sql += "'"+form.basementSelect.data+"'"
	#add garage value to sql statement where clause
	if form.garageSelect.data != '0':
		sql += ' and garage = '
		sql += "'"+form.garageSelect.data+"'"
	#add master bed level value to sql statement where clause
	if form.masterFloorSelect.data != 4:
		sql += ' and master_bedroom_level = '
		if form.masterFloorSelect.data == 0:
			sql += "'basement'"
		else:
			sql += "'"+str(form.masterFloorSelect.data)+"'"
	#add mls_num values to sql statement where clause
	if form.mlsNum.data:
		sql += ' and mls_num = ' 
		sql += str(form.mlsNum.data)

	#sql += ' order by list_price'
	#sql += ' limit 10'
	
	return sql

def setOrderBy(query, order):
	"""adding order by clause to query argument string"""
	if order == 'MLS ID#':
		order = ' order by mls_num' 
	elif order =='Price Highest to Lowest':
		order = ' order by list_price desc'
	elif order =='Price Lowest to Highest':
		order = ' order by list_price asc'
	query += order
	return query

def setLimitOffset(query, limit, offset):
	"""adding limit and offset clause to query argument string"""
	query += ' limit '+str(limit)+' offset '+str(offset)
	return query

def mlsNumQuery(mlsNum):
	"""Building a query to retrieve data for an individual listing based on MLS number"""
	sql = mlsNumSearch
	sql += str(mlsNum)
	return sql

def returnListFromQuery(db, query):
	""" Accepts a database connection and a query as parameters then executes the query and sends
		the result set back as the return value"""

	cur = db.cursor()

	result = []
	cur.execute(query)
	row = cur.fetchone()
	while row is not None:
		result.append(row)
		row = cur.fetchone()
			
	cur.close()

	return result
from flask.ext.wtf import Form
from wtforms import SelectMultipleField, DecimalField, widgets, SelectField, IntegerField
from wtforms.validators import Required, Optional
from app.searchOptions import *


class MultiCheckboxField(SelectMultipleField):
    """Checkbox form input"""
    
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
 
 
class mlsSearchForm(Form):
    """creating form field - Choices for select fields are pulled from searchOptions.py"""

    propertyType = MultiCheckboxField(u'Category', choices=category)

    minPrice = DecimalField(u'Min Price:', validators = [Optional(strip_whitespace=True)])
    maxPrice = DecimalField(u'Max Price:', validators = [Optional(strip_whitespace=True)])

    areaSelect = SelectMultipleField(u'Area:', choices=area, coerce=int)

    minSqFeetSelect = SelectField(u'Min Square Feet:', choices=minSqFeet, coerce=int)
    maxSqFeetSelect = SelectField(u'Max Square Feet:', choices=maxSqFeet, coerce=int)

    minAcresSelect = SelectField(u'Min Acres:', choices=minAcres, coerce=int)
    maxAcresSelect = SelectField(u'Max Acres:', choices=maxAcres, coerce=int)

    bathSelect = SelectField(u'Baths:', choices=numBedBath, coerce=int)
    bedroomSelect = SelectField(u'Bedrooms:', choices=numBedBath, coerce=int)

    basementSelect = SelectField(u'Basment:', choices=yesNo)
    garageSelect = SelectField(u'Garage:', choices=yesNo)

    masterFloorSelect = SelectField(u'Master Bed Level:', choices=masterFloor, coerce=int)

    displayGroupSelect = SelectField(u'Display in Groups of:', choices=displayGroups,coerce=int)

    mlsNum = IntegerField(u'Search By MLS Number:', validators = [Optional(strip_whitespace=True)])


class listingSortForm(Form):
    """creating form field - Choices for select fields are pulled from searchOptions.py"""

    sortOrderSelect = SelectField(u'Currently Sorting By:', choices=sortParam, coerce=str)





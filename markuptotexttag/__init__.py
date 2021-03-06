#    This package is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Wesley Hansen"
__date__ = "07/06/2012 11:29:17 PM"
'''
The markuptotexttag package contains the function `convertMarkup` that
will parse a string that is formatted with pango markup and convert
it into GtkTextTags that can be retrieved via the MarkupProps iterator.
'''
import pango
from markuptotexttag.properties import MarkupProps

def convertMarkup(string):
	'''
	Parses the string and returns a MarkupProps instance
	'''
	attr_values = ('value', 'ink_rect', 'logical_rect', 'desc', 'color')
	attr_list, text, accel = pango.parse_markup( string )
	attr_iter = attr_list.get_iterator()
	
	props = MarkupProps()
	props.text = text
	
	val = True
	while val:
		attrs = attr_iter.get_attrs()
		
		for attr in attrs:
			name = attr.type
			start = attr.start_index
			end = attr.end_index
			name = pango.AttrType(name).value_nick
			
			value = None
			for attr_value in attr_values:
				if hasattr( attr, attr_value ):
					value = getattr( attr, attr_value )
					break
			if name == 'font_desc':
				name = 'font'
			props.add( name, value, start, end )

		val = attr_iter.next()

	return props
		

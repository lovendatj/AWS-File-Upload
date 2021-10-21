import StandardLibrary.AWS.Dynamo as dynamo

# Insert new row
key = dynamo.insert_row('reading', {'test': 1234})
# Get row
dynamo.read_row('reading', key)
# Update row
dynamo.update_row('reading', key, 'fname', 'bob')
# Delete row
dynamo.remove_row('reading', key)

# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

t_terms = [term_doc.get('name') for term_doc in artist.top_terms()]

term_artists = artist.search(description=t_terms[2:4])

print 'Artists matching these top terms: ', ', '.join(t_terms[2:4])
for term_artist in term_artists:
    artist_terms = [term_doc.get('name') for term_doc in term_artist.terms[0:4]]
    print '%-30s terms: %s' % (term_artist.name[0:28] + ', ', ', '.join(artist_terms))

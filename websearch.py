from taser.proto.http.websearch import WebSearch

s = WebSearch(search_engine='google', search_query='apartments')

with open('output.txt', 'w') as output:
    output.write(s.start())
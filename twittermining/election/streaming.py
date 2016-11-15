from ..core.streaming import stream_into_db

def stream():
	search_topic = 'Election2016'
	stream_into_db(search_topic)
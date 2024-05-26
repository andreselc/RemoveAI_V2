from gradio_client import Client

client = Client("amirgame197/Remove-Video-Background")
result = client.predict(
		{"video":"./aoafs.mp4","subtitles":None},	# Dict(video: filepath, subtitles: filepath | None)  in 'parameter_2' Video component
		"Fast",	# Literal['Normal', 'Fast']  in 'Select mode' Radio component
		api_name="/predict"
)
print(result)
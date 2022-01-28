from google.cloud import vision

with open('./images/星先生.jpeg', 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

annotator_client = vision.ImageAnnotatorClient()

response_data = annotator_client.label_detection(image=image)

labels = response_data.label_annotations

print('-----Result of analysis!!-----' + '\n')
for label in labels:
    print(label.description, ':', round(label.score * 100, 1), '%')
print('\n' + '-----END-----')

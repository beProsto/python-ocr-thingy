import easyocr

reader = easyocr.Reader(['en', 'pl'])

result = reader.readtext('sc3.png')

for (bbox, text, prob) in result:
    print(f'Text: {text}, Probability: {prob}')
